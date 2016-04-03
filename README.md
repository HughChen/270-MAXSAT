# 270MAXSAT420
MAXSAT project for CS270.

## Project Proposal
In our project, we’ll focus on further exploring topics in class that grabbed our interest.
In addition, we will try to implement some of the algorithms and evaluate their performance.

## Background
Topics of interest:
* Randomized algorithms

## Objectives
Investigate MAX2SAT
* Implement using randomized approach (taking note of variance)
* Investigate derandomizing using method of conditional expectations
* Investigate whether there are any alternative methods for solving MAX2SAT

## Descriptions
MAXSAT
Our research topic of interest is the various algorithms used to solve the maximum satisfiability (MAXSAT) problem.
First, we would like to implement the 3/4-approximate algorithm from homework 2.
Specifically, we would like to find an empirical estimate of the variance in the results of this algorithm in practice.
Next, we have found several other deterministic algorithms which give 2/3-approximations
(greedy approximation algorithm) and 3/4-approximations (LP relaxation with a potential function) to this problem,
and plan to implement those algorithms and see the results for the variance. 

In addition to this, we want to see if there is a reasonable way for us to derandomize the 3/4-approximation
randomized algorithm as done in homework 2.
By looking at the performance of these algorithms, it’s possible to see where their strengths lie in performance.
That is, if having a 2/3-approximation is crucial but anything more doesn’t really add much benefits,
using an algorithm that gives a 2/3-approximation with small variance might be better than an
algorithm which gives 3/4-approximations but high variance.

Two papers on MAXSAT approximation algorithms:
[3/4-approx. deterministic algorithm](https://people.mpi-inf.mpg.de/~anke/WAOA11_vanZuylen.pdf)  
[2/3-approx. deterministic algorithm](http://www.sciencedirect.com/science/article/pii/S0022000074800449)

