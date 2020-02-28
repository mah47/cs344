'''
Homework 1
Marcos Hernandez
CS344
Exercise 2
'''

#imports
from tools.aima.search import Problem, hill_climbing, simulated_annealing, exp_schedule
from random import randrange

class TSP(Problem):

#definition initializes random city and path generator
    def __init__(self, randomCity, randomPath):
        self.initial = []
        self.randomCity = randomCity
        self.randomPath = randomPath
        self.initial.append(randrange(0, randomCity - 1))
        print("Start:" + str(self.initial[0]) + "\n")

#definition value, distance for each city
    def value(self, TSPstate):
        cityValue = 0
        for cityNumber in range(0, len(TSPstate) - 1):
            distance = (cityNumber + 1) % randomCity
            cityValue += self.randomPath[tuple(sorted((TSPstate[cityNumber], TSPstate[distance])))]
        return cityValue

#definition result: new city travelled
    def result(self, TSPstate, travel):
        newCity = TSPstate[ : ]
        newCity.append(travel)
        return newCity

#definition actions: distance
    def actions(self, TSPstate):
        TSPaction = []
        for distance in range(0, randomCity):
            if distance not in TSPstate:
                TSPaction.append(distance)
        return TSPaction

if __name__ == '__main__':

    #change the number of cities it travels
    randomCity = 50
    randomPath = {}

#indicates path and distances that have been randomized
    for cityNumber in range(0, randomCity):
        for space in range(cityNumber + 1, randomCity):
            local = (cityNumber, space)
            newPathDistance = randrange(1, 9)
            randomPath[local] = newPathDistance

    TSPproblem = TSP(randomCity, randomPath)

#implementations
    hillClimbingImp = hill_climbing(TSPproblem)
    simulatedAnnealingImp = simulated_annealing(TSPproblem, exp_schedule(k=10, lam=0.005, limit=100))

#prints hill climbing and simulated annealing results
    print('Hill climbing:\t' + str(hillClimbingImp)
          + '\n\tvalue: ' + str(TSPproblem.value(hillClimbingImp))
          )

    print('Simulated annealing\t: ' + str(simulatedAnnealingImp)
          + '\n\tvalue: ' + str(TSPproblem.value(simulatedAnnealingImp))
          )