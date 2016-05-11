from parse_input import parse_file
from eval_sat import eval_input
from scipy.optimize import linprog

import random

import numpy as np

def lp_solve(filename):
  '''Input: filename - name of the file in the 'input/' directory.
  Output: stores LP assignment in VARDICT
  ''' 
  # Load clauses
  global VARDICT
  (VARDICT,clauses) = parse_file(filename)
  keys = list(VARDICT.keys())

  # Construct the LP
  num_cls = len(clauses)
  num_var = len(keys)
  c = -np.append(np.ones(num_cls), np.zeros(num_var))
  A = np.zeros((num_cls,num_cls+num_var))
  b = np.zeros(num_cls)
  
  for i in range(0,len(clauses)):
    split_clause = clauses[i][2:-2].split(' or ')
    A[i,i] = 1
    for j in range(0,len(split_clause)):
      col = num_cls + keys.index(split_clause[j][-3])
      if 'not' in split_clause[j]:
          b[i] += 1
          A[i,col] = 1
      else:
          A[i,col] = -1
  res = linprog(c, A_ub=A, b_ub=b, bounds=(0, 1)) 

  rround = lambda p: True if random.random() < p else False
  x = np.array(map(rround,res['x']))
  x = x[-num_var:]

  idx = 0
  for k in keys:
    VARDICT[k] = x[idx]
    idx += 1

def rand_solve(filename):
  '''Input: filename - name of the file in the 'input/' directory.
  Output: stores uniform random assignment in VARDICT
  ''' 
  global VARDICT
  (VARDICT,clauses) = parse_file(filename)
  randbin = lambda: True if random.randint(0,1) == 1 else False
  for k in VARDICT.keys():
    VARDICT[k] = randbin()

def rand_lp_solve(filename):
  '''Input: filename - name of the file in the 'input/' directory.
  Output: VARDICT - greater than 3/4 expected value approximation assignment
  ''' 
  coin = random.randint(0,1)
  if coin == 1:
    lp_solve(filename)
  else:
    rand_solve(filename)
  return VARDICT



