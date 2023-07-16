def k_iteration(k, T, N, NV_0, bubble):

    import numpy as np

    NL_0 = N - NV_0
    NV_n = np.sum(bubble)
    NL_n = N - NV_n
    k = k + T*np.log(np.sqrt((NL_0/NL_n)*(NV_n/NV_0)))


    return k
