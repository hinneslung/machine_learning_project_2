"""
Generic implementation of gradient descent.
"""

from numpy import *
import util

def gd(func, grad, x0, numIter, stepSize):
    """
    Perform gradient descent on some function func, where grad(x)
    computes its gradient at position x.  Begin at position x0 and run
    for exactly numIter iterations.  Use stepSize/sqrt(t+1) as a
    step-size, where t is the iteration number.

    We return the final solution as well as the trajectory of function
    values.
    """
    
    # initialize current location
    x = x0

    # set up storage for trajectory of function values
    trajectory = zeros(numIter + 1)
    trajectory[0] = func(x)

    # begin iterations
    for iter in range(numIter):
        # compute the gradient at the current location
        # TODO: YOUR CODE HERE
        g = grad(x)

        # compute the step size
        # TODO: YOUR CODE HERE
        eta = stepSize / sqrt(iter + 1)

        # step in the direction of the gradient
        # TODO: YOUR CODE HERE
        x = x - g * eta

        # record the trajectory
        trajectory[iter+1] = func(x)

    # return the solution
    return (x, trajectory)
