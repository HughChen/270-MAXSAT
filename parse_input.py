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
