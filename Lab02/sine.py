"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time


class Sine(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    # random restarts lab2
    maxHillClimb = 0
    maxHillClimbEnd = 0
    maxSimAnneal = 0
    maxSimAnnealend = 0
    maximum = 30
    hillCountValue = 0
    climbhill = time.time()
    # Formulate a problem with a 2D hill function and a single maximum value.
    #Hill-Climbing Restart Random
    while hillCountValue <= 4:

        initial = randrange(0, maximum)
        p = Sine(initial, maximum, delta=1.0)
        print('\nInitial                      x: ' + str(p.initial)
              + '\t\tvalue: ' + str(p.value(initial))
              )

        # Solve the problem using hill-climbing.
        hill_solution = hill_climbing(p)
        currentValue = hill_solution
        currentSolutionHill = p.value(hill_solution)

        if currentSolutionHill > maxHillClimbEnd:
            maxHillClimbEnd = currentSolutionHill
            maxHillClimb = currentValue
        hillCountValue += 1



    highHillclimb = p.value(hill_solution)
    endClimb = time.time()


#Simualted Annealing Restart Random
    simanneal = time.time()
    countSimAnneal = 0

    while countSimAnneal <= 4:
        initial = randrange(0, maximum)
        p = Sine(initial, maximum, delta=1.0)
        print('Initial                      x: ' + str(p.initial)
              + '\t\tvalue: ' + str(p.value(initial))
              )
    # Solve the problem using simulated annealing.
        annealing_solution = simulated_annealing(
                p,
                exp_schedule(k=20, lam=0.005, limit=1000)
            )

        currentSimAnneal = annealing_solution
        currentSimAnnealSol = p.value(annealing_solution)

        if currentSimAnnealSol > maxSimAnnealend:
            maxSimAnnealend = currentSimAnnealSol
            maxSimAnneal - currentSimAnneal

        countSimAnneal += 1

        simannealend = time.time()



    hillclimbTime = endClimb - climbhill
    annealTime = simannealend - simanneal

    print('\nHill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(p.value(hill_solution))
          )

    print('Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(p.value(annealing_solution))
          )

    print("\nTime Results:")

    print("Hill-climbing: " + str(hillclimbTime))
    print("Simulated Annealing: " + str(annealTime))
