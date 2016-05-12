import numpy as np
from sklearn.neural_network import MLPClassifier

import parse_input 
import eval_sat 
import rand_lp_solver 
import greedy_solver 
import deterministic_lp_solver 

def featurize(input_file):
  '''Make sure input_file is rectangular. That means k must be constant for every clause'''
  VARDICT,clauses = parse_input.parse_file(input_file)
  
  variables = VARDICT.keys()
  variables.sort()

  matrix = np.array([[0] * len(variables)] * len(variables))

  for i in xrange(len(clauses)):
    clause = clauses[i]
    split_clause = clause[2:-2].split(' or ')
    v_in_clause = set()
    for lit in split_clause:
      _,var = greedy_solver.var_from_lit(lit)
      v_in_clause.add(var)
    var = list(var)
    for v in var:
      for w in var:
        if v != w:
          vidx = variables.index(v)
          widx = variables.index(w)
          matrix[v][w] += 1

  return matrix
