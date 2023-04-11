def delta(x):
    import numpy as np

    x_process = 1-(np.abs(1-2*x))**(1/3)

    return x_process