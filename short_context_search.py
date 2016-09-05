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



# method 5: REAL TIME SEARCH TRAINING WITH 1 HIDDEN LAYER NEURAL NETWORK
## It means, it learns from users' input along the time

## CELL 1
from sqlite3 import dbapi2 as sqlite
from sets import Set
from math import tanh

# the slope of the function for any output y
# the output determines how much a node's total input has to change
def dtanh(y):
    return 1.0 - y*y

class onehidden_nn:
    def __init__(self, dbname):
        self.con = sqlite.connect(dbname)
        
        
    def __del__(self):
        self.con.close()
        
        
    def create_tables(self):
        self.con.execute('drop table if exists hidden_node')
        self.con.execute('drop table if exists input_hidden')
        self.con.execute('drop table if exists hidden_output')
        
        self.con.execute('create table hidden_node(create_key)')
        self.con.execute('create table input_hidden(fromid, toid, strength)')
        self.con.execute('create table hidden_output(fromid, toid, strength)')
        
        self.con.execute('create index if not exists hidden_nodeidx on hidden_node(create_key)')
        self.con.execute('create index if not exists ih_fromidx on input_hidden(fromid)')
        self.con.execute('create index if not exists ih_toidx on input_hidden(toid)')
        self.con.execute('create index if not exists ho_fromidx on hidden_output(fromid)')
        self.con.execute('create index if not exists ho_toidx on hidden_output(toid)')
        self.con.commit()
        
    
    # get the strength of a connection in input_hidden table or hidden_output table
    def get_strength(self, fromid, toid, layer):
        if layer == 0: tb = 'input_hidden'
        else: tb = 'hidden_output'
        
        cur = self.con.execute("""
        select strength from %s where fromid=%d and toid=%d
        """ % (tb, fromid, toid)).fetchone()
        if cur == None:
            if layer == 0: return -0.2
            elif layer == 1: return 0
        return cur[0]
    
    
    # if the connection exists, update the strength, otherwise insert a new connection with the strength value
    def set_strength(self, fromid, toid, layer, new_strength):
        if layer == 0: tb = 'input_hidden'
        else: tb = 'hidden_output'
        
        cur = self.con.execute("""
        select rowid from %s where fromid=%d and toid=%d
        """ % (tb, fromid, toid)).fetchone()
        if cur == None:
            self.con.execute("""
            insert into %s (fromid, toid, strength) values (%d,%d,%f)
            """ % (tb, fromid, toid, new_strength))
        else:
            self.con.execute("""
            update %s set strength=%f where rowid=%d
            """ % (tb, new_strength, cur[0]))
        self.con.commit()
        
        
    def create_hidden_node(self, words, urls):
        if len(words) > 3: return
        create_key = '_'.join(sorted([str(wid) for wid in words]))
        cur = self.con.execute("""
        select rowid from hidden_node where create_key='%s'
        """ % create_key).fetchone()
        
        if cur == None:
            cur = self.con.execute("""
            insert into hidden_node (create_key) values ('%s')
            """ % create_key)
            hidden_id = cur.lastrowid
        else:
            hidden_id = cur[0]
        for wid in words:
            self.set_strength(wid, hidden_id, 0, 1.0/len(words))
        for uid in urls:
            self.set_strength(hidden_id, uid, 1, 0.1)
        self.con.commit()
        
    
    # using the input or output ids to find the hidden nodes    
    def find_hidden_nodes(self, words, urls):
        hidden_nodes = Set()
        for wid in words:
            for (hidden_node,) in self.con.execute('select toid from input_hidden where fromid=%d' % wid):
                hidden_nodes.add(hidden_node)
        for uid in urls:
            for (hidden_node,) in self.con.execute('select fromid from hidden_output where toid=%d' % uid):
                hidden_nodes.add(hidden_node)
        return list(hidden_nodes)
    
    
    # setup neural network
    def setup_nn(self, words, urls):
        self.words = words
        self.urls = urls
        self.hidden_nodes = self.find_hidden_nodes(words, urls)
        
        self.li = [1.0]*len(self.words)
        self.lo = [1.0]*len(self.urls)
        self.lh = [1.0]*len(self.hidden_nodes)
        
        # build the weight matrix for input_hidden and hidden_output
        self.w_ih = [[self.get_strength(wid, hid, 0) for hid in self.hidden_nodes] for wid in self.words]
        self.w_ho = [[self.get_strength(hid, uid, 1) for uid in self.urls] for hid in self.hidden_nodes]
        
    def feedforward(self, words, urls):
        
        for j in range(len(self.hidden_nodes)):
            sum = 0.0
            for i in range(len(self.words)):
                sum += self.li[i]*self.w_ih[i][j]
            self.lh[j] = tanh(sum)
            
        for j in range(len(self.urls)):
            sum = 0.0
            for i in range(len(self.hidden_nodes)):
                sum += self.lh[i]*self.w_ho[i][j]
            self.lo[j] = tanh(sum)
            
        return self.lo
    
    
    def backpropagrate(self, targets, N=0.5):
        output_deltas = [0.0]*len(self.urls)
        hidden_deltas = [0.0]*len(self.words)
        
        for i in range(len(self.urls)):
            err = targets[i] - self.lo[i]
            output_deltas[i] = dtanh(self.lo[i])*err
        
        for j in range(len(self.hidden_nodes)):
            sum_err = 0.0
            for k in range(len(self.urls)):
                sum_err += output_deltas[k]*self.w_ho[j][k]
            hidden_deltas[j] = dtanh(self.lh[j])*sum_err
            
        # update hidden_output weights
        for i in range(len(self.hidden_nodes)):
            for j in range(len(self.urls)):
                change = output_deltas[j]*self.lh[i]
                self.w_ho[i][j] += change*N
        
        #  update input_hidden weights
        for i in range(len(self.words)):
            for j in range(len(self.hidden_nodes)):
                change = hidden_deltas[j]*self.li[i]
                self.w_ih[i][j] += change*N
        
        
    def update_db(self):
        for i in range(len(self.words)):
            for j in range(len(self.hidden_nodes)):
                self.set_strength(self.words[i], self.hidden_nodes[j], 0, self.w_ih[i][j])
        
        for i in range(len(self.hidden_nodes)):
            for j in range(len(self.urls)):
                self.set_strength(self.hidden_nodes[i], self.urls[j], 1, self.w_ho[i][j])
                
                
    def train_nn(self, words, urls, selected_url):
        #print '********feedforward********'
        feedforward_output = self.feedforward(words, urls)
        #print feedforward_output
        
        #print '********backpropagrate********'
        targets = [0.0]*len(urls)
        targets[urls.index(selected_url)] = 1.0
        
        self.backpropagrate(targets)
        self.update_db()
        results = self.feedforward(words, urls)
        return results
        
     
## CELL 2
from pyspark.sql import Row

rdd0 = s4.rdd.zipWithIndex().cache()
rdd1 = rdd0.map(lambda (m,idx): Row(Merchant_Info=m[0], S1=m[1], S4=m[2], Idx=idx))
selected_rdd = rdd0.filter(lambda (m, idx): (m[1]!=0 or m[2]!=0))


## CELL 3
NN_df = rdd1.toDF()
NN_df = NN_df.select(NN_df.Idx, NN_df.Merchant_Info)
NN_df.show(truncate=False)
  
  
## CELL 4
query_rdd = sc.parallelize(q6).zipWithIndex()
query_idx = query_rdd.map(lambda (t, idx): idx)
merchant_idx = rdd0.map(lambda (m, idx): idx)
selected_merchant_idx = selected_rdd.map(lambda (m, idx): idx)

query_lst = query_idx.collect()
all_merchant = merchant_idx.collect()
selected_merchant_lst = selected_merchant_idx.collect()


## CELL 5
def train_NN(query_lst, all_merchant, selected_merchant_lst):
  dbname = 'neural_network.db'
  my_nn = onehidden_nn(dbname)
  my_nn.create_tables()
  result = None
  
  # create hidden nodes
  my_nn.create_hidden_node(query_lst, all_merchant)

  # input-hidden
  my_nn.con.execute('select * from input_hidden')
  # hidden-output
  my_nn.con.execute('select * from hidden_output')

  # setup NN
  my_nn.setup_nn(query_lst, all_merchant)
  
  for selected_merchant in selected_merchant_lst:
    result = my_nn.train_nn(query_lst, all_merchant, selected_merchant)
  
  return result
  
  
## CELL 6
NN_results = sc.parallelize(train_NN(query_lst, all_merchant, selected_merchant_lst)).zipWithIndex().toDF().withColumnRenamed('_1', 'NN_score')
cond = [NN_results._2 == NN_df.Idx]
final_NN_df = NN_df.join(NN_results, cond, 'inner').select(NN_df.Idx, NN_df.Merchant_Info, NN_results.NN_score).orderBy(NN_results.NN_score.desc())


## CELL 7
# The out put is the final score after users have chose the first 3 choices seperately
final_NN_df.show(truncate=False)
