# When the text context is very short, and you cannot build the search engine by simply calculating
## query terms distance, query terms frequency or query terms position
## In the code here, I am trying different methods to allow better key words search


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
s2 = tmp2.orderBy(tmp2.S2)



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
s2 = tmp2.orderBy(tmp2.S2)



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
s2 = tmp2.orderBy(tmp2.S2)



# TO BE CONTINUED...
