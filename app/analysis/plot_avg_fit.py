import matplotlib.pyplot as plt
import numpy as np

def plot_avg_fit(averages, plot_file):
    title = 'Average Fitness For Each Successive Generation'
    x_axis = np.arange(0.0, len(averages[0]), 1.0)
    y_axis1 = averages[0, :]
    y_axis2 = averages[1, :]

    fig, axes = plt.subplots()
    axes.plot(x_axis, y_axis1, 'b')
    axes.plot(x_axis, y_axis2, 'g')
    axes.set(xlabel='generation', ylabel='average fitness', title=title)
    axes.set_ylabel(ylabel='average fitness', labelpad=0)
    axes.grid()
    fig.savefig("tmp/{}_avg.png".format(plot_file))

    title = 'Best Fitness For Each Successive Generation'
    axes.set_ylim(top=200000, bottom=0)
    axes.set(xlabel='generation', ylabel='best fitness', title=title)
    fig.savefig("tmp/{}_best.png".format(plot_file))
