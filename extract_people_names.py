import nltk
import nltk.tag.stanford as st

path_pre = "[your full path for NER package]/stanford-ner-2015-12-09/"

st = st.StanfordNERTagger(path_pre+'classifiers/english.all.3class.distsim.crf.ser.gz', path_pre+'stanford-ner.jar')

text1 = """emmanuel means jesus!"""
text2 = """Emmanuel means jesus!"""
text3 = """Emmanuel means Jesus!"""
text4 = """Does Emmanuel like Ice Cream like Hanhan does?"""
text5 = """Emmanuel, miss Hanhan?"""
text6 = """Does Tim Hortons like KFC?"""


all_text = [text1, text2, text3, text4, text5, text6]

for t in all_text:
    for sent in nltk.sent_tokenize(t):
        tokens = nltk.tokenize.word_tokenize(sent)
        tags = st.tag(tokens)
        for tag in tags:
            if tag[1]=='PERSON': print (tag, t)

