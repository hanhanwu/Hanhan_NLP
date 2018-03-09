# Hanhan_NLP
NLP research and implementation

*********************************************************************************************

<b>Somethig About NLP</b>

* Computational Linguistics Basics: https://www.analyticsvidhya.com/blog/2017/12/introduction-computational-linguistics-dependency-trees/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
  * Dependency trees
  * Stanford Dependencies Manual: https://nlp.stanford.edu/software/dependencies_manual.pdf
  * Coreference Resolution or Anaphora Resolution
    * Identify all the expressions that refer to the same entity

* Basic TOP k NLP Operations
  * Stemming
    * Shorten the words. 
    * Such as "beautiful" and "beautifully" are stemmed to "beauti"
  * Lemmatisation
    * Reduce words into their lemma/dictionary form. 
    * Such as "good", "better" and "best" are lemmatised to "good"
  * Words Inflection
    * Looks like the opposite operation of Lemmatisation/Stemming
    * It adds the characters to a word base format, so that we get more formats, such as singular or plural
  * Words Embedding
    * A word or a phase is represented in a fixed dimensional vector of length X
  * Part-of-Speech Tagging
    * Tag word type (such as Noun, Verb, Adj. etc.) fo each word in the text
  * Named Entity Disambiguation
    * Try to link the entity in the text with knowledge
    * such as, "Apple has best phone", machine needs to figure out "Apple" is a company or fruit or something else
  * Named Entity Recognition
    * Give the entity a category
    * Such as Location, Person, Date, Organization
  * Sentiment Analysis
  * Semantic Text Similarity
    * Semantic Text Similarity is the process of analysing similarity between two pieces of text with respect to the <b>meaning and essence</b> of the text rather than analysing the syntax of the two pieces of text
  * Text Summarisation
    * Identify important points to form a summary
    * The goal of Text Summarisation is to retain maximum information along with maximum shortening of text without altering the meaning of the text.
  * refernece: https://www.analyticsvidhya.com/blog/2017/10/essential-nlp-guide-data-scientists-top-10-nlp-tasks/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
    * It has Python code for implementation of each task
    * Also has relavant papers, application
  * My code: https://github.com/hanhanwu/Basic_But_Useful/blob/master/NLP_basic_preprocessing.ipynb
    * It has more
    * Major libraries you can try for NLP tasks
      * nltk - very basic
      * Spacy
      * Standard core NLP
      * gensim - topic modeling
  * My code2: https://github.com/hanhanwu/Hanhan_NLP/blob/master/NLP_textblob.ipynb
    * It is using an NLP library - TextBlob, which is build upon nltk
    * TextBlob makes calling nltk functions easier, but the functions are very basic. Spacy is fasteer and may provides more NLP data manipulation functions; classifiers are also basic
    * However, <b>I like the Language Translation in TextBlob</b>. It's built upon Google Translate, you don't need to download any language package, and it can do the translation, looks not bad
    * Sentiment Analysis tells not only positive & negative, but also trying to tell how subjective a statement is. 
      * Language codes supported: https://cloud.google.com/translate/docs/languages
    * TextBlob document: http://textblob.readthedocs.io/en/dev/
    * reference: https://www.analyticsvidhya.com/blog/2018/02/natural-language-processing-for-beginners-using-textblob/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29


*********************************************************************************************

<b>PRACTICE</b>

* When dealing with special characters in text, ASCII and Binary Characteristics: http://roubaixinteractive.com/PlayGround/Binary_Conversion/The_Characters.asp

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
 
* Scikit_Learn NLP Go Through
  * Text Matching - Distance Matching, Phonetic Matching, Flexible String Matching, Cosine Similarity 
  * In Distance Matching, besides Levenshtein Distance, there are other distance methods: [Jaro Distance][5], [Hammig Distance][6]
  * For Phonetic Matching, python Fuzzy contains Soundex, DMetaphone and nysiis. It seems that when it comes to similar pronuncation but different spelling, DMetaphone works better. But if you care about both spelling and pronouncation differences, Soundex and nysiis maybe better
  * Flexible String Matching, I will try regular expression, lemmatized matching (StanfordNLP), compact matching (python fuzzyfinder)
  * Cosine Similarity, when the text is represented as vector notation, a general cosine similarity can also be applied in order to measure vectorized similarity. <b>It seems that this method works very well when the words in 2 strings are not in the same order</b>, if we use Levenshtein Distance, it cares about words order and will output larger distance.
  * <b>Coreference Resolution</b> is a process of finding relational links among the words (or phrases) within the sentences. it automatically figures out what does "he", "it" mean in the sentences. [Standford NLP Coreference Resolution][7], [Standford NLP Python][8] 
  * [Reference][9]
  * [my code][10]
 
* R Web Mining
  * Learning Resource: https://www.analyticsvidhya.com/blog/2017/03/beginners-guide-on-web-scraping-in-r-using-rvest-with-hands-on-knowledge/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
  * My R code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/R_web_parsing.R
  * The way I parse the data is totally different from the methods used in learning resources. In the learning resource, they are using class name, and when there are multiple web elements with the same class names, their method may not be able to find the content in order. In my code, I have found that using `XPATH` is much better for this case, and with `Firebug`, you can simply right click to copy the `XPATH` of your web element, write a function to get the content in order

 
[5]:https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
[6]:https://en.wikipedia.org/wiki/Hamming_distance
[7]:http://nlp.stanford.edu/software/dcoref.shtml
[8]:https://github.com/Wordseer/stanford-corenlp-python
[9]:https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
[10]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/NLP%20with%20Scikit%20Learn.ipynb

 
*********************************************************************************************

<b>RESAERCH AND DEVELOPMENT</b>

* How to improve search accuracy with Google Search
  * Simple video explains how google search works: https://www.youtube.com/watch?v=KyCYyoGusqs
  * Operators used in google search query, looks helpful: https://support.google.com/websearch/answer/2466433?visit_id=1-636146162684675642-3633116773&rd=1
  
  
* <b>Word Embedding Methods</b>
  * Reference: https://www.analyticsvidhya.com/blog/2017/06/word-embeddings-count-word2veec/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
  * Frequency based Embedding
    * Count Vectors
      * Imagine you have a table, each column is a unique word, each row is a document
      * In a corpus, unique words are top couted words, otherwise that's too much
      * For the same document, the word count for each word - Document Vector
      * For the same word, its count in each document - Word Vector
    * TF-IDF
      * It checks not only how many times a word appears in one document, but also checks the time it appears in the whole corpus. And it will penalize those common words which appeared in large number of documents, in this way, it is more likely to find real important words for a subset of documents
      * `TF = the number of time word t appears in 1 document`
      * `IDF = log(N/n)`, N is the number of documents, n is the number of documents that t appeared. In this way, when n is large, IDF tend to get closer to 0, and therefore those stop words will get low score (`TF * IDF`)
    * Co-Occurrence Matrix & Context Window
      * With context window, it defines the number of words together, and even a direction. For example, 2 words together
      * Co-occurance will be the count of word tuples, the number of words ina tuple is defined by context window. For example, count the co-occurance of (ice, cream)
      * Co-occurrence matrix can be huge even remove stop words. It uses algorithms such as PCA to decompose.
        * If you perform PCA on a V*V matrix, you get V principle components. Choose k components out of V, you get a new matrix of V*k
        * It preserves semantic relationships between words. For example "ice" and "cream" is closer than "ice" and "human"
        * You just compute it once and can use multiple times, so it's fast
  * Prediction based Embedding (methods here need you manually create lables)
    * Word2Vector = CBOW (Continuous bag of Words) + Skip-Gram
      * CBOW: 
        * Probabilistic, better than deterministic. 
        * Lower memory requirement
        * It's neural network and the hidden layer taks advantage of the context
    * Skip-Gram
      * It's also neural network, it predicts context given a word
    * A visualization tool: https://docs.google.com/document/d/1qUH1LvNcp5msoh2FEwTQAUX8KfMq2faGpNv4s4WXhgg/pub


<b>Auto Search APIs</b>

* Google search API sets limitations per day, only could get 32 search reuslts each day
* <b>xgoogle</b>, it has a pretty good tutorial, but google has blocked it, since Google doesn't allow automated search... http://www.catonmat.net/blog/python-library-for-google-search/
* <b>pygoogle</b> is no longer available either, it recommends to use Google Custom Search
* <b>YQL</b>
  * Yahoo YQL Guide: https://developer.yahoo.com/yql/guide/usage_info_limits.html
  * Yahoo Dev Center, to get the key and secret for YQL boss.search: https://developer.yahoo.com/apps/
  * yql open tables: https://github.com/hanhanwu/yql-tables
  * yql health checker, to check the current situations of yql open tables (I really like this feature, when you are clicking the tables here, it leads to YQL Console to allow you run the test query immediately): https://www.datatables.org/healthchecker/
  * <b>Example</b>, yql with Bing Web Search: https://developer.yahoo.com/yql/console/?env=store://datatables.org/alltableswithkeys&q=SELECT+*+FROM+microsoft.bing.web+WHERE+query%3D%27stackoverflow%27#h=SELECT+*+FROM+microsoft.bing.web+WHERE+query%3D'stackoverflow'
  * But, yql always returns empty results for my queries....
* <b>Bing</b>
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
* <b>Google Custom Search Engine (CSE)</b>
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
  * About the pricing, one thing is a little weird, if you are using $5 per 1000 query based on the free version, it will prevent you from calling more queries each day when you haven't reached to 10k queirs. Maybe this is because I'm not the one who paid the price and cannot see the settings...
  * My sample code about how to get the results through python, with FREE version: https://github.com/hanhanwu/Hanhan_NLP/blob/master/google_cse_sample_python_call.py
  * Google CSE is great, cheaper than many other web search apis, even cheaper than Google Search API, and it's well documented. One thing need to note that google CSE didn't mention is their limitations per second. Bing Search API has 5 query limitation per second. I guess Google CSE also has limitation, therefore only using for loop to execute multiple queries will get errors. You can simply add `time.sleep(1)` in your for loop. Check my code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/multiple_query_google_cse.py
 

<b>Java Script Parser</b>

* <b>Gigya Javascript Web Parser</b>
  * One year ago, Amazon Camel-Camel-Camel suddenly changed its website source code and everything parsable has become Javascript, therefore I lost many data, and thought Javascript written website may not be parsable. Today, I just tried the Gigya API (the researchers I'm working with may have paid this API...), it will return all the content hidden behind the Javascript code!
  * How does this work: http://developers.gigya.com/display/GD/Developer%27s+Guide
  * Parameters: http://developers.gigya.com/display/GD/comments.getComments+JS
  * One thing about the parameters, some website has hundreds or even thoughds of comments, but you need to click a button such as "More Comments" to see more comments, and the url has never changed. When you are using Gigya API, gave to set parameter "threadLimit", otherwise it cannot return all the comments.
* <b>DIY JavaScript Parser - with selenium</b>
  * In above you will find Gigya works well to get the content from JS written website, however it doesn't work all the time. Recently, I just met a problem, that when Globe and Mail is updating their website, all the old comments have been hidden from the view, only new comments posted after Nov. 28, 2016 will appear with added new features. However, by using Gigya, I could get all the old comments, but no new comments, no new feature in the output data as well. After 2 days experiments, finally I somewhat realized why this happened, and at least I have found the basic solution to get the content data of this JS written website.
  * <b>My code 1</b>: https://github.com/hanhanwu/Hanhan_NLP/blob/master/DIY_JSParser.py
  * JS written website is not impossible for parsing without other API, we cannot see content from the source code, but we should be able to get the HTML content from the JS page.
  * <b> First of all</b>, install <b>Firebug!</b>(the name is really cool!) on your Firefox, it's an Addon. With Firebug, when you open the url in Firefox, click `HTML` in Firebug, you will see all the content. With Firebug search function, it's easy to locate and find the tags of the content you want to parse. Then, write code similar to mine, we can get the content.
  * <b>Then</b>, as you can see, in my code, I am using selenium library, it's super cool. It can get HTML page from JS written website, add, with `click()` method, you can click the chosen element. This is very imortant is because some elements such as reactions counts in my sample url will not appear until you click each reaction image.
  * selenium elements locating: http://selenium-python.readthedocs.io/locating-elements.html
  * NOTE: selenium has get_element_* and get_elements_*, pay attention to this detail.
  * <b>My code 2</b>: https://github.com/hanhanwu/Hanhan_NLP/blob/master/DIY_JS_Parser2.py
  * In my part 2 code, I was dealing with multiple clickable elements that have the same class name. When you clicked one, without closing it or scroll down, you cannot click another one. In this code, the code closed each popup, before clicking the next one.
  * Also in my code 2, I'm using this method `driver.execute_script("arguments[0].scrollIntoView();", clk)`, each time you need to interact with the next element, it will move to that position first. Otherwise you will get an error for not be able to see that (x,y) point, even if you maximize the browser.
  * <b>Getting parents web element</b>: https://github.com/hanhanwu/Hanhan_NLP/blob/master/DIY_JS_Parser_get_parents.py
  * <b>My code 3</b>: https://github.com/hanhanwu/Hanhan_NLP/blob/master/DIY_JS_Parser3.py
  * My code 3 has finished a complex process, that is to extract hierarchical data and recover them back to the original hierarchial structure. If you copy the url to firefox and have firebug on it, you will find for each main comment author, the class name is "c29cjTJ", the replied author of each main comment has class name "c29cjTJ c3fk6Wf". In fact "c29cjTJ c3fk6Wf" is a compact class, you cannot find the element through this class name, but you can find the element through `driver.find_element_by_css_selector(".c29cjTJ.c3fk6Wf")`. However, there is a even simpler way, that is what I wrote in my code 3, you use `driver.find_element_by_class_name("c29cjTJ")`, it will include all the authors for main comment and replies. Later, just try to trace back to find the root class id to decide which reply belongs to which main comment.
  * NOTE: In some machines, it may require `geckodriver`, and sometimes, adding its path into $PATH doesn't work, so in your code, instead of using `driver = webdriver.Firefox()`, you should use `driver = webdriver.Firefox(executable_path='[your path]/geckodriver')`
  * <b>My code 4</b>: https://github.com/hanhanwu/Hanhan_NLP/blob/master/DIY_JS_Parser4.py
  * I thought my code 3 was good, no it's not. When I found there was a "Show More Comments" button at the bottom, and tried to expand all the comments, I have found that the expanded comments had no HTML location id, which was the ids I used to map comment authors, post time text, reactions and replies together. I tried some methods, hoping to adding something on my code 3 to solve the problem, but only made things more complex. Maybe, sometimes when the problem becomes more complex, the solution will in fact become easier. I redisigned the code, and just found that, instead of using driver to get all the web elements, I could use a web elements to locate its children, which makes my mapping much easier. Although the website have some inconsistent display, I put many "try... except" in the code, at least for nnow, there is no error. Here are the test urls: https://github.com/hanhanwu/Hanhan_NLP/blob/master/test_urls.txt
  * Note: in my code 4, I am using `driver.quit()`, instead of `driver.close()`, this is because in some machine, `driver.close()` does not work, this may be a bug in selenium, here is the discussion: https://github.com/seleniumhq/selenium/issues/654


<b>How to get NationalPost Comments</b>

* Sample url "http://news.nationalpost.com/full-comment/marni-soupcoff-bob-dylans-nobel-silence-is-golden"
* I need to get the comments and I don't want to use its HTML data, looks simple, but no. Because this website embed everything in WordPress, however, traditional APIs cannot get the right comments data.
* <b>Gigya</b> got empty comments
* <b>WordPress API</b>: https://developer.wordpress.com/docs/api/
  * WordPress API console: https://developer.wordpress.com/docs/api/console/
  * But for each NationalPost article, both WordPress post and comment all point to the article, and the `$site` has to be the domain. `https://public-api.wordpress.com/rest/v1/sites/news.nationalpost.com/comments/307452/`, `https://public-api.wordpress.com/rest/v1/sites/news.nationalpost.com/posts/1282447/replies`, others could not help either.
* <b>PostMedia open source</b> is not useful either: https://github.com/Postmedia
* <b>Python Twill</b>: Python Twill does not work well for JavaScript. http://twill.idyll.org/,  http://twill.idyll.org/python-api.html
* <b>Zombie</b>: I tried Zombie first because it's browserless, which means when it is parsing the data, there is no browser popup. First of all, its Python API does not work for external url not built by me. So I had to try Zombie.js, it finally only returned me those only in web source code, still cannot get comments data. But a good learning experience.
  * Zombie CoffeeScript Stackoverflow reference: http://stackoverflow.com/questions/11628636/i-cant-get-the-whole-source-code-of-an-html-page
  * In order to use Zombie.js, I have checked: how to use node.js: http://www.dannemanne.com/posts/tutorial_get_started_with_node_js_on_mac_beginner_
  * In order to use Zombie.js, I have checked: coffeescript - TRY COFFEESCRIPT: http://coffeescript.org/
  * In order to use Zombie.js, I have checked: zombie.js: http://zombie.js.org/
  * In order to use Zombie.js, I have checked: zombie functions: http://zombie.readthedocs.io/en/latest/pythonzombie.html
  * In order to use Zombie.js, I have checked: CSS selector string: http://www.w3schools.com/jsref/met_document_queryselector.asp
* <b>Mechanize</b>: It is built on python urllib2, therefore it cannot get the comments data which is not showing in web source code... But it is very convenient to get article title. http://wwwsearch.sourceforge.net/mechanize/
* <b>Selenium</b>: Finally I got the comments by using selenium and firebug. They were my last choice because of the popup browsers, but, I have to admit, they are good to use.
  * My code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/get_national_post_comments.py
  * In my code, I have learned that, when using XPath, `//iframe[@class='fb_ltr']` means this element ins directly under the root, if not, use `.//iframe[@class='fb_ltr']`
 
 
<b>Python Scrapy</b>
 
* Scrapy Web Crawler
  * Scrapy General: https://github.com/scrapy/scrapy
  * Scrapy documents: https://doc.scrapy.org/en/latest/
  * Pyhton yield: http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
* Scrapy Pipeline
  * The Scrapy Pipeline aims to let you execute a series activities through a pipeline of process
  * If you check Scrapy Pipeline document here, it's difficult to really get thing done: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
  * Here is my detailed readme about what did I try and worked: https://github.com/hanhanwu/Hanhan_NLP/blob/master/HanhanScrapt/Hanhan_Scrapy_Pipeline_ReadMe.md
  * All my Scrapy Pipeline code: https://github.com/hanhanwu/Hanhan_NLP/tree/master/HanhanScrapt
* Other Scrapy Resources
  * Web Scrapign: https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
    * Extract web elements such as images, text, votes, etc. with Scrapy Spider
    * Based on my experience, Scrapy only works well when the webiste does not use any bot to prevent customized spiders (even if you change Scrapy bot settings). Python selenium often works even when there is bot.
 

<b>Entity Recognizer</b>
 
* Stanford Named Entity Recognizer (NER)
  * NER is able to regognize names of different things/people in English words
  * Download NER package: http://nlp.stanford.edu/software/CRF-NER.shtml#Download
  * My code to extract people names with NER: https://github.com/hanhanwu/Hanhan_NLP/blob/master/extract_people_names.py


<b>Information Retrieval</b>

* It helps find relevant information/documents that can satisfiy readers requirements
* You can use this method in:
  * Search Engine
  * Content Based Image Retrieval
  * Recommendation System
* KNN vs KD Tree
  * KNN takes O(N) time for N data points; KNN with K Neighbour search takes O(log(K)*N). In both cases, when there are large amount of data points, KNN can be time consuming
  * KD Tree is an improvement on KNN, it uses both decision tree and KNN to  calculate nearest neighbours
    * Similar to binary search tree, you build a decision tree by spliting training data based on certain conditions. Now when there is a testing data, it travels from root to the node its condition satisfied with.
    * But locating the node for your testing data doesn't mean data points in that node are the nearest neighbour. You need to check sibling nodes by tracing back to 1 level parent root and gets to sibling nodes each time, compare the nearest distance with current nearest data point
    * This method can help you get rid of subtress and improve the time efficiency
    * Also KD Tree allows you to split and organize data based on certain conditions
    * Average time complexity O(log(N)), worst case O(N) when the data structure and conditions make the tress like a list
    * KDTree may not work well in high dimensions (lots of features). When there are many features, you still need to check many partitions in the tree, won't be very efficient. I would do dimensional reduction first and and try KDTree, and compare with other algorithms
  * My code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/KDTree_Information_Retrieval.ipynb
    * In this code, I'm using KDTree to retrieve text close to 'Emmanuel'! It works well!
  * reference: https://www.analyticsvidhya.com/blog/2017/11/information-retrieval-using-kdtree/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
* Distance Methods used in KNN
  * The paper: https://github.com/hanhanwu/readings/blob/master/knn_distance_algs.pdf
  * There are definitions of 11 distance methods
  * They have compared 8 datasets with 11 distance methods and found:
    * Hamming and Jaccard perform worst since these 2 methods will be affected by the ratio of the members of each class, while other methods won't be affected
    * The top 6 distance methods a they tried in KNN are: City-block, Chebychev, Euclidean, Mahalanobis, Minkowski, Standardized Enuclidean techniques


<b>Sentiment Analysis</b>

* Resources: https://github.com/hanhanwu/Hanhan_NLP/blob/master/Sentiment_Analysis_Resources/resources.md

* nltk Sentiment Analysis
  * NLTK Sentiment Analysis: http://www.nltk.org/howto/sentiment.html
  * Download Vader .zip file here: https://github.com/hanhanwu/vaderSentiment
  * After downloading Vader, import all the 3 files in vaderSentiment folder to your python SDK, under the same project you are going to do sentiment analysis
  * <b>Python 2.x only</b>
  * My nltk sentiment analysis test code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/nltk_sentiment_analysis_test.py

* R Sentiment Analysis
  * Reference - Sentiment analysis on movie and tweet: https://www.analyticsvidhya.com/blog/2017/03/measuring-audience-sentiments-about-movies-using-twitter-and-text-analytics/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
    * This tutorial is worthy to try is because of the `NRC sentiment dictionary` they use. In R, if you use `library syuzhet` you can use the sentiment dictionary. It has multiple sentiment levels: <b>"Positive","Anger","Anticipation","Disgust","Fear","Joy","Sadness","Surprise","Trust","Negative"</b>
    * <b>My code</b>: https://github.com/hanhanwu/Hanhan_NLP/blob/master/tweets_sentiment_analysis.R
    * My code includes Tweet data collection, sentiment analysis and visualization
    * Resource about collect tweets through R - How tweet search query works, and tutorial for generating tweets in R: http://bogdanrau.com/blog/collecting-tweets-using-r-and-the-twitter-search-api/
  * Stanford Sentiment Analysis Example: http://stackoverflow.com/questions/32879532/stanford-nlp-for-python
    * In Stanford sentiment analysis, their sentiment levels are: <b>VeryPositive, Positive, Nuetral, Negative, VeryNegative</b>
    
* Python Flash Text - Search, Replace words in text, faster than regex
  * reference: https://www.analyticsvidhya.com/blog/2017/11/flashtext-a-library-faster-than-regular-expressions/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
  * flashtext: https://pypi.python.org/pypi/flashtext/2.2
    * I don't really like that 'remove keywords' feature
  * It's using <b>Trie Data Structure</b> for the words
  * <b>Single Pass vs No Single Pass</b>
    * With single pass, each word replacing will use the origial text/string as input
    * Without single pass, each replace is built based on the last replacing
  * FlashText is faster than regex is because, it checks whether the keyword exists in keyword dictionary, rather than checking the whole text
  * my code: https://github.com/hanhanwu/Basic_But_Useful/blob/master/try_flashtext.ipynb


<b>NLP Tools Research</b>

<b>Feature Extraction, for Clustering Use</b>

* Stanford CoreNLP: http://stanfordnlp.github.io/CoreNLP/

* Spacy
  * https://spacy.io/
  * Spacy GitHub: https://github.com/hanhanwu/spaCy
  * Spack API Reference: https://spacy.io/docs/api/
  * NLP Tutorials: https://spacy.io/docs/usage/tutorials
  * Spacy Workflow: https://spacy.io/docs/usage/language-processing-pipeline
  * My code for basic try spacy: https://github.com/hanhanwu/Hanhan_NLP/blob/master/try_Spacy.ipynb
  * Reference: https://www.analyticsvidhya.com/blog/2017/04/natural-language-processing-made-easy-using-spacy-%E2%80%8Bin-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
    * For the machine learning part in this tutorial, I didn't try, since I think only the pipeline part is special but I don't see any meaning for the author to create `class predictors`. If I have to use pipeline in my personal projects, I'd rather to use Spark + Stanford CoreNLP
 
* Tools built on Spacy (maybe they are even better)
  * Overall: https://spacy.io/docs/usage/showcase
* <b>Textacy</b>
  * Textacy Document: https://media.readthedocs.org/pdf/textacy/latest/textacy.pdf
  * [Text Preprocessing][1]: Their preprocessing choices are very rich, removing emails, remove urls, fix unicode, deal with Egnlish contractions and so on. Meanwhile, if you ues `textacy.preprocess.preprocess_text()`, you can choose which choices to use, very flexible.
  * [Extract][2]: They are using Part-of-speech tagging as Spacy dose. The part-of-speech tagger uses the OntoNotes 5 version of the Penn Treebank tag set. We also map the tags to the simpler Google Universal POS tag set. 
  * [My textacy explore code][3]
 
* NLTK
  * NLP basic operations go through: http://clarkgrubb.com/nlp
 
* Other Methods
  * [Feature Summary with Python][4] (the data preprocessing methods here are too basic, however, it's very interesting to learn there is `tf-isf` and see the way they calculate it. The only pity is, they got Cue Words manually...)

* Methods used in Published Papers
  * Threat Comments Detection (check their features selection): https://www.semanticscholar.org/paper/Threat-detection-in-online-discussions-Wester-%C3%98vrelid/f4150e2fb4d8646ebc2ea84f1a86afa1b593239b
 

<b>Python Gensim</b> - Topic Modeling
* https://github.com/hanhanwu/gensim
 
<b>Pyhthon Pattern</b> - NLP and Machine Learning
* https://github.com/hanhanwu/pattern

<b>Python TextBlob</b> - NLP, built upon NLTK and Pattern
* https://github.com/hanhanwu/TextBlob


*********************************************************************************************

<b>ADVENCED NLP TOOLS/OPEN SOURCE</b>

<b>Format JSON Output</b>, when you don't have notepad++: http://jsonviewer.stack.hu/

<b>Web Annotatio Tools</b>
* WebAnno: https://webanno.github.io/webanno/
  * WebAnno source code, more about web development: https://github.com/webanno/webanno
* Brat: http://brat.nlplab.org/examples.html


<b>UW NLP TOOLS</b>

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

* Crowd Sourcing for Sentiment Analysis
  * CrowdFlower: https://www.crowdflower.com/use-case/sentiment-analysis/

* R/Python TEXT MINING PACKAGE
  * R text mining basics: https://rstudio-pubs-static.s3.amazonaws.com/31867_8236987cf0a8444e962ccd2aec46d9c3.html
  * Helpful resource - sorting R matrix: https://www.r-bloggers.com/sorting-rows-and-colums-in-a-matrix-with-some-music-and-some-magic/
  * More about LDA with Python code (still for beginners): https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
  

* Facebook Research: https://github.com/facebookresearch
  * It includes not only NLP, but also AI
  * FastText: https://github.com/facebookresearch/fastText
    * It can help supervised text classification
    * I didn't try it, sounds fast... But you need to give the label...


* Chat Bot - RASA-NLU
  * RASA-NLU: https://github.com/RasaHQ/rasa_nlu
    * You need to provide the training data yourself
  * How other use RASA-NLU to build chat-bot app: https://www.analyticsvidhya.com/blog/2018/01/faq-chatbots-the-future-of-information-searching/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
    * source code: https://github.com/yogeshhk/gstfaqbot

*********************************************************************************************

<b>My NLP Presentation</b>
* 2016/8/24: https://github.com/hanhanwu/Hanhan_NLP/blob/master/Hanhan_NLP_Presentation.pdf


[1]:https://github.com/chartbeat-labs/textacy/blob/master/textacy/preprocess.py
[2]:https://github.com/chartbeat-labs/textacy/blob/master/textacy/extract.py
[3]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/textacy_explore/go_through_features.py
[4]:https://www.analyticsvidhya.com/blog/2017/01/introduction-to-structuring-customer-complaints/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29


*********************************************************************************************

<b>RESEARCH PAPERS</b>

* <b>Computational Linguistics</b> - MIT Press: http://www.mitpressjournals.org/loi/coli

* <b>SO-CAL in NLP</b>: https://github.com/hanhanwu/Hanhan_NLP/blob/master/Taboada_etal_SO-CAL.pdf

* <b>Analysis of Collaborative Writing Processes Using Hidden Markov Models and Semantic Heuristics</b> - It analysis the PROCESS of collaborative writing and predict writing performance
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
 

*********************************************************************************************

<b>OTHER RESOURCES</b>

* SFU CMPT-825 NLP, 2008: http://www.cs.sfu.ca/~anoop/courses/CMPT-825-Spring-2008/
* SFU CMPT-825 NLP, 2014: http://anoopsarkar.github.io/nlp-class/syllabus.html
* Deep Leanring Course with NLP: http://cs224d.stanford.edu/syllabus.html
* Deep Learning in NLP & Speech/Audio: https://www.analyticsvidhya.com/blog/2016/08/deep-learning-path/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
* Stanford Question Answering Dataset: https://rajpurkar.github.io/SQuAD-explorer/
  * A new about Alibaba and MSR: https://www.analyticsvidhya.com/blog/2018/01/alibabas-neural-network-model-beat-highest-human-score-stanfords-reading-test/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
