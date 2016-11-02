'''
Created on Nov 1, 2016
'''

from vaderSentiment import sentiment as vaderSentiment

sentences = [
              """Most sentiment tools are shit.""",
              """NLTK sentiment analysis is also shit...""",
              """When the system down, they lost all the money"""
            ]
for sentence in sentences:
    print(sentence)
    vs = vaderSentiment(sentence)
    print str(vs)
