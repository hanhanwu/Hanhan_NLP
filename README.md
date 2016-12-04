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
 * pygoogle is no longer available either, it recommends to use Google Custom Search
 * Yahoo YQL Guide: https://developer.yahoo.com/yql/guide/usage_info_limits.html
 * Yahoo Dev Center, to get the key and secret for YQL boss.search: https://developer.yahoo.com/apps/
 * yql open tables: https://github.com/hanhanwu/yql-tables
 * yql health checker, to check the current situations of yql open tables (I really like this feature, when you are clicking the tables here, it leads to YQL Console to allow you run the test query immediately): https://www.datatables.org/healthchecker/
 * <b>Example</b>, yql with Bing Web Search: https://developer.yahoo.com/yql/console/?env=store://datatables.org/alltableswithkeys&q=SELECT+*+FROM+microsoft.bing.web+WHERE+query%3D%27stackoverflow%27#h=SELECT+*+FROM+microsoft.bing.web+WHERE+query%3D'stackoverflow'
 * But, yql always returns empty results for my queries....
 
 * Bing APIs: https://www.microsoft.com/cognitive-services/en-us/bing-web-search-api/documentation
 * Bing Search API Guide: https://msdn.microsoft.com/en-us/library/dn760781.aspx
 * In order to use Bing Search API, need to get the subscription key here: https://www.microsoft.com/cognitive-services/en-us/subscriptions
 * Bing Search API Parameters (cannot compete with Google...): https://dev.cognitive.microsoft.com/docs/services/56b43eeccf5ff8098cef3807/operations/56b4447dcf5ff8098cef380d
 * Bing API Test Console: https://dev.cognitive.microsoft.com/docs/services/56b43eeccf5ff8098cef3807/operations/56b4447dcf5ff8098cef380d/console
 * Python Bing Search (it seems that the api key here should be got form Azure Market Place....): https://github.com/hanhanwu/py-bing-search
 * When I was using Python Bing Search, it was showing the authorization method is not valid, I guess this maybe the reason:
 https://datamarket.azure.com/dataset/bing/search
 * It changes v2 to v5, and in order to get all those info, I need to purchase in Azure Market Place: https://msdn.microsoft.com/en-US/library/mt707570.aspx
 * Bing Web Search API Pricing: https://www.microsoft.com/cognitive-services/en-us/bing-web-search-api
 

* How to improve search accuracy with Google Search
 * Simple video explains how google search works: https://www.youtube.com/watch?v=KyCYyoGusqs
 * Operators used in google search query, looks helpful: https://support.google.com/websearch/answer/2466433?visit_id=1-636146162684675642-3633116773&rd=1
 
 
* Google Custom Search Engine (CSE)
 * It's super easy and super cool! If you want to custom your own search engine, on your website
 * The tutorial provides all the useful and educational urls: https://developers.google.com/custom-search/docs/topical
 * The control panel is easy and fast to use, you can generate customized search engine within seconds, and google will create a web version as well as html code and tell you how to copy the code to html page: https://cse.google.com/cse/all
 * My CSE test html code, I just opened JSBin console, opened a HTML template and copy the generate code between <body></body>: https://github.com/hanhanwu/Hanhan_NLP/blob/master/google_cse_sample.html
 * If you need the search results obey a certain url pattern, check google search query operator, very helpful!: https://support.google.com/websearch/answer/2466433?visit_id=1-636146162684675642-3633116773&rd=1
 * Now I want to get the search results from pyhton code, it also simple. This is the detail tutorials about where to get your cx (Custom Search Engine id), key (API Key): https://developers.google.com/custom-search/json-api/v1/reference/cse/list
 * In order to get cx, you need to visit this website: https://cse.google.com/cse/all
 * Create a Custom Search Engine, it's very fast! Once you have created one, you will find cx=.... through the url in your browser
 * In order to get Google API Key, you need to go to Google Dev Center: https://console.developers.google.com/apis/dashboard
 * In Google Dev Center, first click Dashboard, then Click 'ENABLE API' and enable 'Custom Search API'. Next, click 'Credentials', and click 'Create Credential' to create an API Key
 * Pricing if you want to have more search requests: https://developers.google.com/custom-search/json-api/v1/overview#key
 * My sample code about how to get the results through python, with FREE version: https://github.com/hanhanwu/Hanhan_NLP/blob/master/google_cse_sample_python_call.py
 * Google CSE is great, cheaper than many other web search apis, even cheaper than Google Search API, and it's well documented. One thing need to note that google CSE didn't mention is their limitations per second. Bing Search API has 5 query limitation per second. I guess Google CSE also has limitation, therefore only using for loop to execute multiple queries will get errors. You can simply add `time.sleep(1)` in your for loop. Check my code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/multiple_query_google_cse.py
 

* Gigya Javascript Web Parser
 * One year ago, Amazon Camel-Camel-Camel suddenly changed its website source code and everything parsable has become Javascript, therefore I lost many data, and thought Javascript written website may not be parsable. Today, I just tried the Gigya API (the researchers I'm working with may have paid this API...), it will return all the content hidden behind the Javascript code!
 * How does this work: http://developers.gigya.com/display/GD/Developer%27s+Guide
 * Parameters: http://developers.gigya.com/display/GD/comments.getComments+JS
 * One thing about the parameters, some website has hundreds or even thoughds of comments, but you need to click a button such as "More Comments" to see more comments, and the url has never changed. When you are using Gigya API, gave to set parameter "threadLimit", otherwise it cannot return all the comments.


* DIY JavaScript Parser
 * In above you will find Gigya works well to get the content from JS written website, however it doesn't work all the time. Recently, I just met a problem, that when Globe and Mail is updating their website, all the old comments have been hidden from the view, only new comments posted after Nov. 28, 2016 will appear with added new features. However, by using Gigya, I could get all the old comments, but no new comments, no new feature in the output data as well. After 2 days experiments, finally I somewhat realized why this happened, and at least I have found the basic solution to get the content data of this JS written website.
 * My code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/DIY_JSParser.py
 * JS written website is not impossible for parsing without other API, we cannot see content from the source code, but we should be able to get the HTML content from the JS page.
 * <b> First of all</b>, install <b>Firebug!</b>(the name is really cool!) on your Firefox, it's an Addon. With Firebug, when you open the url in Firefox, click `HTML` in Firebug, you will see all the content. With Firebug search function, it's easy to locate and find the tags of the content you want to parse. Then, write code similar to mine, we can get the content.
 * <b>But</b>, so far my method is not perfect. If you check the sample url in my code from your broswer, and you want to see reactions count for each comment, you have click the reaction image, when there is a popup window appear, Firebug HTML will show the counts, otherwise, you cannot find them in the HTML. This means, when you are trying to do auto parsing, getting these counts may not be possible. I'm still trying to see whether this is possible.



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
 
* Python Scrapy Pipeline
 * The Scrapy Pipeline aims to let you execute a series activities through a pipeline of process
 * If you check Scrapy Pipeline document here, it's difficult to really get thing done: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
 * Here is my detailed readme about what did I try and worked: https://github.com/hanhanwu/Hanhan_NLP/blob/master/HanhanScrapt/Hanhan_Scrapy_Pipeline_ReadMe.md
 * All my Scrapy Pipeline code: https://github.com/hanhanwu/Hanhan_NLP/tree/master/HanhanScrapt
 
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

* Crowd Sourcing for Sentiment Analysis
 * CrowdFlower: https://www.crowdflower.com/use-case/sentiment-analysis/


-- R TEXT MINING PACKAGE
* R text mining basics: 
* Helpful resource - sorting R matrix: https://www.r-bloggers.com/sorting-rows-and-colums-in-a-matrix-with-some-music-and-some-magic/
* More about LDA with Python code (still for beginners): https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29


-- My NLP Presentation
* 2016/8/24: https://github.com/hanhanwu/Hanhan_NLP/blob/master/Hanhan_NLP_Presentation.pdf


<b>INSPIRING, when I think NLP is very boring</b>
* IBM Watson competes in Jeopardy: https://www.youtube.com/watch?v=lI-M7O_bRNg
