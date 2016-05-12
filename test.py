# Preliminary testing script
from deterministic_lp_solver import *
from exhaustive_solver import *
from rand_lp_solver import *
from average_solver import *
from greedy_solver import *

import parse_input
import eval_sat
import time

fname = '4.in'
(_,clauses) = parse_input.parse_file(fname)
# for clause in clauses:
#   print clause

# Evaluate exhaustive_solve
start_time = time.time()
(num_true, opt_dict) = exhaustive_solve(fname)
opt_time = time.time() - start_time
print 'exhaustive_solve'
print opt_dict
print num_true
print("%s seconds" % opt_time)

# Evaluate greedy_solve
start_time = time.time()
greedy_dict = greedy_solve(fname)
greedy_time = time.time() - start_time
print 'greedy_solve'
print greedy_dict
print eval_input(greedy_dict, clauses)
print("%s seconds" % greedy_time)

# Evaluate rand_lp_solve
start_time = time.time()
rand_lp_dict = rand_lp_solve(fname)
rand_lp_time = time.time() - start_time
print 'rand_lp_solve'
print rand_lp_dict
print eval_input(rand_lp_dict, clauses)
print("%s seconds" % rand_lp_time)

# Evaluate det_solve
start_time = time.time()
det_dict = det_solve(fname)
det_time = time.time() - start_time
print 'det_solve'
print det_dict
print eval_input(det_dict, clauses)
print("%s seconds" % det_time)

# Evaluate avg_solve
start_time = time.time()
avg_dict = average_solve(fname)
avg_time = time.time() - start_time
print 'avg_solve'
print avg_dict
print eval_input(avg_dict, clauses)
print("%s seconds" % avg_time)