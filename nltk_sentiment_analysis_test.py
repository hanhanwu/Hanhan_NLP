'''
Created on Nov 1, 2016
'''

from vaderSentiment import sentiment as vaderSentiment

sentences = [
              """Most sentiment tools are shit.""",
              """NLTK sentiment analysis is also shit...""",
              """When the system down, they lost all the money""",
              """I hate Microsoft products! I hate working on Windows! I hate being managed by people!""",
              """I hate days when I cannot be happy, and have to work in the office. God, please end this internship soon.... I hate working here. I hate I cannot be happy all the time. Why, today I'm feeling so sad. God, and today I'm so many things to do. I simply want to get more sleep, I'm so tired"""
            ]
for sentence in sentences:
    print(sentence)
    vs = vaderSentiment(sentence)
    print str(vs)
