# PSO Function
def particle_swarm_optimization(swarm_size = 3, min_values = [-5,-5], max_values = [5,5], iterations = 50, decay = 0, w = 0.9, c1 = 2, c2 = 2, target_function = target_function, verbose = True):    
    count         = 0
    position      = initial_position(swarm_size = swarm_size, min_values = min_values, max_values = max_values, target_function = target_function)
    init_velocity = initial_velocity(position, min_values = min_values, max_values = max_values)
    i_b_matrix    = np.copy(position)
    best_global   = np.copy(position[position[:,-1].argsort()][0,:])
    while (count <= iterations):
        if (verbose == True):
            print('Iteration = ', count, ' f(x) = ', best_global[-1])
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
    return best_global

############################################################################

############################################################################

# GA Function
def genetic_algorithm(population_size = 5, mutation_rate = 0.1, elite = 0, min_values = [-5,-5], max_values = [5,5], eta = 1, mu = 1, generations = 50, target_function = target_function, verbose = True):    
    count = 0
    population = initial_population(population_size = population_size, min_values = min_values, max_values = max_values, target_function = target_function)
    fitness = fitness_function(population)    
    elite_ind = np.copy(population[population[:,-1].argsort()][0,:])
    while (count <= generations):  
        if (verbose == True):
            print('Generation = ', count, ' f(x) = ', elite_ind[-1])  
        offspring = breeding(population, fitness, min_values = min_values, max_values = max_values, mu = mu, elite = elite, target_function = target_function) 
        population = mutation(offspring, mutation_rate = mutation_rate, eta = eta, min_values = min_values, max_values = max_values, target_function = target_function)
        fitness = fitness_function(population)
        value = np.copy(population[population[:,-1].argsort()][0,:])
        if(elite_ind[-1] > value[-1]):
            elite_ind = np.copy(value) 
        count = count + 1       
    return elite_ind 

############################################################################

# DE Function. DE/Best/1/Bin Scheme.
def differential_evolution(n = 3, min_values = [-5,-5], max_values = [5,5], iterations = 50, F = 0.9, Cr = 0.2, target_function = target_function, verbose = True):    
    count = 0
    position = initial_position(n = n, min_values = min_values, max_values = max_values, target_function = target_function)
    best_global = np.copy(position [position [:,-1].argsort()][0,:])
    while (count <= iterations):
        if (verbose == True):
            print('Iteration = ', count, ' f(x) ', best_global[-1])
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
    return best_global

############################################################################