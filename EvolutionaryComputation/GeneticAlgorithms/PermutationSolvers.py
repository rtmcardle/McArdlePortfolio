from geneal.genetic_algorithms.genetic_algorithm_base import GenAlgSolver
from geneal.utils.helpers import get_elapsed_time
import numpy as np
import math
import datetime
import logging
import matplotlib.pyplot as plt



class PermutationSolver(GenAlgSolver):
    """
    A class based upon GeneAl package customized to solve 
    evolutionary problems using a permutation representation.
    """
    
    def initialize_population(self):
        """
        Initializes the population of the problem according to the
        population size and number of genes. Outputs individuals
        which are permutations of [0,n_genes].
        :return: a numpy array with a randomized initial population
        """

        population_array = [np.random.permutation(self.n_genes) for _ in range(self.pop_size)]

        return np.array(population_array)


    def create_offspring(self,first_parent, sec_parent, crossover_pt, _):
        """
        Creates offspring from the two parents and a crossover
        point. Uses a "cut-and-crossfil" method.

        :param first_parent: first parent's chromosome
        :param sec_parent: second parent's chromosome
        :param crossover_pt: point(s) at which to perform the crossover
        :param offspring_number: whether it's the first or second offspring from a pair of parents.
        Important if there's different logic to be applied to each case.
        :return: the resulting offspring.
        """
        child_first = first_parent[:crossover_pt[0]]
        child_second = []
        for i in range(self.n_genes):
            index = (crossover_pt[0]+i) % self.n_genes
            gene = sec_parent[index]
            if gene not in child_first:
                child_second.append(gene)

        child_second = np.array(child_second)

        return np.hstack((child_first,child_second))


    def get_number_mutations(self):
        return math.ceil((self.pop_size - 1) * self.mutation_rate)


    def solve(self,optimum_fit):
        """
        Performs the genetic algorithm optimization according to the parameters
        provided at initialization.

        :param optimum_fit: a breaking point fitness for the optimization
        :return: None
        """

        start_time = datetime.datetime.now()

        self.solved = True

        mean_fitness = np.ndarray(shape=(1, 0))
        max_fitness = np.ndarray(shape=(1, 0))

        # initialize the population
        population = self.initialize_population()

        fitness = self.calculate_fitness(population)

        fitness, population = self.sort_by_fitness(fitness, population)

        gen_interval = max(round(self.max_gen / 100), 1)

        gen_n = 0
        while True:

            gen_n += 1

            if self.verbose and gen_n % gen_interval == 0:
                logging.info(f"Iteration: {gen_n}")
                logging.info(f"Best fitness: {fitness[0]}")
                logging.info(f"Mean fitness: {fitness.mean()}")

            mean_fitness = np.append(mean_fitness, fitness.mean())
            max_fitness = np.append(max_fitness, fitness[0])

            if max_fitness[-1] >= optimum_fit:
                print("Optimum Solution Found.")
                #gen_n -= 1
                break

            ma, pa = self.select_parents(fitness)

            ix = np.arange(0, self.pop_size - self.pop_keep - 1, 2)

            xp = np.array(
                list(map(lambda _: self.get_crossover_points(), range(self.n_matings)))
            )

            for i in range(xp.shape[0]):

                # create first offspring
                population[-1 - ix[i], :] = self.create_offspring(
                    population[ma[i], :], population[pa[i], :], xp[i], "first"
                )

                # create second offspring
                population[-1 - ix[i] - 1, :] = self.create_offspring(
                    population[pa[i], :], population[ma[i], :], xp[i], "second"
                )

            population = self.mutate_population(population, self.n_mutations)

            fitness = np.hstack((fitness[0], self.calculate_fitness(population[1:, :])))

            fitness, population = self.sort_by_fitness(fitness, population)

            if gen_n >= self.max_gen:
                self.solved = False
                break

        self.generations_ = gen_n
        self.best_individual_ = population[0, :]
        self.best_fitness_ = fitness[0]
        self.population_ = population
        self.fitness_ = fitness


        if self.show_stats:
            end_time = datetime.datetime.now()

            time_str = get_elapsed_time(start_time, end_time)

            self.print_stats(time_str)
        
        if self.plot_results:
            self.plot_fitness_results(mean_fitness, max_fitness, gen_n)


    def print_stats(self, time_str):
        """
        Prints the statistics of the optimization run

        :param time_str: time string given by the method get_elapsed_time
        :return: None
        """
        with open('log.txt', 'w') as f:
            f.write("\n#############################\n")
            f.write("#\t\t\tSTATS\t\t\t#\n")
            f.write("#############################\n\n")
            f.write(f"Total running time: {time_str}\n\n")
            f.write(f"Population size: {self.pop_size}\n")
            f.write(f"Number variables: {self.n_genes}\n")
            f.write(f"Selection rate: {self.selection_rate}\n")
            f.write(f"Mutation rate: {self.mutation_rate}\n")
            f.write(f"Number Generations: {self.generations_}\n")
            f.write(f"Best fitness: {self.best_fitness_}\n")
            f.write(f"Best individual: {self.best_individual_}\n")
        

        logging.info("\n#############################")
        logging.info("#\t\t\tSTATS\t\t\t#")
        logging.info("#############################\n\n")
        logging.info(f"Total running time: {time_str}\n\n")
        logging.info(f"Population size: {self.pop_size}")
        logging.info(f"Number variables: {self.n_genes}")
        logging.info(f"Selection rate: {self.selection_rate}")
        logging.info(f"Mutation rate: {self.mutation_rate}")
        logging.info(f"Number Generations: {self.generations_}\n")
        logging.info(f"Best fitness: {self.best_fitness_}")
        logging.info(f"Best individual: {self.best_individual_}")


    def plot_fitness_results(self,mean_fitness, max_fitness, iterations):
        """
        Plots the evolution of the mean and max fitness of the population.
        Exports a .png file of the plot.

        :param mean_fitness: mean fitness array for each generation
        :param max_fitness: max fitness array for each generation
        :param iterations: total number of generations
        :return: None
        """

        plt.figure(figsize=(7, 7))

        x = np.arange(1, iterations + 1)

        plt.plot(x, mean_fitness, label="mean fitness")
        plt.plot(x, max_fitness, label="max fitness")

        plt.legend()
        plt.savefig('fitness_results.png')
        #plt.show()


class QueensSolver(PermutationSolver):
    """
    Class to solve the N-Queens problem.
    """

    def mutate_population(self, population, n_mutations):
        """
        Mutates the population by randomly swapping two 
        elements of the permutation.

        :param population: the population at a given iteration
        :param n_mutations: number of mutations to be performed.
        :return: the mutated population
        """

        mutation_rows = np.random.choice(range(self.pop_size), n_mutations, replace=False)

        mutation_cols = np.random.choice(self.allowed_mutation_genes, n_mutations, replace=True)

        mutation_cols_2 = np.random.choice(self.allowed_mutation_genes, n_mutations, replace=True)

        
        for i in range(n_mutations):
            ## Ensures that two different genes are selected for swapping
            while mutation_cols_2[i] == mutation_cols[i]:
                mutation_cols_2[i] = np.random.choice(self.allowed_mutation_genes)
                
            ## For each ind. selected to mutate, swap two genes
            swap_1 = population[mutation_rows[i]][mutation_cols[i]]
            swap_2 = population[mutation_rows[i]][mutation_cols_2[i]]

            population[mutation_rows[i]][mutation_cols[i]] = swap_2
            population[mutation_rows[i]][mutation_cols_2[i]] = swap_1

        return population


class TSPSolver(PermutationSolver):
    """Class to solve the Traveling Salesperson Problem."""

    def mutate_population(self, population, n_mutations):
        """
        Mutates the population by randomizing specific positions of the
        population individuals.

        :param population: the population at a given iteration
        :param n_mutations: number of mutations to be performed.
        :return: the mutated population
        """

        mutation_type = np.random.uniform()

        ##Neighbor-swap mutation 30% of the time
        if mutation_type >= .3: 

            mutation_rows = np.random.choice(range(self.pop_size), n_mutations, replace=False)

            mutation_cols = np.random.choice(self.allowed_mutation_genes, n_mutations, replace=True)
        

            for i in range(n_mutations):           
                ## For each ind. selected to mutate, swap with its neighbor
                swap_1 = population[mutation_rows[i]][mutation_cols[i]]
                swap_2 = population[mutation_rows[i]][(mutation_cols[i] + 1) % self.n_genes]

                population[mutation_rows[i]][mutation_cols[i]] = swap_2
                population[mutation_rows[i]][(mutation_cols[i] + 1) % self.n_genes] = swap_1
        
        ## Random-swap mutation 70% of the time
        else: 
            mutation_rows = np.random.choice(range(self.pop_size), n_mutations, replace=False)

            mutation_cols = np.random.choice(self.allowed_mutation_genes, n_mutations, replace=True)

            mutation_cols_2 = np.random.choice(self.allowed_mutation_genes, n_mutations, replace=True)

            for i in range(n_mutations):
                ### Ensures that two different genes are selected for swapping
                while mutation_cols_2[i] == mutation_cols[i]:
                    mutation_cols_2[i] = np.random.choice(self.allowed_mutation_genes)
                
                ## For each pair of ind. selected to mutate, swap their genes
                swap_1 = population[mutation_rows[i]][mutation_cols[i]]
                swap_2 = population[mutation_rows[i]][mutation_cols_2[i]]

                population[mutation_rows[i]][mutation_cols[i]] = swap_2
                population[mutation_rows[i]][mutation_cols_2[i]] = swap_1

        return population

   