# Preliminary testing script
from rand_lp_solver import *
from exhaustive_solver import *
from deterministic_lp_solver import *
import parse_input
import eval_sat

fname = '1.in'
(_,clauses) = parse_input.parse_file(fname)

# Evaluate exhaustive_solve
(num_true, opt_dict) = exhaustive_solve(fname)
print 'exhaustive_solve'
print opt_dict
print num_true

# Evaluate rand_lp_solve
rand_lp_dict = rand_lp_solve(fname)
print 'rand_lp_solve'
print rand_lp_dict
print eval_input(rand_lp_dict, clauses)

# Evaluate det_solve
det_dict = det_solve(fname)
print 'det_solve'
print det_dict
print eval_input(det_dict, clauses)
