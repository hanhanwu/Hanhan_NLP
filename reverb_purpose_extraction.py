'''
Created on Jul 19, 2016
mac terminal command: 
java -Xmx512m -jar reverb-latest.jar all_purpose.csv > all_purpose_export.txt
Note: may need to use Levenshtein Distance or clustering if the final results are unique
      may also need to add " O" in the all_purpose_export.txt since some output is missing this..
      may need to replace all the " in the string to ''
'''

import re
import operator
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.cluster.tests.test_k_means import n_samples


def sort_dct_by_value(mydct, rev = True):
    sorted_lst = sorted(mydct.items(), key=operator.itemgetter(1), reverse=rev)
    for itm in sorted_lst:
        print itm
    print "******************************"


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic #%d:" % topic_idx
        print " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        print 
        
        
def NMF_feature_extraction(text_lst, n_samples, n_features, n_topics, n_top_words):
    print "Extracting tf-idf features for NMF..."
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(text_lst)
    print "Fitting the NMF model with tf-idf features," "n_samples=%d and n_features=%d..." % (n_samples, n_features)
    nmf = NMF(n_components=n_topics, random_state=1, alpha=.1, l1_ratio=.5).fit(tfidf)
    print "\nTopics in NMF model:" 
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    print_top_words(nmf, tfidf_feature_names, n_top_words)
    print "*************end NMF****************"
    
    
def LDA_feature_extraction(text_lst, n_samples, n_features, n_topics, n_top_words):
    print "Extracting tf features for LDA..."
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=n_features, stop_words='english')
    tf = tf_vectorizer.fit_transform(text_lst)
    print "Fitting LDA models with tf features, n_samples=%d and n_features=%d..." % (n_samples, n_features)
    lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=5,
                                    learning_method='online', learning_offset=50.,
                                    random_state=0)
    lda.fit(tf)
    print "\nTopics in LDA model:"
    tf_feature_names = tf_vectorizer.get_feature_names()
    print_top_words(lda, tf_feature_names, n_top_words)
    print "*************end LDA****************"


def main():
    r_pre = "[your file path]/all_purpose"
    f_path = "[your file path]/all_purpose_export.txt"
    
    p1 = r_pre + "\.csv\t\d+\t(.*?)(\t\d+){6}"
    p2 = "(.*?)O\s*\t(.*?)"
    
    extracted_combo_dct = {}
    stemmed_extracted_combo_dct = {}
    extracted_combo_lst = []
    stemmed_extracted_combo_lst = []
    
    n_top_words = 3
    n_topics = 20
    n_features = 50
    
    
    f = open(f_path)
    for l in f:
        r1 = re.search(p1, l)
        m1 = ' '.join(r1.group(1).split('\t'))
        r2 = re.search(p2, l)
        if r2 == None:
            print l
            break    # used to add missing " O"
        m2 = ' '.join([e for e in l.split(r2.group(1))[1].split('O')[1].split('\t') if e != ' ']).split('\n')[0]
        
        extracted_combo_dct.setdefault(m1, 0)
        stemmed_extracted_combo_dct.setdefault(m2, 0)
         
        extracted_combo_dct[m1] += 1
        stemmed_extracted_combo_dct[m2] += 1
        
        extracted_combo_lst.append(m1)
        stemmed_extracted_combo_lst.append(m2)
         
     
    sort_dct_by_value(extracted_combo_dct)
    sort_dct_by_value(stemmed_extracted_combo_dct)
    
    n_samples = len(extracted_combo_lst)
    n_stemmed_samples = len(stemmed_extracted_combo_lst)
    
    # using NMF feature extraction
    NMF_feature_extraction(extracted_combo_lst, n_samples, n_features, n_topics, n_top_words)
    NMF_feature_extraction(stemmed_extracted_combo_lst, n_stemmed_samples, n_features, n_topics, n_top_words)
    
    # using LDA feature extraction
    LDA_feature_extraction(extracted_combo_lst, n_samples, n_features, n_topics, n_top_words)
    LDA_feature_extraction(stemmed_extracted_combo_lst, n_stemmed_samples, n_features, n_topics, n_top_words)
    
    
if __name__ == "__main__":
    main()
