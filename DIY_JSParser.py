# Get Comments and Reactions from new Globe and Mail HTML
from bs4 import BeautifulSoup
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
        htmlSource = driver.page_source
        clk = driver.find_element_by_css_selector('div.c3qHyJD')
        clk.click()
        reaction_counts = driver.find_elements_by_class_name('c2oytXt')
        for rc in reaction_counts:
            print(rc.text)

if __name__ == "__main__":
    main()
