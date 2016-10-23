'''
Created on Oct 22, 2016

When doing text data preprocessing, we can also add some feature just like feature engineering in other data analysis work
In this example, I am implementing a very simple example to add text features which could help further data science work
Extract text features from Title, Summary and Publisher of the raw text here
    The context of this is, in the later data analysis such as classification, 
    all the words of a whole dictionary will appear as features, so here just need to mark those appeared words as 1
'''
import re

def text_feature_selection(raw_text):
    # Remove non-alphanumeric characters
    spliter = re.compile("\\W*")
    result_dct = {}
    
    # Extract Title words and each of the word is a Feature, remove very short or very long words
    title_words = [w.lower() for w in spliter.split(raw_text['Title']) if len(w) > 2 and len(w) < 20]
    for w in title_words:
        result_dct['Title:' + w] = 1
        
    # Extract Summary words
    summary_words = [w.lower() for w in spliter.split(raw_text['Summary']) if len(w) > 2 and len(w) < 20]
    
    ## For summary words, count upper case words, if it's more than 30 percent, record it
    ## record word pairs too, here only 2 words in a pair
    upper_count = 0
    for i in len(summary_words):
        w = summary_words[i]
        result_dct[w] = 1
        if w.isupper(): upper_count += 1
        
        if i < len(summary_words)-1:
            word_pair = ' '.join(summary_words[i:i+2])
            result_dct[word_pair] = 1
            
    if float(upper_count)/len(summary_words) > 0.3: result_dct['UpperCase'] = 1
    
    result_dct['Publisher:' + raw_text['Publisher']] = 1
    
    return result_dct
        
    
    
