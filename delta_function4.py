def delta(x):
    import numpy as np

    x_process = 1-(np.abs(1-2*x))**(12)

    return x_process