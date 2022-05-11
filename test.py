import numpy as np

from task_6.q1 import plotIntersection

if __name__ == '__main__':

    points = np.linspace(-10, 10, 1000)
    f = lambda x: x ** 2
    g = lambda x: x + 10

    plotIntersection(points, f, g)

    points = np.linspace(-10, 10, 1000)
    f = lambda x: np.sin(x)
    g = lambda x: 0.2 * x

    plotIntersection(points, f, g)


    points = np.linspace(-10, 10, 1000)
    f = lambda x: x + x
    g = lambda x: x - x

    plotIntersection(points, f, g)


    points = np.linspace(-10, 10, 1000)
    f = lambda x: x ** 2
    g = lambda x: x - 2

    plotIntersection(points, f, g)


    points = np.linspace(-10, 10, 1000)
    f = lambda x : np.sin(x)
    g = lambda x : np.cos(x)
    plotIntersection(points, f, g)