def iteration(ite_num, box_x, box_y, box_z, rho, T, phi, mu, k, e_ff, chi, NV_0):

    import rho_iteration3
    import kappa_iteration
    import numpy as np
    import os

    os.makedirs('./output/rho_output_NV{}_mu{}'.format(NV_0, mu))

    k_mem = []
    N = box_x * box_y * box_z
    interval = np.array([0.5])
    
    for n in range(ite_num):
        rho = rho_iteration3.rho_iteration(box_x, box_y, box_z, rho, T, phi, mu, k, e_ff)
        chi = np.digitize(rho, interval)
        np.save('./output/rho_output_NV{}_mu{}/rho_ite{}.npy'.format(NV_0, mu, n), rho)
        
        k_mem.append(k)
        k = kappa_iteration.kappa_iteration(k, T, N, NV_0, chi)
        print('{0:-^60.2%}'.format((n+1)/ite_num), end = '\r')

    k_mem = np.array(k_mem)

    return k_mem, rho