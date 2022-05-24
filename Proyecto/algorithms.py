# Required Libraries
import numpy  as np
import math
import random
import os
import matplotlib.pyplot as plt

############################################################################

# Function
def target_function():
    return

############################################################################

# Function: Initialize Variables
def initial_position(swarm_size = 3, min_values = [-5,-5], max_values = [5,5], target_function = target_function):
    position = np.zeros((swarm_size, len(min_values)+1))
    for i in range(0, swarm_size):
        for j in range(0, len(min_values)):
             position[i,j] = random.uniform(min_values[j], max_values[j])
        position[i,-1] = target_function(position[i,0:position.shape[1]-1])
    return position

# Function: Initialize Velocity
def initial_velocity(position, min_values = [-5,-5], max_values = [5,5]):
    init_velocity = np.zeros((position.shape[0], len(min_values)))
    for i in range(0, init_velocity.shape[0]):
        for j in range(0, init_velocity.shape[1]):
            init_velocity[i,j] = random.uniform(min_values[j], max_values[j])
    return init_velocity

# Function: Individual Best
def individual_best_matrix(position, i_b_matrix): 
    for i in range(0, position.shape[0]):
        if(i_b_matrix[i,-1] > position[i,-1]):
            for j in range(0, position.shape[1]):
                i_b_matrix[i,j] = position[i,j]
    return i_b_matrix

# Function: Velocity
def velocity_vector(position, init_velocity, i_b_matrix, best_global, w = 0.5, c1 = 2, c2 = 2):
    r1 = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
    r2 = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
    velocity = np.zeros((position.shape[0], init_velocity.shape[1]))
    for i in range(0, init_velocity.shape[0]):
        for j in range(0, init_velocity.shape[1]):
            velocity[i,j] = w*init_velocity[i,j] + c1*r1*(i_b_matrix[i,j] - position[i,j]) + c2*r2*(best_global[j] - position[i,j])
    return velocity

# Function: Updtade Position
def update_position(position, velocity, min_values = [-5,-5], max_values = [5,5], target_function = target_function):
    for i in range(0, position.shape[0]):
        for j in range(0, position.shape[1] - 1):
            position[i,j] = np.clip((position[i,j] + velocity[i,j]),  min_values[j],  max_values[j])
        position[i,-1] = target_function(position[i,0:position.shape[1]-1])
    return position

############################################################################

# PSO Function
def particle_swarm_optimization(swarm_size = 3, min_values = [-5,-5], max_values = [5,5], iterations = 50, decay = 0, w = 0.9, c1 = 2, c2 = 2, target_function = target_function, verbose = True):    
    count         = 0
    position      = initial_position(swarm_size = swarm_size, min_values = min_values, max_values = max_values, target_function = target_function)
    init_velocity = initial_velocity(position, min_values = min_values, max_values = max_values)
    i_b_matrix    = np.copy(position)
    best_global   = np.copy(position[position[:,-1].argsort()][0,:])
    plt.title(label = "Particle Swarm Optimization")
    while (count <= iterations):
        if (verbose == True):
            print('Iteration = ', count, ' f(x) = ', best_global[-1])
            plt.plot(count, best_global[-1], 'ro')
        position    = update_position(position, init_velocity, target_function = target_function)            
        i_b_matrix  = individual_best_matrix(position, i_b_matrix)
        value       = np.copy(i_b_matrix[i_b_matrix[:,-1].argsort()][0,:])
        if (best_global[-1] > value[-1]):
            best_global = np.copy(value)   
        if (decay > 0):
            n  = decay
            w  = w*(1 - ((count-1)**n)/(iterations**n))
            c1 = (1-c1)*(count/iterations) + c1
            c2 = (1-c2)*(count/iterations) + c2
        init_velocity = velocity_vector(position, init_velocity, i_b_matrix, best_global, w = w, c1 = c1, c2 = c2)
        count         = count + 1     
    plt.show()
    return best_global

############################################################################

# Function: Initialize Variables
def initial_population(population_size = 5, min_values = [-5,-5], max_values = [5,5], target_function = target_function):
    population = np.zeros((population_size, len(min_values) + 1))
    for i in range(0, population_size):
        for j in range(0, len(min_values)):
             population[i,j] = random.uniform(min_values[j], max_values[j]) 
        population[i,-1] = target_function(population[i,0:population.shape[1]-1])
    return population

# Function: Fitness
def fitness_function(population): 
    fitness = np.zeros((population.shape[0], 2))
    for i in range(0, fitness.shape[0]):
        fitness[i,0] = 1/(1+ population[i,-1] + abs(population[:,-1].min()))
    fit_sum = fitness[:,0].sum()
    fitness[0,1] = fitness[0,0]
    for i in range(1, fitness.shape[0]):
        fitness[i,1] = (fitness[i,0] + fitness[i-1,1])
    for i in range(0, fitness.shape[0]):
        fitness[i,1] = fitness[i,1]/fit_sum
    return fitness

# Function: Selection
def roulette_wheel(fitness): 
    ix = 0
    random = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
    for i in range(0, fitness.shape[0]):
        if (random <= fitness[i, 1]):
          ix = i
          break
    return ix

# Function: Offspring
def breeding(population, fitness, min_values = [-5,-5], max_values = [5,5], mu = 1, elite = 0, target_function = target_function):
    offspring = np.copy(population)
    b_offspring = 0
    if (elite > 0):
        preserve = np.copy(population[population[:,-1].argsort()])
        for i in range(0, elite):
            for j in range(0, offspring.shape[1]):
                offspring[i,j] = preserve[i,j]
    for i in range (elite, offspring.shape[0]):
        parent_1, parent_2 = roulette_wheel(fitness), roulette_wheel(fitness)
        while parent_1 == parent_2:
            parent_2 = random.sample(range(0, len(population) - 1), 1)[0]
        for j in range(0, offspring.shape[1] - 1):
            rand = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
            rand_b = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)                                
            if (rand <= 0.5):
                b_offspring = 2*(rand_b)
                b_offspring = b_offspring**(1/(mu + 1))
            elif (rand > 0.5):  
                b_offspring = 1/(2*(1 - rand_b))
                b_offspring = b_offspring**(1/(mu + 1))       
            offspring[i,j] = np.clip(((1 + b_offspring)*population[parent_1, j] + (1 - b_offspring)*population[parent_2, j])/2, min_values[j], max_values[j])           
            if(i < population.shape[0] - 1):   
                offspring[i+1,j] = np.clip(((1 - b_offspring)*population[parent_1, j] + (1 + b_offspring)*population[parent_2, j])/2, min_values[j], max_values[j]) 
        offspring[i,-1] = target_function(offspring[i,0:offspring.shape[1]-1]) 
    return offspring
 
# Function: Mutation
def mutation(offspring, mutation_rate = 0.1, eta = 1, min_values = [-5,-5], max_values = [5,5], target_function = target_function):
    d_mutation = 0            
    for i in range (0, offspring.shape[0]):
        for j in range(0, offspring.shape[1] - 1):
            probability = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
            if (probability < mutation_rate):
                rand = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
                rand_d = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)                                     
                if (rand <= 0.5):
                    d_mutation = 2*(rand_d)
                    d_mutation = d_mutation**(1/(eta + 1)) - 1
                elif (rand > 0.5):  
                    d_mutation = 2*(1 - rand_d)
                    d_mutation = 1 - d_mutation**(1/(eta + 1))                
                offspring[i,j] = np.clip((offspring[i,j] + d_mutation), min_values[j], max_values[j])
        offspring[i,-1] = target_function(offspring[i,0:offspring.shape[1]-1])                        
    return offspring

############################################################################

# GA Function
def genetic_algorithm(population_size = 5, mutation_rate = 0.1, elite = 0, min_values = [-5,-5], max_values = [5,5], eta = 1, mu = 1, generations = 50, target_function = target_function, verbose = True):    
    count = 0
    population = initial_population(population_size = population_size, min_values = min_values, max_values = max_values, target_function = target_function)
    fitness = fitness_function(population)    
    elite_ind = np.copy(population[population[:,-1].argsort()][0,:])
    plt.title(label = "Genetic Algorithm")
    while (count <= generations):  
        if (verbose == True):
            print('Generation = ', count, ' f(x) = ', elite_ind[-1])  
            plt.plot(count, elite_ind[-1], 'ro')
        offspring = breeding(population, fitness, min_values = min_values, max_values = max_values, mu = mu, elite = elite, target_function = target_function) 
        population = mutation(offspring, mutation_rate = mutation_rate, eta = eta, min_values = min_values, max_values = max_values, target_function = target_function)
        fitness = fitness_function(population)
        value = np.copy(population[population[:,-1].argsort()][0,:])
        if(elite_ind[-1] > value[-1]):
            elite_ind = np.copy(value) 
        count = count + 1    
    plt.show()   
    return elite_ind 

############################################################################

# Function: Initialize Variables
def initial_position(n = 3, min_values = [-5,-5], max_values = [5,5], target_function = target_function):
    position = np.zeros((n, len(min_values) + 1))
    for i in range(0, n):
        for j in range(0, len(min_values)):
             position[i,j] = random.uniform(min_values[j], max_values[j])
        position[i,-1] = target_function(position[i,0:position.shape[1]-1])
    return position

# Function: Velocity
def velocity(position, best_global, k0 = 0, k1 = 1, k2 = 2, F = 0.9, min_values = [-5,-5], max_values = [5,5], Cr = 0.2, target_function = target_function):
    v = np.copy(best_global)
    for i in range(0, len(best_global)):
        ri = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
        if (ri <= Cr):
            v[i] = best_global[i] + F*(position[k1, i] - position[k2, i])
        else:
            v[i] = position[k0, i]
        if (i < len(min_values) and v[i] > max_values[i]):
            v[i] = max_values[i]
        elif(i < len(min_values) and v[i] < min_values[i]):
            v[i] = min_values[i]
    v[-1] = target_function(v[0:len(min_values)])
    return v

############################################################################

# DE Function. DE/Best/1/Bin Scheme.
def differential_evolution(n = 3, min_values = [-5,-5], max_values = [5,5], iterations = 50, F = 0.9, Cr = 0.2, target_function = target_function, verbose = True):    
    count = 0
    position = initial_position(n = n, min_values = min_values, max_values = max_values, target_function = target_function)
    best_global = np.copy(position [position [:,-1].argsort()][0,:])
    plt.title(label = "Differential Evolution")
    while (count <= iterations):
        if (verbose == True):
            print('Iteration = ', count, ' f(x) ', best_global[-1])
            plt.plot(count, best_global[-1], 'ro')
        for i in range(0, position.shape[0]):
            k1 = int(np.random.randint(position.shape[0], size = 1))
            k2 = int(np.random.randint(position.shape[0], size = 1))
            while k1 == k2:
                k1 = int(np.random.randint(position.shape[0], size = 1))
            vi = velocity(position, best_global, k0 = i, k1 = k1, k2 = k2, F = F, min_values = min_values, max_values = max_values, Cr = Cr, target_function = target_function)        
            if (vi[-1] <= position[i,-1]):
                for j in range(0, position.shape[1]):
                    position[i,j] = vi[j]
            if (best_global[-1] > position [position [:,-1].argsort()][0,:][-1]):
                best_global = np.copy(position [position [:,-1].argsort()][0,:])  
        count = count + 1     
    plt.show()
    return best_global

############################################################################