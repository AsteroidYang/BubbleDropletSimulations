def kappa_iteration(kappa, T, N, NL_0, chi):

    import numpy as np

    NV_0 = N - NL_0
    NL_n = np.sum(chi)
    NV_n = N - NL_n
    kappa = kappa + T*np.log(np.sqrt((NL_0/NL_n)*(NV_n/NV_0)))

    return kappa
