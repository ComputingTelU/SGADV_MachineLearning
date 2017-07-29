import sys
import json
import numpy as np
import matplotlib.pyplot as plt

# Hyphotesis test
def hyph(item, t0, t1):
    return t0 + t1 * item[0]

# Cost function
def cost(data, t0, t1):
    return 0.5 / len(data) * sum([(hyph(item, t0, t1) - item[1]) ** 2 for item in data])

# Learning function, for univariate variable
def learn(fx, fy, flearn):
    # Load x and y data from external files (fx and fy)
    x = []
    y = []
    with open(fx) as f1, open(fy) as f2:
        x = [float(line) for line in f1]
        y = [float(line) for line in f2]

    data = [(x[i], y[i]) for i in range(len(x))]

    # Learning rate and number of max iteration
    lrate = 0.07
    itern = 1000

    # Threshold for determining when iteration should stop converging
    thres = 1e-6

    # Find theta values using gradient descent
    t0 = 0.
    t1 = 0.
    for i in range(itern):
        g0 = lrate * sum([(hyph(item, t0, t1) - item[1]) for item in data]) / len(data)
        g1 = lrate * sum([(hyph(item, t0, t1) - item[1]) * item[0] for item in data]) / len(data)

        curcost = cost(data, t0 - g0, t1 - g1)
        if curcost < thres:
            break

        t0 -= g0
        t1 -= g1

        mincost = curcost

    # Save theta values to json file
    with open(flearn, 'w') as f:
        json.dump((t0, t1), f)

    # Draw it
    axis = np.arange(0., 10., 0.1)

    plt.plot(x, y, 'o', label='Data', markersize=5)
    plt.plot(axis, t0 + t1 * axis, 'r', label='Line')
    plt.legend()
    plt.show()

# Test function
def test(flearn, value):
    with open(flearn, 'r') as f:
        t0, t1 = json.load(f)

    result = t0 + t1 * value


    print 'result for', value, '=', result
