import numpy as np
import pandas
import time

# Import Algorithms
from pyMetaheuristic.algorithm import particle_swarm_optimization, genetic_algorithm, differential_evolution
# Import Functions
from pyMetaheuristic.test_function import eggholder, ackley

start = time.time()

# EGGHOLDER

# PSO - Parameters
pso_parameters = {
    'swarm_size': 250,
    'min_values': (-512, -512),
    'max_values': (512, 512),
    'iterations': 100,
    'decay': 0,
    'w': 1.5,
    'c1': 2.03,
    'c2': 2.03
}

pso_results = []
for i in range(20):
    pso = particle_swarm_optimization(target_function = eggholder, **pso_parameters)

    # Print Solution
    pso_variables = pso[:-1]
    pso_minimum   = pso[ -1]
    print('Variables: ', np.around(pso_variables, 4) , ' Minimum Value Found: ', round(pso_minimum, 4) )
    pso_results.append(pso_minimum)

# GA - Parameters
ga_parameters = {
    'population_size': 250,
    'min_values': (-512, -512),
    'max_values': (512, 512),
    'generations': 100,
    'mutation_rate': 0.1,
    'elite': 1,
    'eta': 1,
    'mu': 1,
    'verbose': True
}

ga_results = []
for i in range(20):
    ga = genetic_algorithm(target_function = eggholder, **ga_parameters)

    # Print Solution
    ga_variables = ga[:-1]
    ga_minimum   = ga[ -1]
    print('Variables: ', np.around(ga_variables, 4) , ' Minimum Value Found: ', round(ga_minimum, 4) )
    ga_results.append(ga_minimum)

# DE - Parameters
de_parameters = {
    'n': 250,
    'min_values': (-512, -512),
    'max_values': (512, 512),
    'iterations': 100,
    'F': 0.9,
    'Cr': 0.2,
    'verbose': True
}

de_results = []
for i in range(20):
    de = differential_evolution(target_function = eggholder, **de_parameters)

    # Print Solution
    de_variables = de[:-1]
    de_minimum   = de[ -1]
    print('Variables: ', np.around(de_variables, 4) , ' Minimum Value Found: ', round(de_minimum, 4) )
    de_results.append(de_minimum)

dict = {
    'PSO': pso_results,
    'GA': ga_results,
    'DE': de_results,
}

df = pandas.DataFrame(dict)

df.to_csv("eggholder_data.csv")

# ACKLEY

# PSO - Parameters
pso_parameters = {
    'swarm_size': 250,
    'min_values': (-32.768, -32.768),
    'max_values': (32.768, 32.768),
    'iterations': 100,
    'decay': 0,
    'w': 1.5,
    'c1': 2.03,
    'c2': 2.03
}

pso_results = []
for i in range(20):
    pso = particle_swarm_optimization(target_function = ackley, **pso_parameters)

    # Print Solution
    pso_variables = pso[:-1]
    pso_minimum   = pso[ -1]
    print('Variables: ', np.around(pso_variables, 4) , ' Minimum Value Found: ', round(pso_minimum, 4) )
    pso_results.append(pso_minimum)

# GA - Parameters
ga_parameters = {
    'population_size': 250,
    'min_values': (-32.768, -32.768),
    'max_values': (32.768, 32.768),
    'generations': 100,
    'mutation_rate': 0.1,
    'elite': 1,
    'eta': 1,
    'mu': 1,
    'verbose': True
}

ga_results = []
for i in range(20):
    ga = genetic_algorithm(target_function = ackley, **ga_parameters)

    # Print Solution
    ga_variables = ga[:-1]
    ga_minimum   = ga[ -1]
    print('Variables: ', np.around(ga_variables, 4) , ' Minimum Value Found: ', round(ga_minimum, 4) )
    ga_results.append(ga_minimum)

# DE - Parameters
de_parameters = {
    'n': 250,
    'min_values': (-32.768, -32.768),
    'max_values': (32.768, 32.768),
    'iterations': 100,
    'F': 0.9,
    'Cr': 0.2,
    'verbose': True
}

de_results = []
for i in range(20):
    de = differential_evolution(target_function = ackley, **de_parameters)

    # Print Solution
    de_variables = de[:-1]
    de_minimum   = de[ -1]
    print('Variables: ', np.around(de_variables, 4) , ' Minimum Value Found: ', round(de_minimum, 4) )
    de_results.append(de_minimum)

dict = {
    'PSO': pso_results,
    'GA': ga_results,
    'DE': de_results,
}

df = pandas.DataFrame(dict)

df.to_csv("ackley_data.csv")

print("Total execution time:",time.time() - start)