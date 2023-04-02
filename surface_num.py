def surf_num(rho):

    import numpy as np

    (x, y, z) = np.shape(rho)
    num = 0

    for i in range(x):
        for j in range(y):
            for k in range(z):
                if 0.4<rho[i, j, k]<0.6:
                    num = num + 1
    print('surface=', num)
    return None
