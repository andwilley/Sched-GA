import matplotlib.pyplot as plt
import numpy as np

def plot_avg_fit(averages):
    title = 'Average Fitness For Each Successive Generation'
    x_axis = np.arange(0.0, len(averages), 1.0)
    y_axis = averages

    fig, axes = plt.subplots()
    axes.plot(x_axis, y_axis)

    axes.set(xlabel='generation', ylabel='average fitness', title=title)
    axes.grid()

    fig.savefig("tmp/test.png")
    plt.show()
