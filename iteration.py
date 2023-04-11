def iteration(ite_num, box_x, box_y, box_z, rho, T, phi, mu, kappa, e_ff, chi, NV_0):

    import rho_iteration2
    import kappa_iteration
    import numpy as np

    k_mem = []
    N = box_x * box_y * box_z
    interval = np.array([0.5])
    
    for n in range(ite_num):
        rho = rho_iteration2.rho_iteration(box_x, box_y, box_z, rho, T, phi, mu, kappa, e_ff)
        chi = np.digitize(rho, interval)
        
        k_mem.append(kappa)
        kappa = kappa_iteration.kappa_iteration(kappa, T, N, NV_0, chi)
        print('{0:-^60.2%}'.format((n+1)/ite_num), end = '\r')

    k_mem = np.array(k_mem)

    return rho, kappa, k_mem