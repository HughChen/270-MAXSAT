from parse_input import parse_file
from eval_sat import eval_input
from scipy.optimize import linprog

import random

import numpy as np

def lp_solve(input_file):
  # Load clauses
  global VARDICT
  (VARDICT,clauses) = parse_file(input_file)
  keys = list(VARDICT.keys())
  keys.sort()

  # Construct the LP

  # >>> A = [[-3, 1], [1, 2]]
  # >>> b = [6, 4]
  # >>> x0_bounds = (None, None)
  # >>> x1_bounds = (-3, None)
  # >>> from scipy.optimize import linprog
  # >>> res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds),
  # ...               options={"disp": True})

  num_cls = len(clauses)
  num_var = len(VARDICT.keys())
  c = -np.append(np.ones(num_cls), np.zeros(num_var))
  A = np.zeros((num_cls,num_cls+num_var))
  b = np.zeros(num_cls)
  for i in range(0,len(clauses)):
    split_clause = clauses[i][2:-2].split(' or ')
    A[i,i] = 1
    print split_clause
    for j in range(0,len(split_clause)):
      col = num_cls + keys.index(split_clause[j][-3])
      if 'not' in split_clause[j]:
          b[i] += 1
          A[i,col] = 1
      else:
          A[i,col] = -1
  res = linprog(c, A_ub=A, b_ub=b, bounds=(0, 1), options={"disp": True})

  rround = lambda p: 1 if random.random() < p else 0
  x = np.array(map(rround,res['x']))
  print res['x']
  print x
  x = x[-num_var:]
  
  idx = 0
  for k in keys:
    VARDICT[k] = x[idx]
    idx += 1


