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
def get_VBNN_combination(interaction):
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






# Extract Interactions
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
  print
