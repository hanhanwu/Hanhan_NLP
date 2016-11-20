import re
from json import loads
from urllib.parse import urlencode
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule



class NewsSpider(CrawlSpider):
    '''
    This class is responsible for crawling globe and mail articles and their comments
    '''
    name = 'ScrapeNews'
    allowed_domains = ["theglobeandmail.com"]

    # List of start urls.
    url_path = r'../resources/test_urls.txt'
    start_urls = [line.strip() for line in open(url_path).readlines()]

    # Rules for including and excluding urls
    rules = (
        Rule(LinkExtractor(allow=r'\/opinion\/.*\/article\d+\/$'), callback="parse_articles"),
    )

    def __init__(self, **kwargs):
        '''
        :param kwargs:
         Read user arguments and initialize variables
        '''
        CrawlSpider.__init__(self)
        self.outDir = kwargs['outDir']
        self.startYear = kwargs['startYear']
        self.endYear = kwargs['endYear']
        print('startYear: ', self.startYear)
        print('self.endYear: ', self.endYear)
        print('self.outDir: ', self.outDir)

        self.headers = ({'User-Agent': 'Mozilla/5.0',
                         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                         'X-Requested-With': 'XMLHttpRequest'})
        self.payload = {'username': '[user name for The Globe and Mail]', 'password': '[password for The Globe and Mail]'}
        self.apikey = '[API Key for Gigya]'
        self.categoryID = 'Production'


    def parse_articles(self, response):
        article_ptn = "http://www.theglobeandmail.com/opinion/(.*?)/article(\d+)/"
        resp_url = response.url
        article_m = re.match(article_ptn, resp_url)
        article_id = ''
        if article_m != None:
            article_id = article_m.group(2)

        if article_id == '32753320':
            print('***URL***', resp_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = Selector(text=response.text).xpath('//*[@id="content"]/div[1]/article/div/div[3]/div[2]').extract()


            if text:
                print("*****in Spider text*****", soup.title.string)
                yield {article_id: {"title": soup.title.string, "link": resp_url, "article_text": text}}
                comments_link = response.url + r'comments/'
                if comments_link == 'http://www.theglobeandmail.com/opinion/a-fascists-win-americas-moral-loss/article32753320/comments/':
                    yield Request(comments_link, callback=self.parse_comments)


    def parse_comments(self, response):
        '''
        :param response:
        :return:
        '''
        print('****COMMENTS URL:**** ', response.url)

        pat = r'''streamId = "(?P<streamid>\d{8})"'''
        session = requests.Session()
        resp = session.get(response.url, headers=self.headers)
        cookies = requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies))
        resp = session.post(response.url, headers=self.headers, data=self.payload, cookies=cookies)
        streamid = ''
        pn = '1234'
        r = requests.get(response.url + '?part_number=' + pn, headers=self.headers, cookies=cookies)
        m = re.search(pat, r.text)
        if m:
            print(m.group('streamid'))
            streamid = m.group('streamid')

        data = {"categoryID": self.categoryID,
                "streamID": streamid,
                "APIKey": self.apikey,
                "callback": "foo",
                "threadLimit": 1
                }
        r = urlopen("http://comments.us1.gigya.com/comments.getComments", data=urlencode(data).encode("utf-8"))
        comments_json = loads(r.read().decode("utf-8"))["comments"]
        yield {"comments": comments_json}


