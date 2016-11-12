# Hanhan_NLP
NLP research and implementation



<b>RESEARCH PAPERS</b>

* <b>Analysis of Collaborative Writing Processes Using Hidden Markov Models and Semantic Heuristics</b>
* It analysis the PROCESS of collaborative writing and predict writing performance
* Inspiration
 * Maybe I can try HMM in my semantic layer, see what kind of key components will lead to what kind of result
 * It's a good idea to record writing behaviour and do analysis, plus time/duration may be better


* <b>Text - Independent Speaker Identification using Hidden Markov Models</b>
* <b>Hidden Markov Models in Text Recognition</b>
* Python HMM
 * http://scikit-learn.sourceforge.net/stable/modules/hmm.html
 * https://github.com/hanhanwu/hmmlearn/blob/master/examples/plot_hmm_stock_analysis.py
* R HMM
 * https://cran.r-project.org/web/packages/HMM/HMM.pdf

* <b>Author Recognition</b>
* Using style markers: https://github.com/hanhanwu/Hanhan_NLP/blob/master/author%20recognition.pdf


<b>LEARNING RESOURCES</b>
* SFU CMPT-825 NLP, 2008: http://www.cs.sfu.ca/~anoop/courses/CMPT-825-Spring-2008/
* SFU CMPT-825 NLP, 2014: http://anoopsarkar.github.io/nlp-class/syllabus.html
* Deep Leanring Course with NLP: http://cs224d.stanford.edu/syllabus.html
* Deep Learning in NLP & Speech/Audio: https://www.analyticsvidhya.com/blog/2016/08/deep-learning-path/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29


<b>PRACTICE</b>
* Keywords Search for Short Context
  * When the text context is very short, and you cannot build the search engine by simply calculating query terms distance, query terms frequency or query terms position. 
  * In the code here, I am trying different methods to allow better key words search for short context. https://github.com/hanhanwu/Hanhan_NLP/blob/master/short_context_search.py
  * In the code, I have implemented 5 methods to do the search. <b>METHOD 1</b> - calculate the score based on the number of search query tokens in the short context; <b>METHOD 2</b> - calculate the score based on how similar the words in short context to the query tokens; <b>METHOD 3</b> - calculate the score based on query tokens order appeard in the short context; <b>METHOD 4</b> - calculate the score based on the query token totoal min physical distances in the short context; <b>METHOD 5</b> - Adjust the score basde on which output users have chosen. Among these 5 mtthonds, method 1 to 4 can be used together by setting different weights, method 5 can be used in real time learning to make the output more intelligent based on all the users choices
  * By rescaling the score in this method, we will be able to use method 1, 2, 3, 4 together, but don't rescale method 4, because using method 4 has to order method 1 results first, which means method 4 output is cannot simply be normalized with max and min. Just use the unnormalized method 4 results with normalized others is fine here. https://github.com/hanhanwu/Hanhan_NLP/blob/master/rescale_score.py
  * NOTE: If the user input contains plural, stemming the query tokens is better
  * NOTE: However, in many cases, the semmed tokens cannot be found in the text with python, for example "beauty" will be stemmed into "beauti", in these cases, no stemming returns better result. This is especially important in method 4, since it will be ordered by the number of query token existence first, then will be orered by the token distance

* Text Feature Selection Example
 * Python code: text_feature_selection_example.py
 * This is just an example to do feature engineering on text data, which means, besides the individual words we could use as features, we could also generate other features based on the text to help later data analysis work.

* Spam Detection with Akismet
 * Akismet Python examples: http://www.programcreek.com/python/example/56583/akismet.verify_key
 * My code with Akismet for spam detection: https://github.com/hanhanwu/Hanhan_NLP/blob/master/spam_detection_Akismet.py

* Login Spider
 * Crawl web pages that need login: https://github.com/hanhanwu/Hanhan_NLP/blob/master/basic_authentication_spider.py
 * When running the code with Scrapy, use terminal command. cd to the top folder of your project, then type `scrapy runspider [spider file path]/[spider file name].py`
 * NOTE: this method does not work for all the web pages that needs login...
 
* Looking for Alternatives for Google Search API
 * Google search API sets limitations per day, only could get 32 search reuslts each day
 * xgoogle, it has a pretty good tutorial, but google has blocked it, since Google doesn't allow automated search... http://www.catonmat.net/blog/python-library-for-google-search/
 * Yahoo YQL Guide: https://developer.yahoo.com/yql/guide/usage_info_limits.html
 * Yahoo Dev Center, to get the key and secret for YQL boss.search: https://developer.yahoo.com/apps/
 * yql open tables: https://github.com/hanhanwu/yql-tables
 * yql health checker, to check the current situations of yql open tables (I really like this feature, when you are clicking the tables here, it leads to YQL Console to allow you run the test query immediately): https://www.datatables.org/healthchecker/
 * <b>Example</b>, yql with Bing Web Search: https://developer.yahoo.com/yql/console/?env=store://datatables.org/alltableswithkeys&q=SELECT+*+FROM+microsoft.bing.web+WHERE+query%3D%27stackoverflow%27#h=SELECT+*+FROM+microsoft.bing.web+WHERE+query%3D'stackoverflow'
 * But, yql always returns empty results for my queries....
 
 * Bing APIs: https://www.microsoft.com/cognitive-services/en-us/bing-web-search-api/documentation
 * Bing Search API Guide: https://msdn.microsoft.com/en-us/library/dn760781.aspx
 * In order to use Bing Search API, need to get the subscription key here: https://www.microsoft.com/cognitive-services/en-us/subscriptions
 * API Test Console: https://dev.cognitive.microsoft.com/docs/services/56b43eeccf5ff8098cef3807/operations/56b4447dcf5ff8098cef380d/console
 * Python Bing Search (it seems that the api key here should be got form Azure Market Place....): https://github.com/hanhanwu/py-bing-search
 

* How to improve search accuracy with Google Search
 * Simple video explains how google search works: https://www.youtube.com/watch?v=KyCYyoGusqs


<b>Advanced NLP Tools</b>

-- UW NLP TOOLS
* Reverb  (works well on raw text)
 * About Reverb: https://github.com/hanhanwu/reverb
 * My code using reverb for extraction: https://github.com/hanhanwu/Hanhan_NLP/blob/master/reverb_extraction.py
 * Sample data for my code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/reverb_sample_data.txt
 * How to run my code: 1) Download the latest reverb .jar file 2) open your terminal, cd to the folder where you have your text data input and reverb .jar file 3) run this command in your terminal `java -Xmx512m -jar reverb-latest.jar [input file name] > [output file name]` 4) The run my Python code, in the python code, `r_pre` is the file path prefix for data input, `f_path` is the output data path full name

* Ollie (works better than Reverb for longer/more complex raw text)
 * About Ollie: https://github.com/hanhanwu/ollie
 * Sample text data: https://github.com/hanhanwu/Hanhan_NLP/blob/master/ollie_sample_data.txt
 * Ollie extracted results: https://github.com/hanhanwu/Hanhan_NLP/blob/master/ollie_extracted_output.txt
 * Check Ollie Quick Start to run do the extraction, if you want to extract the results into a file, run command line `java -Xmx512m -jar ollie-app-latest.jar ollie_sample_data.txt >> extracted_ollie_sample_data.txt`, and remember to `cd` to the folder that include both latest Ollie .jar and engmalt.linear-1.7.mco
 * Ollie really did a good job in my example, in this sample text example, there must be grammer mistake and each sentence is very long. But Ollie could find large amount of relational noun. I am also surprised by its N-ary extractions, some of them could extract those parallized phrases accurately. Check my ollie_extracted_output.txt, you will find the examples

* Open Source Statistical Machine Translation: http://www.statmt.org/

* SFU Parser: https://github.com/sfu-natlang/glm-parser

* Python Scrapy Web Crawler
 * Scrapy General: https://github.com/scrapy/scrapy
 * Scrapy documents: https://doc.scrapy.org/en/latest/
 * Pyhton yield: http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
 
* Stanford Named Entity Recognizer (NER)
 * NER is able to regognize names of different things/people in English words
 * Download NER package: http://nlp.stanford.edu/software/CRF-NER.shtml#Download
 * My code to extract people names with NER: https://github.com/hanhanwu/Hanhan_NLP/blob/master/extract_people_names.py

* nltk Sentiment Analysis
 * NLTK Sentiment Analysis: http://www.nltk.org/howto/sentiment.html
 * Download Vader .zip file here: https://github.com/hanhanwu/vaderSentiment
 * After downloading Vader, import all the 3 files in vaderSentiment folder to your python SDK, under the same project you are going to do sentiment analysis
 * <b>Python 2.x only</b>
 * My sentiment analysis test code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/nltk_sentiment_analysis_test.py


-- R TEXT MINING PACKAGE
* R text mining basics: 
* Helpful resource - sorting R matrix: https://www.r-bloggers.com/sorting-rows-and-colums-in-a-matrix-with-some-music-and-some-magic/
* More about LDA with Python code (still for beginners): https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29


-- My NLP Presentation
* 2016/8/24: https://github.com/hanhanwu/Hanhan_NLP/blob/master/Hanhan_NLP_Presentation.pdf


<b>INSPIRING, when I think NLP is very boring</b>
* IBM Watson competes in Jeopardy: https://www.youtube.com/watch?v=lI-M7O_bRNg
