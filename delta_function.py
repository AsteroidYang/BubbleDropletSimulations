def delta(x):
    import numpy as np

    interval1 = np.array([0.45, 0.55])
    interval2 = np.array([0.55, 0.45])
    x_delta1 = np.digitize(x, interval1)
    x_delta2 = np.digitize(x, interval2)
    x_delta = x_delta1 * x_delta2 * x
    x_process = 1-np.abs(1-2*x_delta)

    return x_process