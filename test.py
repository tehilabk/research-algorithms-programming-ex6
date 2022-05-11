import numpy as np

from task_6.q1 import plotIntersection
from task_6.q2 import education_budget, security_budget_ratio, largest_budget_year

if __name__ == '__main__':

#####################q1#######################

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


#####################q2#######################

print("education budget for year 2000 was:", education_budget(2000))
print("security budget ratio for year 2000 was:", security_budget_ratio(2000))
print("largest budget for security office was: ", largest_budget_year("משרד הבטחון"))

