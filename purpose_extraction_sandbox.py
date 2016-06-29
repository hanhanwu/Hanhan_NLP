
# token pos are arranged in a specific order, every pos appears in this case once
def get_first_pos_index(general_pos, pos_lst, pre_idx, post_idx):
  for i in range(len(pos_lst)):
    if pos_lst[i].startswith(general_pos) and i > pre_idx and i < post_idx: return i
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
    idx = get_first_pos_index(target_pos_lst[i], pos_lst, pre_idx, post_idx)
    if idx == -1: return []
    idx_lst.append(idx)
    pre_idx = idx
    i += 1
  return [token_lst[idx] for idx in idx_lst]

   
  
# get whole chunk of tokens with the sprcified start and end
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
    idx = get_first_pos_index(reversed_end_target_pos_lst[i], reversed_pos_lst, pre_idx, post_idx)
    if idx == -1: return []
    end_idx_lst.append(len(pos_lst)-1-idx)
    pre_idx = idx
    i += 1
  end_idx_lst = [ei for ei in reserved(end_idx_lst)]
  
  post_idx = end_idx_lst[0]
  while j < len(start_target_pos_lst):
    idx = get_first_pos_index(start_target_pos_lst[j], pos_lst)
  
  # TO + VB + ..... '.' 
