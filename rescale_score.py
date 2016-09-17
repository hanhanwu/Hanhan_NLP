def rescale_score(score, mins, maxs, small_is_better=0):
  v = 0.00001  # avoid to be divided by 0
  if small_is_better:
    new_score = float(mins)/max(score, v)
  else:
    if maxs == 0: maxs = v
    new_score = float(score)/maxs
  return new_score
