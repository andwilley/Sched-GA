from app.models.population import Population
from app.ga.parameters import MAX_GEN, POP_SIZE, ELITE_RATIO, MUT_PROB, X_OVER_PTS
from app.models.state import State
from app.state.events import events
from app.state.pilots import pilots

# main program
# Runs the EA that fills pilots into events in a schedule.

# initialize the state
state = State(pilots, events)

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

print("all elites", population.elites[0])
