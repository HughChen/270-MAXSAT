from sat_gen import *
import csv

"""
Generate inputs for same parameters
Critical ratios for clause-to-variable I used:
  2SAT 2.4
  3SAT 5.2
  4SAT 10.7
  5SAT 21.8
  6SAT 44.0
"""
k = 6
for i in range(0,100):
  random_input(str(k) + 'SAT/' + str(i) + '.in',k,440,10)

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