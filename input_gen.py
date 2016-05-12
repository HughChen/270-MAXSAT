from sat_gen import *
import csv
import numpy as np

import random

"""
Generate inputs for same parameters
Critical ratios for clause-to-variable I used:
  2SAT 2.4
  3SAT 5.2
  4SAT 10.7
  5SAT 21.8
  6SAT 44.0
"""

ratio = {2:2.4,\
    3: 5.2,\
    4: 10.7,\
    5: 21.8,\
    6: 44.0 }

for k in xrange(2,7):
  for i in range(0,3000):
    num_clause = random.randint(100,1000)
    try:
      num_vars = random.randint(int(np.log2(num_clause) + 2),int(num_clause/ratio[k]))
    except:
      num_vars = int(np.log2(num_clause)) + 2
    random_input('train/' + str(k) + 'SAT' + str(i) + '.in',k,num_clause,num_vars)

"""
Generate varying variables and clause numbers:
"""
# l = []

# for i in range(1,51):
#   for j in range(1,11):
#     random_input('3SAT_varied/iter5/' + str(i) + '_' + str(j) + '.in',3,i,j)
    # l.append([str(i), str(j)])

# with open('input/' + '3SAT_varied/' + "parameters.csv", "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(l)
