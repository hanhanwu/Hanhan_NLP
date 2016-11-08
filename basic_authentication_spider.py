# Test Login Spider
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request


login_url = "[your login url]"
user_name = b"[your user id]"
pswd = b"[your passwd]"
response_page = "[response page url]"


class MySpider(scrapy.Spider):
    name = 'myspider'

    def start_requests(self):
        return [scrapy.FormRequest(login_url,
                               formdata={'user': user_name, 'pass': pswd},
                               callback=self.logged_in)]

    def logged_in(self, response):
        # login failed
        if "authentication failed" in response.body_as_unicode():
            print ("Login failed")
        # login succeeded
        else:
            print ('login succeeded')
            return Request(url=response_page,
                   callback=self.parse_responsepage)

    def parse_responsepage(self, response):
        hxs = HtmlXPathSelector(response)
        yum = hxs.select('//span')
        print(yum)


def main():
    test_spider = MySpider(scrapy.Spider)
    test_spider.start_requests()

if __name__ == "__main__":
    main()
