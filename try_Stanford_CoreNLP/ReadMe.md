

*****************************************************************************

RESOURCES

* [Stanford Software][1]
* [Download Stanfrord CoreNLP Server][2]
* [Stanford CoreNLP for multiple languages][3]
* [Details about the whole setup process][4]


[1]:https://nlp.stanford.edu/software/
[2]:http://stanfordnlp.github.io/CoreNLP/
[3]:http://stanfordnlp.github.io/CoreNLP/other-languages.html#python
[4]:http://stackoverflow.com/questions/32879532/stanford-nlp-for-python


*****************************************************************************

HOW TO INSTALL STANFORD CORE NLP

1. Download [Newest Stanford CoreNLP][5]
2. Unzip your downloaded .zip file. For example, `unzip stanford-corenlp-full-2016-10-31.zip`
3. `cd stanford-corenlp-full-2016-10-31`
4. `java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000`, this will start the server.
timeout is in milliseconds, here we set it to 10 sec above. You should increase it if you pass huge blobs to the server.
5. `pip3 install pycorenlp`
6. [For an example code to test your setup][6]


[5]:http://stanfordnlp.github.io/CoreNLP/
[6]:http://stackoverflow.com/questions/32879532/stanford-nlp-for-python


*****************************************************************************

TEXT PREPROCESSING

* [Annotators][5]


[7]:http://stanfordnlp.github.io/CoreNLP/annotators.html


*****************************************************************************
