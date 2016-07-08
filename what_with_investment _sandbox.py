def for_NN_investment(ts, s):
  key_start = 'investment'
  key_start_idx = -1
  followers = ['opportuni', 'purpose']
  
  if key_start in s:
    for i in range(len(ts)):
      if ts[i][0].startswith(key_start):
        key_start_idx = i
        break
        
  if key_start_idx != -1:
    for f in followers:
      if ts[i+1][0].startswith(f):
        return None
      
      flag_ct = 0
      order = 0
      pre_idx = key_start_idx - 1
      combination_start_idx = -1
      while pre_idx >= 0:
        if order == 0 and ts[pre_idx][1].startswith('NN'):
          flag_ct += 1
          order += 1
        # nearest 'for'
        elif order == 1 and ts[pre_idx][1].startswith('for'):
          combination_start_idx = pre_idx
          flag_ct += 1
          order += 1
        elif order == 2 and (ts[pre_idx][1].startswith('.') or ts[pre_idx][1].startswith('CC') or pre_idx == 0):
          flag_ct += 1
          order += 1
        if flag_ct == 3:
          return ts[combination_start_idx:key_start_idx+1]
        
        pre_idx -= 1
        
  return None
