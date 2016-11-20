#!/bin/sh

echo "Running Globe and Mail scraper"
#scrapy crawl ScrapeNews -o output.json --logfile log.txt

scrapy runspider -a outDir='../output/' -a startYear='2014' -a endYear='2016' -o ../output/output.json ScrapeNews/spiders/my_news_spider.py
echo "Done!"
