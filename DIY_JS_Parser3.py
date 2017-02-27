# put replies under their main comments

# Get Comment, Reactions, Reaction Counts
# For each comment url, a browser will be opened and the reaction buttion will be clicked.
# After getting the data, the borwser will be closed.
from selenium import webdriver
import time
import re
import collections
import json
import unidecode

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
        "http://www.theglobeandmail.com/opinion/dont-set-your-hair-on-fire-it-wont-help/article33683150/comments/"
        # "http://www.theglobeandmail.com/opinion/a-fascists-win-americas-moral-loss/article32753320/comments/",
        # "http://www.theglobeandmail.com/opinion/academic-extremism-comes-to-canada/article33185073/comments/"
                   ]
    article_id_ptn = "http://www.theglobeandmail.com/.*?/article(\d+)/comments"


    for comment_url in comment_urls:
        article_id = re.match(article_id_ptn, comment_url).group(1)
        driver = webdriver.Firefox()
        driver.get(comment_url)
        all_dct = {}
        time.sleep(5)

        # authors
        comment_authors = driver.find_elements_by_class_name("c29cjTJ")
        for comment_author in comment_authors:
            rp = comment_author.find_element_by_xpath('../../../../..')
            p = comment_author.find_element_by_xpath('../../../..')
            rp_class = rp.get_attribute("class")
            rp_id = rp.get_attribute("data-reactid")
            p_class = p.get_attribute("class")
            p_id = p.get_attribute("data-reactid")
            ca_key = "_".join([rp_class, rp_id, p_class, p_id])
            all_dct.setdefault(ca_key, {"author": comment_author.text, "post_time": "", "comment_text":"", "reactions":None})

        # post time
        post_times = driver.find_elements_by_class_name("cNCPihY")
        for post_time in post_times:
            rp = post_time.find_element_by_xpath('../../../../..')
            p = post_time.find_element_by_xpath('../../../..')
            rp_class = rp.get_attribute("class")
            rp_id = rp.get_attribute("data-reactid")
            p_class = p.get_attribute("class")
            p_id = p.get_attribute("data-reactid")
            pt_key = "_".join([rp_class, rp_id, p_class, p_id])
            all_dct[pt_key]["post_time"] = post_time.text

        # comment_text
        comment_text_lst = driver.find_elements_by_class_name("c1bE414")
        for comment_text in comment_text_lst:
            rp = comment_text.find_element_by_xpath('../../../../..')
            p = comment_text.find_element_by_xpath('../../../..')
            rp_class = rp.get_attribute("class")
            rp_id = rp.get_attribute("data-reactid")
            p_class = p.get_attribute("class")
            p_id = p.get_attribute("data-reactid")
            ct_key = "_".join([rp_class, rp_id, p_class, p_id])
            all_dct[ct_key]["comment_text"] = unidecode.unidecode(comment_text.text.replace("\n", "").replace("\"", "'"))

        # click
        clicks= driver.find_elements_by_css_selector('div.c2iexvC')
        for click in clicks:
            rp = click.find_element_by_xpath('../../../../../..')
            p = click.find_element_by_xpath('../../../../..')
            rp_class = rp.get_attribute("class")
            rp_id = rp.get_attribute("data-reactid")
            p_class = p.get_attribute("class")
            p_id = p.get_attribute("data-reactid")
            click_key = "_".join([rp_class, rp_id, p_class, p_id])

            driver.execute_script("arguments[0].scrollIntoView();", click)
            click.click()

            reaction_counts = [rc.text for rc in driver.find_elements_by_class_name('c2oytXt')]
            reaction_users = [ru.text for ru in driver.find_elements_by_class_name('c3TwkwL')]
            reaction_time = [rt.text for rt in driver.find_elements_by_class_name('c_0Qpsz')]
            reactions = [get_reaction(r.get_attribute('src')) for r in driver.find_elements_by_class_name('c3S62yx')
                         if 'all' not in r.get_attribute('src')]
            reaction_lst = []

            for i in range(len(reaction_users)):
                reaction_lst.append({'reaction_user':reaction_users[i], 'reaction_time':reaction_time[i], 'reaction':reactions[i]})

            all_dct[click_key]["reactions"] = collections.OrderedDict({'reaction_counts':reaction_counts, 'reaction_list':reaction_lst})

            close_clk = driver.find_element_by_class_name("c1KbZcP")
            close_clk.click()

        driver.close()

        hierarchical_dct = {}
        for k,v in all_dct.items():
            if "c2LlVA7 c1EuLzy" not in k: # main comment
                hierarchical_dct.setdefault(k.split('_c2LlVA7_')[0], {
                                                                        "author":v['author'],
                                                                        "post_time":v['post_time'],
                                                                        "comment_text":v['comment_text'],
                                                                        "reactions":v['reactions'],
                                                                        "replies":{}
                                                                     })

        for k, v in all_dct.items():
            if "c2LlVA7 c1EuLzy" in k:
                main_comment_key = k.split('_c2LlVA7 c1EuLzy_')[0]
                hierarchical_dct[main_comment_key]['replies'][k] = collections.OrderedDict(v)


        f_name = r'../../output/Comment_Reactions/article_' + article_id + '_comments.json'
        with open(f_name, 'w') as out:
            json.dump(collections.OrderedDict(hierarchical_dct), out)

if __name__ == "__main__":
    main()
