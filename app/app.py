from datetime import datetime
from typing import Dict
import uuid
import numpy as np
from app.models.state import State
from app.models.event import Event
from app.models.population import Population
from app.ga.parameters import MAX_GEN, POP_SIZE, ELITE_RATIO, MUT_PROB, X_OVER_PTS, DIVERSE_ELITE
from app.state.pilots_big import pilots
from app.state.snivs_big import snivs
from app.analysis.plot_avg_fit import plot_avg_fit
from app.analysis.diversity import pop_avg_hamming_dist

def main(events: Dict[uuid.UUID, Event], print_results: bool = False):
    # main program
    # Runs the EA that fills pilots into events in a schedule based on constraints.

    # initialize the analysis
    avg_fits = np.array([[], []])
    start_time = datetime.now()

    # initialize the state
    state = State(pilots, events, snivs)

    # initialize population and calculate initial fitness
    population = Population(size=POP_SIZE, elite_ratio=ELITE_RATIO, diverse_elite=DIVERSE_ELITE,
                            x_ovr_pts=X_OVER_PTS, mut_prb=MUT_PROB, state=state)
    population.set_fitness()

    # go through each generation
    for gen in range(MAX_GEN):
        # select parents
        population.make_next_generation()
        # calc fitness
        population.set_fitness()
        # save each generation's average fitness
        tot_fit = sum([indiv.fitness for indiv in population.population])
        avg_fits = np.append(avg_fits, [[tot_fit / population.size], [population.min_fitness]],
                             axis=1)
        print(".", end='', flush=True)
    print("")

    end_time = datetime.now()

    plot_avg_fit(avg_fits)
    feasible = population.get_feasible_count()
    if print_results:
        print("10 Best:", sorted(population.population)[:10])
        print("Feasible solutions: ", feasible, "{}%".format((feasible / population.size) * 100))
        print("Run Time (s):", (end_time - start_time).total_seconds())
        # print("avg hamming dist:", pop_avg_hamming_dist(population.population))
