"""
Main program function.
Runs the EA that fills pilots into schedules events based on constraints.
"""

from datetime import datetime
from typing import Dict, List, NamedTuple
import uuid
import numpy as np
from app.models.state import State
from app.models.event import Event
from app.models.population import Population
from app.models.individual import Individual
from app.ga.parameters import MAX_GEN, POP_SIZE, ELITE_RATIO, MUT_PROB, X_OVER_PTS, DIVERSE_ELITE
from app.state.pilots_big import pilots
from app.state.snivs_big import snivs
from app.analysis.plot_avg_fit import plot_avg_fit
from app.analysis.diversity import pop_avg_hamming_dist

class Results(NamedTuple):
    population: List[Individual]
    avg_fits: List[List[float]]
    num_feasible: int
    percent_feasible: float
    run_time: float

def main(events: Dict[uuid.UUID, Event], print_results: bool = False, plot_results: bool = False,
         plot_file: str = '', print_hamming: bool = False) -> Results:
    """
    Main program. Runs the EA.

    Args:
        events: A dict of event objects describing the schedule.
        print_results: Set to True to print results to console.
        plot_results: Set to True to save a plot of the average and best fitness values.
        plot_file: name to save the plot file as.
        print_hamming: Set to True to print the final hamming distance to the console. Will not 
            print if print_results is False.

    Returns:
        'Results' named tuple
            population: List[Individual] - the final population
            avg_fits: List[List[float]] - the best and average fitness data by generation
            num_feasible: int - number of feasible solutions found
            percent_feasible: float - percentage of feasible solutions
            run_time: float - run time
    """

    # initialize the analysis
    avg_fits = np.array([[], []])
    start_time = datetime.now()

    # initialize the state, create composite chromosome
    state = State(pilots, events, snivs)

    # initialize population
    population = Population(size=POP_SIZE, elite_ratio=ELITE_RATIO, diverse_elite=DIVERSE_ELITE,
                            x_ovr_pts=X_OVER_PTS, mut_prb=MUT_PROB, state=state)

    # calculate initial fitness
    population.set_fitness()

    # go through each generation
    for _ in range(MAX_GEN):
        # select parents
        population.make_next_generation()
        # calc fitness
        population.set_fitness()
        # save each generation's average fitness for plotting / analysis
        tot_fit = sum([indiv.fitness for indiv in population.population])
        avg_fits = np.append(avg_fits, [[tot_fit / population.size], [population.min_fitness]],
                             axis=1)
        print(".", end='', flush=True)
    print("")

    run_time = (datetime.now() - start_time).total_seconds()
    feasible = population.get_feasible_count()

    if plot_results:
        plot_file = 'test' if not plot_file else plot_file
        plot_avg_fit(avg_fits, plot_file)
    if print_results:
        print("10 Best:", sorted(population.population)[:10])
        print("Feasible solutions: ", feasible, "{}%".format((feasible / population.size) * 100))
        print("Run Time (s):", run_time)
        if print_hamming:
            print("avg hamming dist:", pop_avg_hamming_dist(population.population))

    return Results(population=population.population, avg_fits=avg_fits, num_feasible=feasible,
                   percent_feasible=(feasible / population.size) * 100, run_time=run_time)
