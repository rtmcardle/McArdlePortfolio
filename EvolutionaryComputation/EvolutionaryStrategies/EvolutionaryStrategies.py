###############################################################
##  Ryan McArdle
##  5 November 2020
##
##  Use evolutionary optimizations to solve for the optima to 
##  the provided equations. 
##
##  Code modified from the DEAP documentation at:
##  https://deap.readthedocs.io/en/master/index.html
##
###############################################################

from deap import creator, base, tools, algorithms
import numpy as np
import matplotlib.pyplot as plt
import random, array, math, os, datetime, textwrap


def initES(ind_cls, strg_cls, xmin, xmax, ymin, ymax, smin, smax):
    """
    An initializer to create individuals in order to minimize
    the function:
    f(x,y,a) = (|x|+|y|) · (1+|sin(a·|x|·pi)| + |sin(a·|y|·pi)|)
    """

    ind = ind_cls((np.random.uniform(xmin,xmax),np.random.uniform(ymin,ymax)))
    ind.strategy = strg_cls((np.random.uniform(smin,smax),np.random.uniform(smin,smax)))
    ind.xmin = xmin
    ind.xmax = xmax
    ind.ymin = ymin
    ind.ymax = ymax
    return ind

def initACK(ind_cls, strg_cls, dim, dmin, dmax, smin, smax):
    """
    An initializer to create individuals in order to minimize 
    Ackley's Function.
    """

    ind = ind_cls((np.random.uniform(dmin,dmax) for _ in range(dim)))
    ind.strategy = strg_cls((np.random.uniform(smin,smax) for _ in range(dim)))
    return ind


def evaluate1a(ind):
    """
    The fitness function for optimizing f(x,y,1)
    """

    t1 = abs(ind[0]) + abs(ind[1])
    t2 = 1 + abs(np.sin(abs(ind[0])*math.pi)) + abs(np.sin(abs(ind[1])*math.pi))
    return t1*t2,

def evaluate1b(ind):
    """
    The fitness function for optimizing f(x,y,3)
    """

    t1 = abs(ind[0]) + abs(ind[1])
    t2 = 1 + abs(np.sin(3*abs(ind[0])*math.pi)) + abs(np.sin(3*abs(ind[1])*math.pi))
    return t1*t2,

def evaluateAck(ind):
    """
    The fitness function for optimizing Ackley's function.
    """

    n = len(ind)
    listsq = [x**2 for x in ind]
    listcos = [math.cos(2*math.pi*x) for x in ind]
    t1 = -20*math.exp(-0.2*math.sqrt((1/n)*np.sum(listsq)))
    t2 = -math.exp((1/n)*np.sum(listcos))
    t3 = math.e + 20
    return t1+t2+t3,

def checkBounds(xmin, xmax, ymin, ymax):
    """
    A wrapper to correct for parameters that go outside of the 
    desired bounds.
    """

    def decorator(func):
        def wrapper(*args, **kargs):
            offspring = func(*args, **kargs)
            for child in offspring:
                if child[0] < xmin:
                    child[0] = xmin
                elif child[0] > xmax:
                    child[0] = xmax
                if child[1] < ymin:
                    child[1] = ymin
                elif child[1] > ymax:
                    child[1] = ymax
            return offspring
        return wrapper
    return decorator

def checkStrategy(minstrategy):
    """
    A wrapper to correct for strategy variables that go below
    a minimum value.
    """

    def decorator(func):
        def wrappper(*args, **kargs):
            children = func(*args, **kargs)
            for child in children:
                for i, s in enumerate(child.strategy):
                    if s < minstrategy:
                        child.strategy[i] = minstrategy
            return children
        return wrappper
    return decorator


def solve1a():
    """
    The function to solve for the optimum to f(x,y,1).
    """

    mu = 10
    lambda_ = 7 * mu
    CXPB = 0.75
    MUTPB = 0.5
    eval_limit = 2000

    xmin,xmax = -60,40
    ymin,ymax = -30,70
    smin, smax = 1e-3, 5.0

    toolbox = base.Toolbox()

    toolbox.register('individual', initES, creator.Individual, creator.Strategy, xmin, xmax, ymin, ymax, smin, smax)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxESBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutESLogNormal, c=0.01, indpb=0.25)
    toolbox.register('select', tools.selRandom)
    toolbox.register('evaluate', evaluate1a)

    toolbox.decorate('mate', checkBounds(xmin,xmax,ymin,ymax))
    toolbox.decorate('mutate', checkBounds(xmin,xmax,ymin,ymax))

    toolbox.decorate('mate', checkStrategy(smin))
    toolbox.decorate('mutate', checkStrategy(smin))

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    hof = tools.HallOfFame(1)

    pop = toolbox.population(n=mu)

    # Evaluate the entire population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # Record initial population
    g = 0
    record = stats.compile(pop)
    total_evals = mu
    logbook = tools.Logbook()
    logbook.header = 'gen','evals','min','max','avg','std'
    logbook.record(gen=0, evals=mu, **record)

    while True:
        if total_evals < (eval_limit - lambda_):
            g+=1
            # Select the next generation individuals
            offspring = toolbox.select(pop, lambda_)
            # Clone the selected individuals
            offspring = list(map(toolbox.clone, offspring))

            # Apply crossover and mutation on the offspring
            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < CXPB:
                    toolbox.mate(child1, child2)
                    del child1.fitness.values
                    del child2.fitness.values

            for mutant in offspring:
                if random.random() < MUTPB:
                    toolbox.mutate(mutant)
                    del mutant.fitness.values

            # Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit

            
            # Sort the offspring by fitness
            offspring.sort(key=lambda x: x.fitness.values[0])

            # Replace population with top mu offspring
            pop = list(map(toolbox.clone, offspring[:mu]))

            # The population is entirely replaced by the offspring
            #pop[:] = offspring

            # Record the new generation
            hof.update(pop)
            record = stats.compile(pop)
            total_evals += len(invalid_ind)
            logbook.record(gen=g, evals=total_evals, **record)
            print(logbook.stream)
        else:
            break


    gen = logbook.select("gen")
    fit_mins = logbook.select("min")
    size_avgs = logbook.select("avg")


    print(f'Best Score: {hof[0].fitness.values[0]}')
    print(f'Best Individual: {hof[0]}')

    # Plot evolution
    fig, ax1 = plt.subplots()
    line1 = ax1.plot(gen, fit_mins, "b-", label="Minimum Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")
    for tl in ax1.get_yticklabels():
        tl.set_color("b")

    ax2 = ax1.twinx()
    line2 = ax2.plot(gen, size_avgs, "r-", label="Average Fitness")
    ax2.set_ylabel("Avg. Fit.", color="r")
    for tl in ax2.get_yticklabels():
        tl.set_color("r")

    lns = line1 + line2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc="center right")

    # Record run
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S.%f')
    cur_dir = os.getcwd()
    prob_dir = os.path.join(cur_dir,'HW5\\Prob1a\\')
    if not os.path.exists(prob_dir):
        os.mkdir(prob_dir)
    time_dir = os.path.join(prob_dir,f'{timestamp}\\')
    os.mkdir(time_dir)
    plt.savefig(os.path.join(time_dir,'plot.png'))

    log_file = os.path.join(time_dir,'log.txt')
    with open(log_file, 'w') as f:
        print(f'Best Score: {hof[0].fitness.values[0]}', file=f)
        print(f'Best Individual: {hof[0]}\n', file = f)
        print(f'History: ', file=f)
        print(logbook, file=f)

    return hof[0]

def solve1b():
    """
    The function to solve for the optimum to f(x,y,3).
    """

    mu = 10
    lambda_ = 5 * mu
    CXPB_0 = 0.75
    MUTPB_0 = 0.5
    eval_limit = 2000

    xmin,xmax = -60,40
    ymin,ymax = -30,70
    smin, smax = 1e-3, 5.0

    toolbox = base.Toolbox()

    toolbox.register('individual', initES, creator.Individual, creator.Strategy, xmin, xmax, ymin, ymax, smin, smax)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxESBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutESLogNormal, c=0.01, indpb=0.25)
    toolbox.register('select', tools.selRandom)
    toolbox.register('evaluate', evaluate1b)

    toolbox.decorate('mate', checkBounds(xmin,xmax,ymin,ymax))
    toolbox.decorate('mutate', checkBounds(xmin,xmax,ymin,ymax))

    toolbox.decorate('mate', checkStrategy(smin))
    toolbox.decorate('mutate', checkStrategy(smin))

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    hof = tools.HallOfFame(1)

    pop = toolbox.population(n=mu)

    # Evaluate the entire population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # Record initial population
    g = 0
    record = stats.compile(pop)
    total_evals = mu
    logbook = tools.Logbook()
    logbook.header = 'gen','evals','min','max','avg','std'
    logbook.record(gen=0, evals=mu, **record)

    while True:
        if total_evals < (eval_limit - lambda_):
            CXPB = CXPB_0*(1-(total_evals/(eval_limit*1.05)))
            #CXPB = CXPB_0
            MUTPB = MUTPB_0*(total_evals/(eval_limit))
            g+=1
            # Select the next generation individuals
            offspring = toolbox.select(pop, lambda_)
            # Clone the selected individuals
            offspring = list(map(toolbox.clone, offspring))

            # Apply crossover and mutation on the offspring
            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < CXPB:
                    toolbox.mate(child1, child2)
                    del child1.fitness.values
                    del child2.fitness.values

            for mutant in offspring:
                if random.random() < MUTPB:
                    toolbox.mutate(mutant)
                    del mutant.fitness.values

            # Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit

            
            # Sort the offspring by fitness
            offspring.sort(key=lambda x: x.fitness.values[0])

            # Replace population with top mu offspring
            pop = list(map(toolbox.clone, offspring[:mu]))

            # The population is entirely replaced by the offspring
            #pop[:] = offspring

            # Record the new generation
            hof.update(pop)
            record = stats.compile(pop)
            total_evals += len(invalid_ind)
            logbook.record(gen=g, evals=total_evals, **record)
            print(logbook.stream)
        else:
            break


    gen = logbook.select("gen")
    fit_mins = logbook.select("min")
    size_avgs = logbook.select("avg")


    print(f'Best Score: {hof[0].fitness.values[0]}')
    print(f'Best Individual: {hof[0]}')

    # Plot evolution
    fig, ax1 = plt.subplots()
    line1 = ax1.plot(gen, fit_mins, "b-", label="Minimum Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")
    for tl in ax1.get_yticklabels():
        tl.set_color("b")

    ax2 = ax1.twinx()
    line2 = ax2.plot(gen, size_avgs, "r-", label="Average Fitness")
    ax2.set_ylabel("Avg. Fit.", color="r")
    for tl in ax2.get_yticklabels():
        tl.set_color("r")

    lns = line1 + line2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc="center right")

    # Record run
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S.%f')
    cur_dir = os.getcwd()
    prob_dir = os.path.join(cur_dir,'HW5\\Prob1b\\')
    if not os.path.exists(prob_dir):
        os.mkdir(prob_dir)
    time_dir = os.path.join(prob_dir,f'{timestamp}\\')
    os.mkdir(time_dir)
    plt.savefig(os.path.join(time_dir,'plot.png'))

    log_file = os.path.join(time_dir,'log.txt')
    with open(log_file, 'w') as f:
        print(f'Best Score: {hof[0].fitness.values[0]}', file=f)
        print(f'Best Individual: {hof[0]}\n', file=f)
        print(f'History: ', file=f)
        print(logbook, file=f)

    return hof[0]

def solve2():
    """
    The function to solve for the optimum to Ackley's function.
    """

    mu = 100
    lambda_ = 7 * mu
    CXPB_0 = 0.75
    MUTPB_0 = 0.2
    eval_limit = 200000

    dim = 30
    dmin,dmax = -30,30
    smin, smax = 5e-16, 1.0

    toolbox = base.Toolbox()

    toolbox.register('individual', initACK, creator.Individual, creator.Strategy, dim, dmin, dmax, smin, smax)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxESBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutESLogNormal, c=0.01, indpb=0.25)
    toolbox.register('select', tools.selRandom)
    toolbox.register('evaluate', evaluateAck)

    toolbox.decorate('mate', checkBounds(dmin,dmax,dmin,dmax))
    toolbox.decorate('mutate', checkBounds(dmin,dmax,dmin,dmax))

    toolbox.decorate('mate', checkStrategy(smin))
    toolbox.decorate('mutate', checkStrategy(smin))

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    hof = tools.HallOfFame(1)

    pop = toolbox.population(n=mu)

    # Evaluate the entire population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # Record initial population
    g = 0
    record = stats.compile(pop)
    total_evals = mu
    logbook = tools.Logbook()
    logbook.header = 'gen','evals','min','max','avg','std'
    logbook.record(gen=0, evals=mu, **record)

    while True:
        if total_evals < (eval_limit - lambda_):
            CXPB = CXPB_0
            MUTPB = MUTPB_0*(total_evals/eval_limit)
            if record['std'] == 0:
                toolbox.register("mutate", tools.mutESLogNormal, c=0.01, indpb=0.1)
            else:
                toolbox.register("mutate", tools.mutESLogNormal, c=0.01, indpb=0.05)
            g+=1
            # Select the next generation individuals
            offspring = toolbox.select(pop, lambda_)
            # Clone the selected individuals
            offspring = list(map(toolbox.clone, offspring))

            # Apply crossover and mutation on the offspring
            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < CXPB:
                    toolbox.mate(child1, child2)
                    del child1.fitness.values
                    del child2.fitness.values

            for mutant in offspring:
                if random.random() < MUTPB:
                    toolbox.mutate(mutant)
                    del mutant.fitness.values

            # Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = map(toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit

            # Sort the offspring by fitness
            offspring.sort(key=lambda x: x.fitness.values[0])

            # Replace population with top mu offspring
            pop = list(map(toolbox.clone, offspring[:mu]))

            # Record the new generation
            hof.update(pop)
            record = stats.compile(pop)
            total_evals += len(invalid_ind)
            logbook.record(gen=g, evals=total_evals, **record)
            print(logbook.stream)
        else:
            break


    gen = logbook.select("gen")
    fit_mins = logbook.select("min")
    size_avgs = logbook.select("avg")

    print(f'Best Score: {hof[0].fitness.values[0]}')
    print(f'Best Individual: {hof[0]}')

    # Plot evolution
    fig, ax1 = plt.subplots()
    line1 = ax1.plot(gen, fit_mins, "b-", label="Minimum Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")
    for tl in ax1.get_yticklabels():
        tl.set_color("b")

    ax2 = ax1.twinx()
    line2 = ax2.plot(gen, size_avgs, "r-", label="Average Fitness")
    ax2.set_ylabel("Avg. Fit.", color="r")
    for tl in ax2.get_yticklabels():
        tl.set_color("r")

    lns = line1 + line2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc="center right")

    # Record run
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S.%f')
    cur_dir = os.getcwd()
    prob_dir = os.path.join(cur_dir,'HW5\\Prob2\\')
    if not os.path.exists(prob_dir):
        os.mkdir(prob_dir)
    time_dir = os.path.join(prob_dir,f'{timestamp}\\')
    os.mkdir(time_dir)
    plt.savefig(os.path.join(time_dir,'plot.png'))

    log_file = os.path.join(time_dir,'log.txt')
    with open(log_file, 'w') as f:
        print(f'Best Score: {hof[0].fitness.values[0]}', file=f)
        print(f'Best Individual: {hof[0]}\n', file=f)
        print(f'History: ', file=f)
        print(logbook, file=f)

    return hof[0]
    
def find_best_run(problem):
    """
    A function to solve the given problem 10 times and report
    the best individuals found from each run.
    """

    if problem == '1a':
        run_func = solve1a
    elif problem == '1b':
        run_func = solve1b
    elif problem == '2':
        run_func = solve2

    global_hof = tools.HallOfFame(10)
    for i in range(10):
        print(i)
        run_best = run_func()
        global_hof.insert(run_best)

    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S.%f')
    cur_dir = os.getcwd()
    prob_dir = os.path.join(cur_dir,'HW5\\Prob'+problem+'\\')
    if not os.path.exists(prob_dir):
        os.mkdir(prob_dir)
    best_dir = os.path.join(prob_dir,f'best_runs_{timestamp}\\')
    os.mkdir(best_dir)
    
    best_runs_log = os.path.join(best_dir,'top_ten_log.txt')


    prefix = f'Score: {global_hof[0].fitness.values[0]}\t'
    preferredwidth = 210
    wrapper = textwrap.TextWrapper(width=preferredwidth,subsequent_indent=' '*len(prefix))
    with open(best_runs_log, 'w') as f:
        for ind in global_hof:
            print(wrapper.fill(f'Score: {ind.fitness.values[0]}\tInd: {ind}'), file=f)


if __name__=='__main__':
    
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin, strategy=None)
    creator.create("Strategy", array.array, typecode="d")

    #solve1a()
    #solve1b()
    #solve2()
    find_best_run('1a')
    find_best_run('1b')
    find_best_run('2')
