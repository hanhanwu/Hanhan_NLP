from nltk.stem.porter import *
stemmer = PorterStemmer()

def JJ_NN_investment(ts, s):
  key_start = 'investment'
  key_start_idx = -1
  filtered_NN = ['future']
  
  if key_start in s:
    for i in range(len(ts)):
      if ts[i][0].startswith(key_start):
        key_start_idx = i
  
  if key_start_idx != -1:
    if key_start_idx >= 2 and ts[key_start_idx-1][1].startswith('NN'):
      if ts[key_start_idx-1][0] not in filtered_NN:
        if ts[key_start_idx-2][1].startswith('JJ'):  
          return ' '.join([stemmer.stem(t[0]) for t in ts[key_start_idx-2 : key_start_idx]])
        else: return ' '.join([stemmer.stem(t[0]) for t in ts[key_start_idx-1 : key_start_idx]])
      
      

# investment IN .. NN
def investment_IN_NN(ts, s):
  key_start = 'investment'
  key_start_idx = -1
  
  if key_start in s:
    for i in range(len(ts)):
      if ts[i][0].startswith(key_start):
        key_start_idx = i
        break
        
  if key_start_idx != -1:
    after_idx = key_start_idx + 1
    if ts[after_idx][1].startswith('IN'):
      first_NN = 0
      start_combination_idx = after_idx
      end_combination_idx = -1
      while after_idx < len(ts) and ts[after_idx][1].startswith('.') == False:
        if ts[after_idx][1].startswith('NN') and first_NN == 0:
          first_NN += 1
        elif ts[after_idx][1].startswith('NN') == False and first_NN == 1:
          end_combination_idx = after_idx
          return ' '.join([stemmer.stem(t[0]) for t in ts[start_combination_idx+1 : end_combination_idx]])

        after_idx += 1
    
  return None



# invest IN .. NN
def invest_IN_NN(ts, s):
  key_start = 'invest'
  key_start_idx = -1
  
  if key_start in s:
    for i in range(len(ts)):
      if ts[i][0].startswith(key_start):
        key_start_idx = i
        break
        
  if key_start_idx != -1:
    after_idx = key_start_idx + 1
    if ts[after_idx][1].startswith('IN'):
      first_NN = 0
      start_combination_idx = after_idx
      end_combination_idx = -1
      while after_idx < len(ts) and ts[after_idx][1].startswith('.') == False:
        if ts[after_idx][1].startswith('NN') and first_NN == 0:
          first_NN += 1
        elif ts[after_idx][1].startswith('NN') == False and first_NN == 1:
          end_combination_idx = after_idx
          return ' '.join([stemmer.stem(t[0]) for t in ts[start_combination_idx+1 : end_combination_idx]])

        after_idx += 1
    
  return None
    
