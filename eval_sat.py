def eval_clause(VARDICT,sclause):
  '''Input: sclause - split clause excluding the parenthesis.
  VARDICT - a dictionary with unique keys equal to literals.
  Output: boolean evaluating the clause.
  '''
  if (not sclause):
    return True
  if (sclause[0] == 'or'):
    return eval_clause(VARDICT,sclause[1:])
  if (sclause[0] == 'not'):
    return not eval(sclause[1]) and eval_clause(VARDICT,sclause[2:])
  else:
    return eval(sclause[0]) and eval_clause(VARDICT,sclause[2:])

def eval_input(VARDICT,clauses):
  '''Input: VARDICT - a dictionary with unique keys equal to literals.
  clauses - a list of strings that are inputs to the eval() function.
  Output: num_true - number of clauses that evaluate to be true
  '''
  num_true = 0
  for clause in clauses:
    split_clause = clause.split(' ')
    split_clause = split_clause[1:-1]
    if (eval_clause(VARDICT,split_clause)):
      num_true += 1
  return num_true