from deterministic_lp_solver import *
from exhaustive_solver import *
from rand_lp_solver import *
from greedy_solver import *
from parse_input import parse_file

import numpy as np

def average_solve(filename):
  '''Input: filename - name of the file in the 'input/' directory.
  Output: VARDICT - a dict with one set of optimal assignments.
  ''' 
  x = np.random.uniform()
  if (x <= 1.0/3.0):
    return greedy_solve(filename)
  elif (x <= 2.0/3.0):
    return rand_lp_solve(filename)
  else:
    return det_solve(filename)