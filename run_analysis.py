from typing import List
from app.app import main, Results
from app.state.events1 import events as event1
from app.state.events2 import events as event2
from app.state.events3 import events as event3
from app.state.events4 import events as event4
from app.state.events5 import events as event5
from app.analysis.plot_avg_fit import plot_avg_fit

RUNS_EACH = 20
events_list = [event1, event2, event3, event4, event5]
results: List[List[Results]] = [[], [], [], [], []]

for row, events in enumerate(events_list):
    for _ in range(RUNS_EACH):
        results[row].append(main(events))

total_run_time = 0.0
total_feasible = 0
for row, result_array in enumerate(results):
    event_total_run_time = 0.0
    event_total_feasible = 0
    for column, result in enumerate(result_array):
        if column == 0:
            event_total_fits = result.avg_fits
        else:
            event_total_fits += result.avg_fits
        event_total_run_time += result.run_time
        event_total_feasible += result.num_feasible
    # average each event, plot the averages
    plot_avg_fit(event_total_fits / float(RUNS_EACH), 'event{}'.format(row + 1))
    if row == 0:
        total_fits = event_total_fits
    else:
        total_fits += event_total_fits
    # average the run times for each event, print those
    print("event{} avg run time:".format(row + 1), event_total_run_time / RUNS_EACH)
    total_run_time += event_total_run_time
    # average number of feasible solutions per event, print those
    print("event{} avg feasible solutions:".format(row + 1), event_total_feasible / RUNS_EACH)
    total_feasible += event_total_feasible

# average of all average fits
plot_avg_fit(total_fits / (len(events_list) * RUNS_EACH), 'overall')
# average of all run times
print("overall avg run time:", total_run_time / (len(events_list) * RUNS_EACH))
# average of feasible solutions & percentage
print("overall avg feasible:", total_feasible / (len(events_list) * RUNS_EACH))
