from parse_input import parse_file
from eval_sat import *
from scipy.optimize import linprog

import random

import numpy as np

def lp_solve(filename):
  '''Input: filename - name of the file in the 'input/' directory.
  Output: returns the solution to the LP
  ''' 
  # Load clauses
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
      var = split_clause[j].split("'")[1]
      col = num_cls + keys.index(var)
      if 'not' in split_clause[j]:
          b[i] += 1
          A[i,col] = 1
      else:
          A[i,col] = -1
  res = linprog(c, A_ub=A, b_ub=b, bounds=(0, 1))
  return res['x'][-num_var:]

def eval_sub_clause(VARDICT,sclause):
  '''Input: sclause - split clause excluding the parenthesis.
  assign_dict - a dictionary with unique keys equal to literals,
    may be a subset of the variables in the clauses.
  Output: boolean evaluating the clause.
  '''
  if (not sclause):
    return False
  if (sclause[0] == 'not'):
    var = sclause[1].split("'")[1]
    if (var in VARDICT.keys()):
      return (not eval(sclause[1])) or eval_sub_clause(VARDICT,sclause[2:])
    else:
      return eval_sub_clause(VARDICT,sclause[2:])
  else:
    var = sclause[0].split("'")[1]
    if (var in VARDICT.keys()):
      return eval(sclause[0]) or eval_sub_clause(VARDICT,sclause[1:])
    else:
      return eval_sub_clause(VARDICT,sclause[1:])

def det_solve(filename):
  '''Input: filename - name of the file in the 'input/' directory.
  Output: assigned_vars - greater than 3/4 assignment (deterministic)
  '''
  global VARDICT
  (VARDICT,clauses) = parse_file(filename)
  assigned_vars = {}
  keys = VARDICT.keys()
  # Go through and assign each variable
  q = lp_solve(filename)
  for i in range(0,len(keys)):
    print i
    curr_x = keys[i]
    unsat_clauses = []

    # Get unsatisfied clauses
    for clause in clauses:
      sclause = clause.split(' ')
      sclause = filter(lambda x: x != 'or', sclause[1:-1])
      if (not eval_sub_clause(assigned_vars, sclause)):
        unsat_clauses.append(clause)

    # Increment appropriate variables
    w_i, w_i_bar, f_i, f_i_bar = 0, 0, 0, 0
    for clause in unsat_clauses:
      string_literals = clause.split(' ')
      string_literals = filter(lambda x: x != 'or', string_literals[1:-1])
      string_literals = map(lambda x: x.split("'")[1] if 'VARDICT' in x else x, string_literals)
      # Check for x_i
      if (keys[i] in string_literals):
        curr_index = string_literals.index(keys[i])
        # Negated x_i 
        if (curr_index != 0 and string_literals[curr_index - 1] == 'not'):
          is_f = False
          # Check for x_{i+1}, ..., x_n
          for j in range(i+1,len(keys)):
            if (keys[j] in string_literals):
              is_f = True
          if (is_f):
            f_i_bar += 1
          else:
            w_i_bar += 1
        # Normal x_i
        else:
          is_f = False
          # Check for x_{i+1}, ..., x_n
          for j in range(i+1,len(keys)):
            if (keys[j] in string_literals):
              is_f = True
          if (is_f):
            f_i += 1
          else:
            w_i += 1

    # Calculate alpha
    num = w_i + f_i + w_i_bar
    den = f_i + f_i_bar
    if (den == 0):
      if (num >= 0):
        alpha = 1
      else:
        alpha = 0
    else:
      alpha = num/den

    # Deterministic Rounding (the order of these if statements matters)
    if (alpha >= 1):
      assigned_vars[keys[i]] = True
    elif (alpha <= 0):
      assigned_vars[keys[i]] = False
    elif (q[i] >= (1-alpha)/(2*alpha)):
      assigned_vars[keys[i]] = True
    elif (q[i] < (1-alpha)/(2*alpha)):
      assigned_vars[keys[i]] = False
  return assigned_vars

