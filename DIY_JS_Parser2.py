# Get Comment, Reactions, Reaction Counts
# For each comment url, a browser will be opened and the reaction buttion will be clicked.
# After getting the data, the borwser will be closed.
from selenium import webdriver
import time
import re
from pprint import pprint

image_reaction_map = {
                       "B9CMO5aR": 'funny',
                       "CYVHcC0N":'like',
                       "0cm0eNFD":'disagree',
                       "OQlF5Uky":'sad',
                       "yQIVy5qm":'wow',
                     }

def get_reaction(img_str):
    img_ptn = 'https://assets.civilcomments.com/v1/images/reactions/(\w+)_64.png'
    reaction = image_reaction_map[re.match(img_ptn, img_str).group(1)]
    return reaction



def main():
    comment_urls = [
        "http://www.theglobeandmail.com/opinion/a-fascists-win-americas-moral-loss/article32753320/comments/",
        "http://www.theglobeandmail.com/opinion/academic-extremism-comes-to-canada/article33185073/comments/"
                   ]
    article_id_ptn = "http://www.theglobeandmail.com/.*?/article(\d+)/comments"

    for comment_url in comment_urls:
        article_id = re.match(article_id_ptn, comment_url).group(1)
        driver = webdriver.Firefox()
        driver.get(comment_url)
        time.sleep(5)

        comment_autors = [ca.text for ca in driver.find_elements_by_class_name("c29cjTJ")]
        post_time = [pt.text for pt in driver.find_elements_by_class_name("cNCPihY")]
        comment_text = [cmt.text for cmt in driver.find_elements_by_class_name("c1bE414")]
        comments_reactions = []

        clicks= driver.find_elements_by_css_selector('div.c2iexvC')
        for clk in clicks:
            driver.execute_script("arguments[0].scrollIntoView();", clk)
            clk.click()

            reaction_counts = [rc.text for rc in driver.find_elements_by_class_name('c2oytXt')]
            reaction_users = [ru.text for ru in driver.find_elements_by_class_name('c3TwkwL')]
            reaction_time = [rt.text for rt in driver.find_elements_by_class_name('c_0Qpsz')]
            reactions = [get_reaction(r.get_attribute('src')) for r in driver.find_elements_by_class_name('c3S62yx')
                         if 'all' not in r.get_attribute('src')]
            reaction_lst = []

            for i in range(len(reaction_users)):
                reaction_lst.append({'reaction_user':reaction_users[i], 'reaction_time':reaction_time[i], 'reaction':reactions[i]})

            comments_reactions.append({'reaction_counts':reaction_counts, 'reactions':reaction_lst})

            close_clk = driver.find_element_by_class_name("c1KbZcP")
            close_clk.click()

        driver.close()

        for i in range(len(comment_autors) - len(comments_reactions)):
            comments_reactions.append({'reaction_counts':0, 'reactions':[]})

        comments = []
        for idx in range(len(comment_autors)):
            comments.append({'comment_id':idx, 'comment_author':comment_autors[idx],
                             'comment_time':post_time[idx], 'comment':comment_text[idx],
                             'reaction_list':comments_reactions[idx]
                             })
        output = {article_id:{'comments':comments}}
        f_name = r'../../output/article'+article_id+'_comment_reaction.txt'
        with open(f_name, 'wt') as out:
            pprint(output, stream=out)

if __name__ == "__main__":
    main()
