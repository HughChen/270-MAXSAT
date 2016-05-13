import glob
import random
import numpy as np
from sklearn.neural_network import MLPClassifier
import pickle

import parse_input 
import eval_sat 
import rand_lp_solver 
import greedy_solver 
import deterministic_lp_solver 

PATH = 'input/'

def featurize(input_file,var_dim=100,clause_dim=1000):
  '''Make sure input_file is rectangular. That means k must be constant for every clause'''
  global VARDICT,clauses,variables
  VARDICT,clauses = parse_input.parse_file(input_file)
  
  variables = VARDICT.keys()
  variables.sort()




  # matrix1 is a graph of variables and the edges indicate the number
  # of clauses two variables are in with one another
  global matrix1
  matrix1 = np.array([[0] * len(variables)] * len(variables))

  for i in xrange(len(clauses)):
    clause = clauses[i]
    split_clause = clause[2:-2].split(' or ')
    v_in_clause = set()
    for lit in split_clause:
      _,var = greedy_solver.var_from_lit(lit)
      v_in_clause.add(var)
    var = list(v_in_clause)
    for v in var:
      for w in var:
        if v != w:
          vidx = variables.index(v)
          widx = variables.index(w)
          matrix1[vidx][widx] += 1
  u1,s1,v1 = np.linalg.svd(matrix1)
  if len(s1) < var_dim:
    s1 = np.concatenate((s1,[0] * (var_dim-len(s1))))
  


  # matrix2 is a graph in which the vertices are clauses and edges are the number of
  # literals two clauses share in common with one another.
  global matrix2
  matrix2 = np.array([[0] * len(clauses)] * len(clauses))
  
  for i in xrange(len(clauses)):
    clause1 = clauses[i]
    split_clause1 = clause1[2:-2].split(' or ')
    for j in xrange(len(clauses)):
      if i == j:
        continue
      clause2 = clauses[j]
      split_clause2 = clause2[2:-2].split(' or ')
      match = sum(map(lambda elem,li: elem in li, split_clause1, [split_clause2] * len(split_clause1)))
      if match:
        matrix2[i][j] += match
  u2,s2,v2 = np.linalg.svd(matrix2)
  if len(s2) < clause_dim:
    s2 = np.concatenate((s2,[0] * (clause_dim-len(s2))))

  return np.concatenate((s1,s2))

def find_opt(input_file):
  '''Returns (greedy score,random_lp_score,det_lp_score)'''
  _,clauses = parse_input.parse_file(input_file)
  greedy_VARDICT  = greedy_solver.greedy_solve(input_file)
  print 'greedy'
  rand_VARDICT    = rand_lp_solver.rand_solve(input_file)
  print 'random'
  lp_rand_VARDICT,lpres = rand_lp_solver.lp_solve(input_file,True)
  print 'lp'
  det_lp_VARDICT  = deterministic_lp_solver.det_solve(input_file,lpres)
  print 'det lp'

  greedy_score = eval_sat.eval_input(greedy_VARDICT,clauses)
  rand_score = eval_sat.eval_input(rand_VARDICT,clauses)
  lp_rand_score = eval_sat.eval_input(lp_rand_VARDICT,clauses)
  det_lp_score = eval_sat.eval_input(det_lp_VARDICT,clauses)

  rand_alg_score = np.average((rand_score,lp_rand_score))

  scores = np.array([greedy_score,rand_alg_score,det_lp_score],dtype=float)
  print scores
  scores = (scores-min(scores))
  scores = (scores/max(scores) - .5) * 2

  scores = (scores == max(scores))
  scores = scores/sum(scores)
  scores = np.cumsum(scores)

  p = random.random()

  for i in xrange(len(scores)):
    if p < scores[i]:
      return i
  return np.argmax(scores)

def get_samples(loc,files='*'):
  ifiles = glob.iglob(PATH + loc + '/' + files)
  features = []
  labels = []
  ctr = 1
  for f in ifiles:
    print f
    f = f[len(PATH):]
    print f
    try:
      feat_f = featurize(f)
    except:
      print f
      return None,None
    label_f = find_opt(f)
    features.append(feat_f)
    labels.append(label_f)
    if ctr % 100 == 0:
      np.save(PATH + 'features',features)
      np.save(PATH + 'labels',labels)
    ctr += 1
  return features,labels

def learn(features,labels):
  clf = MLPClassifier()
  clf.fit(features,labels)
  return clf
