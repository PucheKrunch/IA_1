# Function: Eggholder. Solution -> f(x1, x2) = -959.6407; (x1, x2) = (512, 404.2319). Domain -> -512 <= x1, x2 <= 512
def eggholder(variables_values = [0, 0]):
    x1, x2     = variables_values
    func_value = - (x2 + 47)*np.sin(np.sqrt(abs( (x1/2) + x2 + 47))) - x1*np.sin(np.sqrt(abs( x1 - (x2 + 47))))
    return func_value

# Function: Ackley. Solution -> f(x1, x2) = 0; (x1, x2) = (0, 0). Domain -> -5 <= x1, x2 <= 5
def ackley(variables_values = [0, 0]):
    x1, x2     = variables_values
    func_value = -20*np.exp(-0.2*np.sqrt(0.5*(x1**2 + x2**2))) - np.exp(0.5*(np.cos(2*np.pi*x1) +np.cos(2*np.pi*x2) )) + np.exp(1) + 20
    return func_value