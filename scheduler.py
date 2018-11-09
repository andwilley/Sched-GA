from app.models.population import Population
from app.state.sched import schedule
from app.ga.parameters import MAX_GEN, POP_SIZE, ELITE_RATIO
from app.models.state import State

# main program
# Runs the EA that fills pilots into events in a schedule.

# initialize the state
# state = State(...)

# initialize population
population = Population(POP_SIZE, ELITE_RATIO, schedule)
# calculate the fitness
population.set_fitness()

for gen in range(MAX_GEN):
    # select parents
    population.make_next_generation()
    # calc fitness
    population.set_fitness()

# display results
