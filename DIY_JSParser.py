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
        soup = BeautifulSoup(htmlSource, 'html.parser')
        authors = [p.find('span').get_text() for p in soup.findAll('p', {'class':'c29cjTJ'})]
        print(authors)

if __name__ == "__main__":
    main()
