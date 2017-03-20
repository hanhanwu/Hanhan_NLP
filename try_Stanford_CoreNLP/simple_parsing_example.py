from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

text = 'To summarize the sprawling, byzantine plot: warning - possible spoilers ahead - an elderly Louvre curator is murdered in the museum. Although shot in the chest, he manages to disrobe and surround himself with cryptographic clues - written in blood AND invisible ink (!) - to the reason for his death. His estranged granddaughter, who, coincidentally is a police inspector (!!) AND a cryptologist (!!!), enlists the aid of a visiting Harvard professor and symbologist (!!!!) in unraveling the multiple mysteries of: '
res = nlp.annotate(text, properties={
                       'annotators': 'tokenize,ssplit,pos',
                       'outputFormat': 'json',
                   })
