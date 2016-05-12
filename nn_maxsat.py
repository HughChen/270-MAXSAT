import numpy as np
from sklearn.neural_network import MLPClassifier

import parse_input 
import eval_sat 
import rand_lp_solver 
import greedy_solver 
import deterministic_lp_solver 

def featurize(input_file):
  VARDICT,clauses = parse_input.parse_file(input_file)
  
  variables = VARDICT.keys()
  variables.sort()

  matrix = np.array([[0] * len(variables)] * len(variables))

  return matrix
