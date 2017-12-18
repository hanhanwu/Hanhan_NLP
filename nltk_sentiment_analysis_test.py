'''
Created on Nov 1, 2016
2017 Update, new vaderSentiment can be found at: https://github.com/cjhutto/vaderSentiment
'''

from vaderSentiment import sentiment as vaderSentiment

sentences = [
              """Most sentiment tools are shit.""",
              """NLTK sentiment analysis is also shit...""",
              """When the system down, they lost all the money""",
              """I hate Microsoft products! I hate working on Windows! I hate being managed by people!""",
              """I hate days when I cannot be happy, and have to work in the office. God, please end this internship soon.... I hate working here. I hate I cannot be happy all the time. Why, today I'm feeling so sad. God, and today I'm so many things to do. I simply want to get more sleep, I'm so tired""",
              """Heartbreaking!""",
              """time kills everything""",
              """I should learn Scala sson, always write Python has some limited ability...""",
              """I like seeing people reply my emails early when I get here early, I hate scilence! But when I am working, I am very quiet too...""",
              """The saddest thing is, long long long time ago, you satrted to like this person because you felt the similarity, but when time passed by, when that person is becoming mroe and more indifference, you gradually realized you may be living in 2 different worlds and you are pusuing different career, but this is not the most painful part. The most painful part is, when you are well prepared to embrace this difference (since if you really like each other, you can grow together and help each other thrive), but that person does not think so at all. Gradually, you have realized, there must be another woman there in his life, but sadly, you simply lie to yourself all the time and do not want to admit, do not want to let him go.... Meanwhile, you cannot tell anyone such as parents or friends, they will all blame you, for not let go in such a long time"""
             ]
for sentence in sentences:
    print(sentence)
    vs = vaderSentiment(sentence)
    print str(vs)
