################################################################
##	Ryan McArdle
##  1 Oct.  2020
##
##  Implements two kinds of genetic algorithm optimizers based 
##  upon the GeneAl library in order to solve the N-Queens and 
##  the Traveling Salesperson problems. Requires the classes 
##  defined in PermutationSolvers.py. 
##
################################################################

from PermutationSolvers import QueensSolver,TSPSolver
import math


def fit_nqueens(individual):
	"""
	Counts the number of conflicting queens (avoids double 
	counts) and returns the negative number. The package geneal
	maximizes fitness, so we must negate.

	:param individual: the individual for whom fitness is 
	evaluated
	"""

	conflicts = 0
	for i in range(len(individual)):							## For each gene,
		for j in range(i+1,len(individual)):					## and each other gene not checked,
			if j-i == abs(individual[i]-individual[j]):			## if vert. diff. == horiz. dist. for queens,
				conflicts += 1									## increase conflict count
	return -conflicts											## and return the negation of the total.


def load_tsp(file):
	"""
	Loads the node position data for TSP.

	:param file: the location of the data file
	"""

	data = {}
	with open(file, 'r') as f:
		file = f.readlines()[2:]
		for line in file:
			node,x,y = line.split()
			data[int(node)-1] = (int(x),int(y))
	return data


def fit_tsp(individual):
	"""
	Counts the total distance for the circuit defined by the 
	permutation for TSP. Geneal maximizes fitness, so we must
	negate the distance.

	:param individual: the individual for whom fitness is 
	evaluated
	"""

	data = load_tsp('TSPDATA.txt')
	length = len(individual)
	dist = 0
	for i in range(length):								## For each gene,
		first = individual[i]							## identify the node for that gene
		second = individual[(i+1) % length]				## and the next node that is visited,
		dist += euc_dist(data[first],data[second])		## and add the distance separating them to the total distance. 
	return -dist


def euc_dist(first,second):
	"""
	Returns the Euclidean Distance between two tuples.

	:param first: the first tuple
	:param second: the second tuple
	"""

	return math.sqrt((first[0]-second[0])**2 + (first[1]-second[1])**2)



def solve_nqueens(n_queens, fit, pop, max_iter):
	solver = QueensSolver(
		n_genes = n_queens,
		pop_size = pop,
		fitness_function = fit,
		max_gen = max_iter//pop,
		mutation_rate = 0.15,
		selection_rate = 0.5,
		selection_strategy = 'tournament'
		)

	solver.solve(0)
	return

def solve_tsp(n_cities, fit, pop, max_iter):

	solver = TSPSolver(
		n_genes = n_cities,
		pop_size = pop,
		fitness_function = fit,
		max_gen = max_iter//pop,
		mutation_rate = 0.25,
		selection_rate = 0.25,
		selection_strategy = 'tournament'
		)

	solver.solve(0)
	return


if __name__=='__main__':
	#solve_nqueens(128,fit_nqueens,100,1000000)
	solve_tsp(127,fit_tsp,250,2500000)