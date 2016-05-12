import random

PATH = 'input/'

def random_input(file_name,k,m,n=None):
  '''k is the number of literals per clause, n is the number of clauses'''
  if n is None:
    n = m
  
  variables = [''] * n
  for i in xrange(n):
    variables[i] = str(i)

  with open(PATH + file_name,'w') as f:
    for i in xrange(m):
      random.shuffle(variables)
      chosen = variables[:k]

      for var in chosen:
        neg = random.random() > .5
        if neg:
          f.write('!')
        f.write(var)
        if var == chosen[-1]:
          f.write('\n')
        else:
          f.write(',')
