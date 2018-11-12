import numpy as np
from app.models.population import Population
from app.ga.parameters import MAX_GEN, POP_SIZE, ELITE_RATIO, MUT_PROB, X_OVER_PTS
from app.models.state import State
from app.state.events import events
from app.state.pilots import pilots
from app.analysis.plot_avg_fit import plot_avg_fit

# main program
# Runs the EA that fills pilots into events in a schedule.

# initialize the state
state = State(pilots, events)

# initialize the analysis
avg_fits = np.array([])

# initialize population
population = Population(size=POP_SIZE, elite_ratio=ELITE_RATIO, x_ovr_pts=X_OVER_PTS,
                        mut_prb=MUT_PROB, state=state)
# calculate the fitness
population.set_fitness()

for gen in range(MAX_GEN):
    # select parents
    population.make_next_generation()
    # calc fitness
    population.set_fitness()
    # print each generation's average fitness
    tot_fit = sum([indiv.fitness for indiv in population.population])
    avg_fits = np.append(avg_fits, tot_fit / population.size)
    # print("avg fit:", tot_fit / population.size)

plot_avg_fit(avg_fits)
print("all elites", population.elites)
