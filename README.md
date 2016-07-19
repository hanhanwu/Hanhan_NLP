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



<b>Advanced NLP Tools</b>

-- UW NLP TOOLS
* Reverb  (works well on raw text)
 * About Reverb: https://github.com/hanhanwu/reverb
 * My code using reverb for extraction: https://github.com/hanhanwu/Hanhan_NLP/blob/master/reverb_extraction.py
 * Sample data for my code: https://github.com/hanhanwu/Hanhan_NLP/blob/master/reverb_sample_data.txt
 * How to run my code: 1) Download the latest reverb .jar file 2) open your terminal, cd to the folder where you have your text data input and reverb .jar file 3) run this command in your terminal `java -Xmx512m -jar reverb-latest.jar [input file name] > [output file name]` 4) The run my Python code, `r_pre` is the file path prefix for data input, `f_path` is the output data path full name
