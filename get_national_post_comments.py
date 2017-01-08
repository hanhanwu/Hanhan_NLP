from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
from pprint import pprint


def main():
    article_urls = [
        "http://news.nationalpost.com/full-comment/marni-soupcoff-bob-dylans-nobel-silence-is-golden"
    ]

    for article_url in article_urls:
        driver = webdriver.Firefox()
        driver.get(article_url)
        comment_url = ""
        try:
            comment_url = driver.find_element_by_xpath(".//iframe[@class='fb_ltr']").get_attribute(name='src')
        finally:
            driver.close()

        if comment_url != "":
            driver = webdriver.Firefox()
            driver.get(comment_url)
            time.sleep(3)
            expand_comments_xpath = ".//button[@class='_1gl3 _4jy0 _4jy3 _517h _51sy _42ft']"
            expand_replies_xpath = ".//span[@class=' _50f3 _50f7']"
            try:
                clk1 = ""
                clk2 = ""
                while(clk1 != None):
                    try:
                        clk1 = driver.find_element_by_xpath(expand_comments_xpath)
                        driver.execute_script("arguments[0].scrollIntoView();", clk1)
                        clk1.click()
                        print('Expand Comments', clk1)
                        time.sleep(3)
                    except:
                        break

                while(clk2 != None):
                    try:
                        clk2 = driver.find_element_by_xpath(expand_replies_xpath)
                        driver.execute_script("arguments[0].scrollIntoView();", clk2)
                        clk2.click()
                        print('Expand Comments', clk2)
                        time.sleep(3)
                    except:
                        break

                all_comments = driver.find_elements_by_xpath(".//div[@class='_3-8y _5nz1 clearfix']")
                comments_lst = []
                for t in all_comments:
                    raw_text = t.get_attribute("innerHTML")
                    soup = BeautifulSoup(raw_text, "html.parser")
                    authors = [author.get_text() for author in soup.find_all(["a", "span"], {"class":" UFICommentActorName"})]
                    # locations = [location.get_text() for location in soup.find_all("div", {"class":"_4q1v"})]
                    comments = [comment.get_text() for comment in soup.find_all("span", {"class":"_5mdd"})]
                    times = [t.get_text() for t in soup.find_all("abbr", {"class":"livetimestamp"})]

                    print(len(authors), len(comments), len(times))
                    cmt_dct = {}
                    cmt_dct['comment_author'] = authors[0]
                    cmt_dct['comment'] = comments[0]
                    cmt_dct['comment_time'] = times[0]
                    cmt_dct['replies'] = []
                    for i in range(1, len(authors)):
                        tmp_dct = {}
                        tmp_dct['reply_author'] = authors[i]
                        tmp_dct['reply_comment'] = comments[i]
                        tmp_dct['reply_time'] = times[i]
                        cmt_dct['replies'].append(tmp_dct)
                    comments_lst.append(cmt_dct)

                # TEST
                for c in comments_lst:
                    print(c)

            finally:
                driver.close()

if __name__ == "__main__":
    main()
