# When the text context is very short, and you cannot build the search engine by simply calculating
## query terms distance, query terms frequency or query terms position
## In the code here, I am trying different methods to allow better key words search

from nltk.stem.porter import *

# tokens here have to be split() and lower() first, since the user input will be a string
q1 = ["drink", "wine"]
q2 = ["hamburger"]
q3 = ["gardening", "plants"]
q4 = ["home", "gardening"]
q5 = ["chinese", "restaurant"]
q6 = ["hair", "beauty"]
q7 = ["beauty", "hair"]
q8 = ["beauty", "hair", "salon"]

stemmer = PorterStemmer()

stemmed_q1 = [stemmer.stem(t) for t in q1]
print stemmed_q1
stemmed_q2 = [stemmer.stem(t) for t in q2]
print stemmed_q2
stemmed_q3 = [stemmer.stem(t) for t in q3]
print stemmed_q3
stemmed_q4 = [stemmer.stem(t) for t in q4]
print stemmed_q4
stemmed_q5 = [stemmer.stem(t) for t in q5]
print stemmed_q5
stemmed_q6 = [stemmer.stem(t) for t in q6]
print stemmed_q6
stemmed_q7 = [stemmer.stem(t) for t in q7]
print stemmed_q7
stemmed_q8 = [stemmer.stem(t) for t in q8]
print stemmed_q8



# method 1: calculate scores based on query terms existence
from pyspark.sql.types import IntegerType

def token_existence(stemmed_token_lst, merchant_info):
  score = 0
  for t in stemmed_token_lst:
    if t in merchant_info: score += 1
  return score

calculate_token_existenceUDF = udf(lambda r: token_existence(stemmed_q1, r.lower()), IntegerType())
tmp1 = df7.withColumn("S1", calculate_token_existenceUDF(df7.Merchant_Info))
s1 = tmp1.orderBy(tmp1.S1.desc())



## Test 1 - unstemmed text context words, add score of the min_distance for each query token
# method 2: find merchant_info that contains closest token which passed a threshold
from Levenshtein import distance
from pyspark.sql.types import IntegerType
import sys

def closest_token(stemmed_token_lst, merchant_info):
  score = 0
  merchant_tokens = merchant_info.split()  # only split works in merchant_info
  for t in stemmed_token_lst:
    min_dist = sys.maxint
    for m in merchant_tokens:
      tmp_dist = distance(t, m)
      if min_dist > tmp_dist:
        min_dist = tmp_dist
    score += min_dist
  return score

calculate_closest_tokenUDF = udf(lambda r: closest_token(stemmed_q3, r.lower()), IntegerType())
tmp2 = df7.withColumn("S2", calculate_closest_tokenUDF(df7.Merchant_Info))
s2 = tmp2.filter(tmp2.S2 < 5).orderBy(tmp2.S2)



## Test 2 - temmed text context words, add score of the min_distance for each query token
# method 2: find merchant_info that contains closest token which passed a threshold
from Levenshtein import distance
from pyspark.sql.types import IntegerType
import sys

def closest_token(stemmed_token_lst, merchant_info):
  score = 0
  merchant_tokens = [stemmer.stem(m) for m in merchant_info.split()]  # stem merchant tokens here
  for t in stemmed_token_lst:
    min_dist = sys.maxint
    for m in merchant_tokens:
      tmp_dist = distance(t, m)
      if min_dist > tmp_dist:
        min_dist = tmp_dist
    score += min_dist
  return score

calculate_closest_tokenUDF = udf(lambda r: closest_token(stemmed_q3, r.lower()), IntegerType())
tmp2 = df7.withColumn("S2", calculate_closest_tokenUDF(df7.Merchant_Info))
s2 = tmp2.filter(tmp2.S2 < 5).orderBy(tmp2.S2)



## Test 3 - stemmed text context words, only use the min_distance for all as the final score
# method 2: find merchant_info that contains closest token which passed a threshold
from Levenshtein import distance
from pyspark.sql.types import IntegerType
import sys

def closest_token(stemmed_token_lst, merchant_info):
  min_dist = sys.maxint  # only use the min_dist for all as the score
  merchant_tokens = [stemmer.stem(m) for m in merchant_info.split()]  # stem merchant tokens here
  for t in stemmed_token_lst:
    for m in merchant_tokens:
      tmp_dist = distance(t, m)
      if min_dist > tmp_dist:
        min_dist = tmp_dist
  return min_dist

calculate_closest_tokenUDF = udf(lambda r: closest_token(stemmed_q2, r.lower()), IntegerType())
tmp2 = df7.withColumn("S2", calculate_closest_tokenUDF(df7.Merchant_Info))
s2 = tmp2.filter(tmp2.S2 < 5).orderBy(tmp2.S2)



# method 3: query term order
## if the token exist, get 1 more score, if its previous token is also in & before, get 1 more score
def ordered_token(stemmed_token_lst, merchant_info):
  score = 0
  idx_q = 0
  for tk in stemmed_token_lst:     # I'm using Spark and could only use this type of for loop
    if tk in merchant_info:
      score += 1
      if idx_q == 0: continue
      idx_m = merchant_info.index(tk)
      if stemmed_token_lst[idx_q-1] in merchant_info[0:idx_m]:    # not using recursion because both text is short, and I'm wondering with Spark distribution system, can I use recursion
        score += 1
    idx_q += 1
    
  return score


calculate_ordered_tokenUDF = udf(lambda r: ordered_token(stemmed_q5, r.lower()), IntegerType())
tmp3 = df7.withColumn("S3", calculate_ordered_tokenUDF(df7.Merchant_Info))
s3 = tmp3.orderBy(tmp3.S3.desc())



# method 4: query terms distance
## for the same amount of query token existence, closer distance better
## the mthods used here could only be used for short context, otherwise it will be time consuming
import re
import sys

def get_min_dist(idx_lst1, idx_lst2):
  min_dist = sys.maxint
  for idx1 in idx_lst1:
    for idx2 in idx_lst2:
      dst = abs(idx1-idx2)
      if dst < min_dist:
        min_dist = dst
  return min_dist
  

def token_distance(token_lst, merchant_info):
  sum_min_disct = 0
  
  for i in range(len(token_lst)-1):
    for j in range(i+1, len(token_lst)):
      if token_lst[i] in merchant_info and token_lst[j] in merchant_info:
        t1 = token_lst[i]
        t2 = token_lst[j]
        idx_lst1 = [m.start() for m in re.finditer(t1, merchant_info)]
        idx_lst2 = [m.start() for m in re.finditer(t2, merchant_info)]
        min_dst = get_min_dist(idx_lst1, idx_lst2)
        sum_min_disct += min_dst
        
  return sum_min_disct


calculate_token_existenceUDF = udf(lambda r: token_existence(q6, r.lower()), IntegerType())
tmp1 = df7.withColumn("S1", calculate_token_existenceUDF(df7.Merchant_Info)).cache()

calculate_token_distanceUDF = udf(lambda r: token_distance(q6, r.lower()), IntegerType())
tmp4 = tmp1.withColumn("S4", calculate_token_distanceUDF(tmp1.Merchant_Info))
s4 = tmp4.orderBy(tmp1.S1.desc(), tmp4.S4.asc())


# TO BE CONTINUED...
