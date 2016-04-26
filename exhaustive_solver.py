from parse_input import parse_file
from eval_sat import eval_input
from itertools import combinations

def exhaustive_solver(filename):
  '''Input: filename - name of the file in the 'input/' directory.
  Output: a tuple of (max_true,best_combo).
  max_true - the optimal number of satisfied clauses.
  best_combo - a dict with one set of optimal assignments.
  ''' 
  # Load clauses
  (VARDICT,clauses) = parse_file(filename)
  
  # Implement the basic exponential exhaustive search
  keys = list(VARDICT.keys())
  combos = sum([map(list, combinations(keys, i)) for i in range(len(keys) + 1)], [])

  # Iterate through the combinations
  max_true = 0
  max_combo = None
  for combo in combos:
    for key in keys:
      VARDICT[key] = False
    for key in combo:
      VARDICT[key] = True
    num_true = eval_input(VARDICT,clauses)
    if (num_true > max_true):
      max_true = num_true
      max_combo = dict(VARDICT)
  return (max_true, max_combo)