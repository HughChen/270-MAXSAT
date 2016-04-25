import re

input_file_location = 'input/'

def parse_line(line,variables):
  try:
    lits = re.split(',',line)
    s = []
    for lit in lits:
      ss = ''
      while lit[0] == '!':
        ss += 'not '
        lit = lit[1:]
      s.append(ss + 'VARDICT[\'' + lit + '\']')
      if lit not in variables:
        variables[lit] = True
    join = lambda l1,l2: l1 + ' or ' + l2
    return '( ' + reduce(join,s) + ' )'
  except:
    pass


def parse_input(filename,loc=input_file_location):
  '''Input: name of the file in the 'input/' directory.
  Output: a tuple of (VARDICT,clauses).
  VARDICT is a dictionary with unique keys equal to literals.
  clauses is a list of strings that are inputs to the eval() function.
  '''
  global VARDICT,clauses
  filename = loc + filename
  clauses = list()
  VARDICT = dict()
  try:
    with open(filename,'r') as f:
      for line in f:
        clauses.append(parse_line(line[:-1],VARDICT))
  except IOError:
    print(filename,'is not found!')

  return (VARDICT,clauses)

def eval_clause(clause):
  '''Input: clause - split clause excluding the parenthesis.
  Output: boolean evaluating the clause.
  '''
  if (not clause):
    return True
  if (clause[0] == 'or'):
    return eval_clause(clause[1:])
  if (clause[0] == 'not'):
    return not eval(clause[1]) and eval_clause(clause[2:])
  else:
    return eval(clause[0]) and eval_clause(clause[2:])

def eval_input():
  '''Input: none.  Uses the globally defined variables.
  Output: number of clauses that evaluate to be true
  '''
  num_true = 0
  for clause in clauses:
    split_clause = clause.split(' ')
    split_clause = split_clause[1:-1]
    if (eval_clause(split_clause)):
      num_true += 1
  return num_true