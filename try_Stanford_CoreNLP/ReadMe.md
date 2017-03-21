

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
6. [pycorenlp][7]
7. [For an example code to test your setup][6]
8. [CoreNLP Server, quick start][10]


[5]:http://stanfordnlp.github.io/CoreNLP/
[6]:http://stackoverflow.com/questions/32879532/stanford-nlp-for-python
[7]:https://github.com/smilli/py-corenlp
[10]:http://stanfordnlp.github.io/CoreNLP/corenlp-server.html


*****************************************************************************

TEXT PREPROCESSING

* [Annotators][8]
* [simple parsing example][9] - in this very simple example, it does tokenize, sentence spliting and POS parsing. You can have more choices by changing the values in `annotators`, check which annotators the library has through the above url
* Sometimes, people hope to use what you have created and give them enough flexibility to modify your code, therefore, you have to use some OO design. [Here is an example][11] - you type command line and indicate your input & output, it will do sentence split, tokenization and POS parsing for you.
* [.sh file here][12] is where you put your command line input. Your input can be a file or a folder full of files; output has to be a folder.
* Each time when you want to run the code, just `cd` to you folder where you put this .sh file, then type in your terminal `sh run_source_code.sh`. Makes life easier, isn't it?


[8]:http://stanfordnlp.github.io/CoreNLP/annotators.html
[9]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/try_Stanford_CoreNLP/simple_parsing_example.py
[11]:https://github.com/hanhanwu/Hanhan_NLP/tree/master/try_Stanford_CoreNLP/parsing_with_OO
[12]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/try_Stanford_CoreNLP/parsing_with_OO/run_source_code.sh


*****************************************************************************
