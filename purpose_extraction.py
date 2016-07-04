# Using Spark Python Notebook here

# Vancouver - 190
json_data = sqlContext.read.format('json').load("[HDFS path]")
json_lst = json_data.collect()
vancouver_purpose = [p for p in json_lst[0]]

# Burnaby - 64
json_data = sqlContext.read.format('json').load("[HDFS path]")
json_lst = json_data.collect()
burnaby_purpose = [p for p in json_lst[0]]

# Surrey - 77
json_data = sqlContext.read.format('json').load("[HDFS path]")
json_lst = json_data.collect()
surrey_purpose = [p for p in json_lst[0]]



all_purpose = []
all_purpose.extend(vancouver_purpose)
all_purpose.extend(burnaby_purpose)
all_purpose.extend(surrey_purpose)

print len(all_purpose)



import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('maxent_treebank_pos_tagger')
nltk.download('averaged_perceptron_tagger')



# extract continious NN
def get_NN_combinations(interaction):
  all_NN_combinations = []
  for i in range(len(interaction)):
    if interaction[i][1].startswith('NN'):
      j = i + 1
      tmp_NN_combinations = []
      while j < len(interaction):
        if interaction[j][1].startswith('NN'): 
          if j == i+1: 
            tmp_NN_combinations.append(interaction[i][0])
          tmp_NN_combinations.append(interaction[j][0])
        else: break
        j += 1
      if len(tmp_NN_combinations) > 0: all_NN_combinations.append(' '.join(tmp_NN_combinations))
        
  return all_NN_combinations



# extract VBNN combinations
def get_VBNN_combinations(interaction):
  all_VBNN_combinations = []
  for i in range(len(interaction)):
    if interaction[i][1].startswith('VB'):
      j = i + 1
      tmp_VBNN_combinations = []
      while j < len(interaction):
        if interaction[j][1].startswith('NN'):
          tmp_VBNN_combinations.append(interaction[i][0])
          tmp_VBNN_combinations.append(interaction[j][0])
        else: break
        j += 1
      if len(tmp_VBNN_combinations) > 0: all_VBNN_combinations.append(' '.join(tmp_VBNN_combinations))
        
  return all_VBNN_combinations



# extract VB...NN combinations
def get_VB2NN_combinations(interaction):
  all_VB2NN_combinations = []
  for i in range(len(interaction)):
    if interaction[i][1].startswith('VB'):
      j = i + 2    # here because I have VBNN method :)
      tmp_VB2NN_combinations = []
      while j < len(interaction):
        if interaction[j][1].startswith('NN'):
          for k in range(i, j+1):
            tmp_VB2NN_combinations.append(interaction[k][0])
          break
        j += 1
      if len(tmp_VB2NN_combinations) > 0: all_VB2NN_combinations.append(' '.join(tmp_VB2NN_combinations))
        
  return all_VB2NN_combinations



# extract strict NN entities
def get_restrict_NN_entities(interaction):
  all_NN_entities = set()
  for i in range(len(interaction)):
    if interaction[i][1] == 'NN':
      all_NN_entities.add(interaction[i][0])
  return list(all_NN_entities)



# extract strict VB entities
def get_restrict_VB_entities(interaction):
  all_VB_entities = set()
  for i in range(len(interaction)):
    if interaction[i][1] == 'VB':
      all_VB_entities.add(interaction[i][0])
  return list(all_VB_entities)


# extract NN entities, startswith NN
def get_NN_entities(interaction):
  all_NN_entities = set()
  for i in range(len(interaction)):
    if interaction[i][1].startswith('NN'):
      all_NN_entities.add(interaction[i][0])
  return list(all_NN_entities)




NN_combinations_dict = {}
VBNN_combinations_dict = {}
VB2NN_combinations_dict = {}
NN_entities_dict = {}
VB_entities_dict = {}
multiple_NN_entities_dict = {}



# Product - Extract Interactions
import re

innocent_starts = ('ms.', 'mr.', 'mrs.', 'miss.', 'i.e')
Specific_NN = ["LOS", "TRXN", "ETO", "FLFA", "Vancity", "TDS", "CIBC", "LOC", "FL", "FA", "HELOC"]    # NNs that only used in this scenario
words2pos = ['want', 'wants', 'member', 'mbr', 'members', 'for']


def get_pos_index(general_pos, pos_lst, pre_idx, post_idx, specified_position=0, follow_close=False):
  if follow_close == False:
    all_idx = [i for i,x in enumerate(pos_lst) if x.startswith(general_pos) and i > pre_idx and i < post_idx]
    if len(all_idx) != 0 and len(all_idx) > specified_position: return all_idx[specified_position]
  else:
    idx = pre_idx + 1
    if pos_lst[idx].startswith(general_pos): return idx
  return -1
    
  
  
# pos appears in order 
def extract_simple_sequences(s, target_pos_lst):
  token_lst = [tp[0] for tp in s]
  pos_lst = [tp[1] for tp in s]
  target_pos_lst_len = len(target_pos_lst)
  i = 0
  pre_idx = -1
  idx_lst = []
  post_idx = len(pos_lst)
  while i < target_pos_lst_len:
    idx = get_pos_index(target_pos_lst[i], pos_lst, pre_idx, post_idx)
    if idx == -1: return []
    idx_lst.append(idx)
    pre_idx = idx
    i += 1
  # return [token_lst[idx] for idx in idx_lst] [pos_lst[idx] for idx in idx_lst]
  return [s[idx] for idx in idx_lst]

   
  
# get whole chunk of tokens with the sprcified start and end, 
## and the start end is the pos closest to the end pos if there are multiple in a sentence
def get_whole_chunk(s, start_target_pos_lst, end_target_pos_lst):
  token_lst = [tp[0] for tp in s]
  pos_lst = [tp[1] for tp in s]
  reversed_pos_lst = [pos for pos in reversed(pos_lst)]
  reversed_end_target_pos_lst = [pos for pos in reversed(end_target_pos_lst)]
  
  i = 0
  j = 0
  start_idx = -1
  end_idx = -1
  
  pre_idx = -1
  post_idx = len(pos_lst)
  end_idx_lst = []
  while i < len(end_target_pos_lst):
    idx = get_pos_index(reversed_end_target_pos_lst[i], reversed_pos_lst, pre_idx, post_idx)
    if idx == -1: return []
    end_idx_lst.append(len(pos_lst)-1-idx)
    pre_idx = idx
    i += 1
  end_idx_lst = [ei for ei in reversed(end_idx_lst)]
  
  post_idx = end_idx_lst[0]
  pre_idx = -1
  first = 0
  first_idx = -1
  while j < len(start_target_pos_lst):
    if first == 0:
      idx = get_pos_index(start_target_pos_lst[j], pos_lst, pre_idx, post_idx, specified_position=-1, follow_close=False)    # set start token closest to the end tokens, start tokens no need to follow up close each other
      first_idx = idx
      first = 1
    else:
      idx = get_pos_index(start_target_pos_lst[j], pos_lst, pre_idx, post_idx, follow_close=True)   # tokens (non-starter) in start tokes should follow each other close

    if idx == -1: return []
    pre_idx = idx
    j += 1
    
  return s[first_idx:end_idx_lst[-1]]



def contains_words(NN_contains, tk):
  for NN in NN_contains:
    if NN.lower() in tk.lower():
      return True
  return False



for tst_s in all_purpose:
  sentences = nltk.tokenize.sent_tokenize(tst_s)
  token_sets = [nltk.tokenize.word_tokenize(s) for s in sentences]
  for j in range(len(token_sets)):
    split_lst = []
    all_tokens = []
    abnormal_lst = set()
    for t in token_sets[j]:
      if t.lower().startswith(innocent_starts) or re.search('\d\.\d+', t) != None:
        continue
      m = re.search('(\w+)(\.)(\w+)', t)
      if m != None: 
        abnormal_lst.add(m.group(0))
        for i in range(1,4): split_lst.append(m.group(i))

    for t in token_sets[j]:
      if t not in abnormal_lst: all_tokens.append(t)
      else:
        all_tokens.extend(split_lst)

    token_sets[j] = all_tokens

    for i in range(len(token_sets[j])):
      if token_sets[j][i] not in Specific_NN:
        token_sets[j][i] = token_sets[j][i].lower()
    
  pos_tagged_tokens = [nltk.pos_tag(ts) for ts in token_sets]
  
  for i in range(len(pos_tagged_tokens)):
    for j in range(len(pos_tagged_tokens[i])):
      if pos_tagged_tokens[i][j][0] in words2pos:
        pos_tagged_tokens[i][j] = list(pos_tagged_tokens[i][j])
        pos_tagged_tokens[i][j][1] = pos_tagged_tokens[i][j][0]
        pos_tagged_tokens[i][j] = tuple(pos_tagged_tokens[i][j])
        
  interaction_collections = []
  
  # MD + TO + VB + NN
  for ts in pos_tagged_tokens:
    target_pos = ['MD', 'TO', 'VB', 'NN']
    interactions = extract_simple_sequences(ts, target_pos)
    if len(interactions) > 0:
      interaction_collections.append(interactions)

  # for + NN
  for ts in pos_tagged_tokens:
    target_pos = ['for', 'NN']
    interactions = extract_simple_sequences(ts, target_pos)
    if len(interactions) > 0:
      interaction_collections.append(interactions)

  # member/members + VB .... NN ..'.'
  for ts in pos_tagged_tokens:
    start_target_pos_lst = ['member', 'VB']
    end_target_pos_lst = ['NN', '.']
    interactions = get_whole_chunk(ts, start_target_pos_lst, end_target_pos_lst)
    if len(interactions) > 0:
      interaction_collections.append(interactions)

  # member/members + VB .... NN ..':'
  for ts in pos_tagged_tokens:
    start_target_pos_lst = ['member', 'VB']
    end_target_pos_lst = ['NN', ':']
    interactions = get_whole_chunk(ts, start_target_pos_lst, end_target_pos_lst)
    if len(interactions) > 0:
      interaction_collections.append(interactions)

  # mbr + VB .... NN ../'.'
  for ts in pos_tagged_tokens:
    start_target_pos_lst = ['mbr', 'VB']
    end_target_pos_lst = ['NN', '.']
    interactions = get_whole_chunk(ts, start_target_pos_lst, end_target_pos_lst)
    if len(interactions) > 0:
      interaction_collections.append(interactions)

  # mbr + VB .... NN ..':'
  for ts in pos_tagged_tokens:
    start_target_pos_lst = ['mbr', 'VB']
    end_target_pos_lst = ['NN', ':']
    interactions = get_whole_chunk(ts, start_target_pos_lst, end_target_pos_lst)
    if len(interactions) > 0:
      interaction_collections.append(interactions)

  # TO + VB + ..... '.' 
  for ts in pos_tagged_tokens:
    start_target_pos_lst = ['TO', 'VB']
    end_target_pos_lst = ['.']
    interactions = get_whole_chunk(ts, start_target_pos_lst, end_target_pos_lst)
    if len(interactions) > 0:
      interaction_collections.append(interactions)

  # TO + VB + ..... ':' 
  for ts in pos_tagged_tokens:
    start_target_pos_lst = ['TO', 'VB']
    end_target_pos_lst = [':']
    interactions = get_whole_chunk(ts, start_target_pos_lst, end_target_pos_lst)
    if len(interactions) > 0:
      interaction_collections.append(interactions)

  # want/wants to + VB .... '.'
  for ts in pos_tagged_tokens:
    start_target_pos_lst = ['want', 'TO', 'VB']
    end_target_pos_lst = ['.']
    interactions = get_whole_chunk(ts, start_target_pos_lst, end_target_pos_lst)
    if len(interactions) > 0:
      interaction_collections.append(interactions)

  # want/wants to + VB ..... ':'
  for ts in pos_tagged_tokens:
    start_target_pos_lst = ['want', 'TO', 'VB']
    end_target_pos_lst = [':']
    interactions = get_whole_chunk(ts, start_target_pos_lst, end_target_pos_lst)
    if len(interactions) > 0:
      interaction_collections.append(interactions)
    
  if len(sentences) > 0: print sentences
  for interaction in interaction_collections:
    print interaction
    
    NN_combinations = get_NN_combinations(interaction)
    if len(NN_combinations) > 0:
      for NN_combination in NN_combinations:
        NN_combinations_dict.setdefault(NN_combination, 0)
        NN_combinations_dict[NN_combination] += 1
        
    VBNN_combinations = get_VBNN_combinations(interaction)
    if len(VBNN_combinations) > 0:
      for VBNN_combination in VBNN_combinations:
        VBNN_combinations_dict.setdefault(VBNN_combination, 0)
        VBNN_combinations_dict[VBNN_combination] += 1
        
    VB2NN_combinations = get_VB2NN_combinations(interaction)
    if len(VB2NN_combinations) > 0:
      for VB2NN_combination in VB2NN_combinations:
        VB2NN_combinations_dict.setdefault(VB2NN_combination, 0)
        VB2NN_combinations_dict[VB2NN_combination] += 1
        
    NN_entities = get_restrict_NN_entities(interaction)
    if len(NN_entities) > 0:
      for NN_entity in NN_entities:
        NN_entities_dict.setdefault(NN_entity, 0)
        NN_entities_dict[NN_entity] += 1
        
    VB_entities = get_restrict_VB_entities(interaction)
    if len(VB_entities) > 0:
      for VB_entity in VB_entities:
        VB_entities_dict.setdefault(VB_entity, 0)
        VB_entities_dict[VB_entity] += 1
        
    multiple_NN_entities = get_NN_entities(interaction)
    if len(multiple_NN_entities) > 0:
      for multiple_NN_entity in multiple_NN_entities:
        multiple_NN_entities_dict.setdefault(multiple_NN_entity, 0)
        multiple_NN_entities_dict[multiple_NN_entity] += 1
    
  print
