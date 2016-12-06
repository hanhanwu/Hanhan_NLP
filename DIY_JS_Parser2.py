# Get Comment, Reactions, Reaction Counts
# For each comment url, a browser will be opened and the reaction buttion will be clicked.
# After getting the data, the borwser will be closed.
from selenium import webdriver
import time


def main():
    comment_urls = [
        "http://www.theglobeandmail.com/opinion/a-fascists-win-americas-moral-loss/article32753320/comments/"
                   ]

    for comment_url in comment_urls:
        driver = webdriver.Firefox()
        driver.get(comment_url)
        time.sleep(5)
        # htmlSource = driver.page_source

        comment_autors = driver.find_elements_by_class_name("c29cjTJ")
        post_time = driver.find_elements_by_class_name("cNCPihY")
        comments = driver.find_elements_by_class_name("c1bE414")


        for ca in comment_autors:
            print(ca.text)

        for pt in post_time:
            print(pt.text)

        for cmt in comments:
            print("####", cmt.text, "####")
        print()


        clks= driver.find_elements_by_css_selector('div.c3qHyJD')
        for clk in clks:
            clk.click()
            print("### click ###")

            reaction_counts = driver.find_elements_by_class_name('c2oytXt')
            reaction_users = driver.find_elements_by_class_name('c3TwkwL')
            reaction_time = driver.find_elements_by_class_name('c_0Qpsz')
            reactions = driver.find_elements_by_class_name('c3S62yx')

            for rc in reaction_counts:
                print(rc.text)

            for ru in reaction_users:
                print(ru.text)

            for rt in reaction_time:
                print(rt.text)

            for r in reactions:
                print(r.get_attribute('src'))

            close_clk = driver.find_element_by_css_selector('div.c1KbZcP')
            close_clk.click()

        driver.close()

if __name__ == "__main__":
    main()
