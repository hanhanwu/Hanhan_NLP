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

* <b> Author Recognition</b>
* Using style markers: https://github.com/hanhanwu/Hanhan_NLP/blob/master/author%20recognition.pdf


<b>LEARNING RESOURCES</b>
* SFU CMPT-825 NLP, 2008: http://www.cs.sfu.ca/~anoop/courses/CMPT-825-Spring-2008/
* SFU CMPT-825 NLP, 2014: http://anoopsarkar.github.io/nlp-class/syllabus.html
* Deep Learning in NLP & Speech/Audio: https://www.analyticsvidhya.com/blog/2016/08/deep-learning-path/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29


<b>PRACTICE</b>
* When the text context is very short, and you cannot build the search engine by simply calculating query terms distance, query terms frequency or query terms position. 
* In the code here, I am trying different methods to allow better key words search. https://github.com/hanhanwu/Hanhan_NLP/blob/master/short_context_search.py


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


-- R TEXT MINING PACKAGE
* R text mining basics: 
* Helpful resource - sorting R matrix: https://www.r-bloggers.com/sorting-rows-and-colums-in-a-matrix-with-some-music-and-some-magic/
* More about LDA with Python code (still for beginners): https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29


-- My NLP Presentation
* 2016/8/24: https://github.com/hanhanwu/Hanhan_NLP/blob/master/Hanhan_NLP_Presentation.pdf


<b>INSPIRING, when I think NLP is very boring</b>
* IBM Watson competes in Jeopardy: https://www.youtube.com/watch?v=lI-M7O_bRNg
