import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def plotIntersection(points, f, g):

    # plot the graph
    plt.plot(points, f(points), points, g(points))

    # descover the point and plot them
    for point in points:
        [p, data, target, error] = fsolve(lambda x: f(x) - g(x), x0=point, full_output=True)
        if target and p <= max(points):
            plt.plot(p, f(p), 'ro')

    #show the graph
    plt.show()
