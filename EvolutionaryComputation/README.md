# Evolutionary Computation
This section showcases various genetic and evolutionary approaches to design and problem solving. 

## [Boid Evolution][BoidEvolution/]
This directory showcases a term project for an Evolutionary Computation course. The object was to use classifiers that had previously been trained to recognize human perception of various swarm behaviors associated with flocking in order to optimize boid parameters that would effectively mimic real-world flocking behaviors. Both evolutionary strategy and genetic evolution approaches are applied and results are compared and analyzed. The fitness functions for this evolution utilize a boid simulation which required considerable optimization in order to operate at the necessary scale (tens of thousands of fitness evaluations, each of which simulate 200 boids for 150 frames).

##[Evolutionary Strategies](EvolutionaryStrategies/)
This directory showcases the use of evolutionary strategies to find optimal solutions for very complex and rugged multidimensional equations, including Ackley's Function for 30 dimensions. Included are the record for ten runs, plots for the average and minimum fitness over time for each run, and a summary the ten runs, including the best individuals found for each of the runs. 

##[Genetic Algorithms](GeneticAlgorithms/)
This directory showcases the use of genetic algorithms to solve both the N-Queens and the Traveling Salesperson permutation problems. Included are runs for various values of N, including both plots of mean and maximum fitness over time, as well as logs which record the best individuals found and the number of iterations/evaluations needed.
