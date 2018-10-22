import random as rnd
import numpy as np

from models.individual import Individual
from models.eventGene import EventGene
from models.pilot import Pilot
from models.event import Event

# Runs the EA that fills pilots into events in a schedule.

MAX_GEN = 1000
POP_SIZE = 300

def createPopulation(size):
    population = [Individual(rnd.randrange(100)) for i in range(size)]
    return population

def selectParents(population):
    sortedPop = sorted(population, key=lambda indiv: indiv.fitness)
    return sortedPop[0:POP_SIZE // 2]

def makeChildren(parents):
    return [Individual(mutate(parent)) for parent in parents]

def mutate(parent):
    return parent.value + np.random.normal(0, .1)



# main program

population = createPopulation(POP_SIZE)
setPopFitness(population)

for gen in range(MAX_GEN):
    # select parents
    parents = selectParents(population)
    # generate offspring
    children = makeChildren(parents)
    # calc fitness
    setPopFitness(children)
    # combine population
    population = parents + children

sortedPop = sorted(population, key=lambda indiv: indiv.fitness)
print(sortedPop[0].value)
