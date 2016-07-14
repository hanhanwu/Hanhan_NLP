# [VB(closest VB)] [(JJ..) (NN..)] to VB combinations

def get_howto_combinations(ts):
  key_start = 'to'
  key_start_idx = -1
  
  for i in range(len(ts)):
    if ts[i][0] == key_start:
      key_start_idx = i
      
  # key_start_idx must > 0 since this function only runs when it's a TO...VB combination
  pre_idx = key_start_idx - 1
  first_NN = 0
  end_idx = -1
  start_idx = -1
  while pre_idx >= 0:
    if first_NN == 0 and ts[pre_idx][1].startswith('NN'):
      end_idx = pre_idx + 1
      first_NN += 1
    elif first_NN == 1 and ts[pre_idx][1].startswith('NN') == False and ts[pre_idx][1].startswith('JJ') == False:
      start_idx = pre_idx - 1
      break
    pre_idx -= 1
    
  if end_idx == -1: return None
  k = start_idx - 1
  while k >= 0:
    if ts[k][1].startswith('VB'):
      return [ts[k], ts[start_idx:end_idx]]
    k -= 1
  return ts[start_idx:end_idx]
      
