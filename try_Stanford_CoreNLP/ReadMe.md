

*****************************************************************************

RESOURCES

* [Stanford Software][1]
* [Download Stanfrord CoreNLP Server][2]
* [Stanford CoreNLP for multiple languages][3]
* [Details about the whole setup process][4]


*****************************************************************************

HOW TO INSTALL STANFORD CORE NLP

1. Download [Newest Stanford CoreNLP][5]
2. Unzip your downloaded .zip file. For example, `unzip stanford-corenlp-full-2016-10-31.zip`
3. `cd stanford-corenlp-full-2016-10-31`
4. `java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000`, this will start the server.
timeout is in milliseconds, here we set it to 10 sec above. You should increase it if you pass huge blobs to the server.
5. `pip3 install pycorenlp`
6. [pycorenlp][7]
7. [An example code to test your setup - Sentiment Analysis][6]
8. [CoreNLP Server, quick start][10]


*****************************************************************************

TEXT PREPROCESSING

* [Annotators][8]
* The most simple way to run CoreNLP is through command line, `java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt -outputDirectory your_output_folder`, here `-file` supports folder input
* [simple parsing example][9] - in this very simple example, it does tokenize, sentence spliting and POS parsing. You can have more choices by changing the values in `annotators`, check which annotators the library has through the above url
* Sometimes, people hope to use what you have created and give them enough flexibility to modify your code, therefore, you have to use some OO design. [Here is an example][11] - you type command line and indicate your input & output, it will do sentence split, tokenization and POS parsing for you.
* [.sh file here][12] is where you put your command line input. Your input can be a file or a folder full of files; output has to be a folder.
* Each time when you want to run the code, just `cd` to you folder where you put this .sh file, then type in your terminal `sh run_source_code.sh`. Makes life easier, isn't it?
* As you can see in OO design example, there are 2 versions preprocess code, [version 1][14] and [version 2][13]. I have made some changes in version 2, so that it is more robust if someone else want to use or modify the code.


*****************************************************************************

DEPENDENCY TREES

* To use Stanford Core NLP is truly painful, it has so many wrapper or relevant simplified libraries, with different methods to turn on the server, and in order to turn server you may need to be under a certain folder, type the right command or there are other constraints....
* Anyway, let me reocrd methods I tried...
* Method 1 - pycorenlp
  * `pip install pycorenlp`
  * Download [Newest Stanford CoreNLP][5]
  * Unzip your downloaded .zip file. For example, `unzip stanford-corenlp-full-2016-10-31.zip`
  * `cd stanford-corenlp-full-2016-10-31`
  * `java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000`, this will start the server.
  * Run your python code under folder `stanford-corenlp-full-2016-10-31/`...
  * Check my code [here][15] for METHOD 1
  
* Method 2 - stanford-core-python
  * <b>Better NOT to try this one</b>
  * This requires old format for not only input file but also old core NLP package, very troublesome
  * Download the required package and install the server: https://github.com/dasmith/stanford-corenlp-python
    * Only `stanford-corenlp-full-2014-08-27.zip` would work, I tried other release, didn't work
  * Then try similar command line here: https://nlp.stanford.edu/software/lex-parser.shtml
    * `java -mx200m -cp "*" edu.stanford.nlp.parser.lexparser.LexicalizedParser -retainTMPSubcategories -outputFormat "wordsAndTags,penn,typedDependencies" englishPCFG.ser.gz mumbai.txt`
      * When you are using `-cp "*"`, run the command under folder `stanford-corenlp-full-2014-08-27/`
      * `englishPCFG.ser.gz mumbai.txt` has special format and your input file has to be that format.... But I don't know what is that old format, looks so troublesome, lazy people like me will just try another solution... Also, the input has to be a file, cannot be a string
  
  
*****************************************************************************

[1]:https://nlp.stanford.edu/software/
[2]:http://stanfordnlp.github.io/CoreNLP/
[3]:http://stanfordnlp.github.io/CoreNLP/other-languages.html#python
[4]:http://stackoverflow.com/questions/32879532/stanford-nlp-for-python
[5]:http://stanfordnlp.github.io/CoreNLP/
[6]:http://stackoverflow.com/questions/32879532/stanford-nlp-for-python
[7]:https://github.com/smilli/py-corenlp
[10]:http://stanfordnlp.github.io/CoreNLP/corenlp-server.html
[8]:http://stanfordnlp.github.io/CoreNLP/annotators.html
[9]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/try_Stanford_CoreNLP/simple_parsing_example.py
[11]:https://github.com/hanhanwu/Hanhan_NLP/tree/master/try_Stanford_CoreNLP/parsing_with_OO
[12]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/try_Stanford_CoreNLP/parsing_with_OO/run_source_code.sh
[13]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/try_Stanford_CoreNLP/parsing_with_OO/text_preprocessing/preprocess2.py
[14]:https://github.com/hanhanwu/Hanhan_NLP/blob/master/try_Stanford_CoreNLP/parsing_with_OO/text_preprocessing/preprocess.py
[15]https://github.com/hanhanwu/Hanhan_NLP/blob/master/NLP_dependency_trees.ipynb
  
