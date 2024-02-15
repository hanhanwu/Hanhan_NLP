The code here was written in Python 3.52.

In this example, Scrapy crawls the urls from 1 single url, and I just chose 1 of these crawled urls, extract article data and commnets data for this single article, and insert the output into article output and comment output, seperately.


* In your Python coding IDE (I use PyCharm), create a new project, in my case I named it as <b>HanhanScrapt</b>.
 * `scrapy startproject HanhanScrapt` will create folder "HanhanScrapt" and all the needed coding files for Scrapy.
* Under folder `HanhanScrapt`, I created these folders: `output` and `resources` to store output and input. Also renamed subfolder "HanhanScrapt" as `source` to store source code.
* After several tests, I have realized Scrapy Pipeline will be executed after running the spider.
* All the `yield` items [in spider][1] will be sent to the [pipeline's][2] function `process_item()`.
* Make sure to specify the pipeline in [settings.py][3]
* Open your Python Terminal, `cd` to `HanhanScrapt/source/`, then execute this command: `sh run_news_scraper.sh`


[1]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/HanhanScrapt/source/ScrapeNews/spiders/my_news_spider.py
[2]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/HanhanScrapt/source/ScrapeNews/my_pipelines.py#L12
[3]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/HanhanScrapt/source/ScrapeNews/settings.py#L66-L68

