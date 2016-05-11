from parse_input import parse_file
from eval_sat import eval_input

import numpy as np
import re

def p_or_n(key,clauses):
  '''Tells you if you should assign your variable p or n.
  (positive or negative)'''
  split_clause = lambda clause: clause[2:-2].split(' or ')
  find = lambda lit, clause: 1 if 'VARDICT[' + lit + ']' in clause else \
      (-1 if 'not VARDICT[' + lit + ']' in clause else 0)

def var_from_lit(literal):
  lit_re = re.match(r'(not )?VARDICT\[(.*)\]',literal)
  neg = lit_re.group(1)
  var = lit_re.group(2)
  return lit_re.group(1) is not None, var[1:-1]

def greedy_solve(input_file):
  # Load clauses
  global VARDICT,clauses
  (VARDICT,clauses) = parse_file(input_file)
  keys = list(VARDICT.keys())
  keys.sort()

  num_cls = len(clauses)
  num_var = len(VARDICT.keys())

  global sub,left,true,lit
  sub = set()
  true = {}
  left = set(clauses)
  lit = set(keys)

  while len(left) > 0 :
    counts = {}
    for i in range(0,len(list(left))):
      split_clause = list(left)[i][2:-2].split(' or ')
      for j in range(0,len(split_clause)):
        l = split_clause[j]
        if var_from_lit(l)[1] in lit:
          if l in counts:
            counts[l] += 1
          else:
            counts[l] = 1

    print counts
    lits = counts.keys()
    most = lits[np.argmax([counts[l] for l in lits])]
    
    left_copy = list(left)
    for i in range(0,len(left_copy)):
      split_clause = left_copy[i][2:-2].split(' or ')
      if most in split_clause:
        sub.add(clauses[i])
        left.remove(left_copy[i])

    neg,sym = var_from_lit(most)
    lit.remove(sym)
    VARDICT[sym] = neg

  return sub
