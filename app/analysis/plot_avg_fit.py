import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot_avg_fit(averages):
    x_axis = np.arange(0.0, len(averages), 1.0)
    y_axis = averages

    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis)

    ax.set(xlabel='generation', ylabel='average fitness',
           title='Average Fitness For Each Successive Generation')
    ax.grid()

    fig.savefig("test.png")
    plt.show()
