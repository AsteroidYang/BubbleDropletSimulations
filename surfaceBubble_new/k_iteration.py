def k_iteration(k, T, N, NV_0, chi):

    import numpy as np

    NL_0 = N - NV_0
    NL_n = np.sum(chi)
    NV_n = N - NL_n
    k = k + T*np.log(np.sqrt((NL_0/NL_n)*(NV_n/NV_0)))

    return k
