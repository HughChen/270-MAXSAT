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

  return file_name


def generate_even_split(file_name,k,n,rep=1):
  '''Generates an example where each variable occurs as nonnegated exactly
  half the number of the times it shows up at all.'''
  while (k*n)%(2*rep) != 0:
    n += 1
  
  num_vars = k*n / (2*rep)
  var_list1 = map(str,xrange(num_vars))
  var_list2 = map(lambda a: '!' + str(a),xrange(num_vars))
  var_list = (var_list1 + var_list2) * rep

  random.shuffle(var_list)

  out = ''
  for i in xrange(n):
    out += reduce(lambda a,b: a+b, map(lambda a: a + ',', var_list[i*k:(i+1)*k]))
    out = out[:-1] + '\n'

  with open(PATH + file_name,'w') as f:
    f.write(out)

  return file_name
