def iteration(ite_num, box_x, box_y, box_z, rho, T, phi, mu, k, e_ff, NV_0):

    import rho_iteration4
    import k_iteration
    import numpy as np
    #import os
    import seek_surface

    #os.makedirs('./output/rho_output_NV{}_mu{}'.format(NV_0, mu))

    k_mem = []
    N = box_x * box_y * box_z
    surface, chi= seek_surface.seek_surface(box_x, box_y, box_z, rho)
    
    for n in range(ite_num):
        
        rho = rho_iteration4.rho_iteration(box_x, box_y, box_z, rho, T, phi, mu, k, e_ff, surface)
        surface, chi = seek_surface.seek_surface(box_x, box_y, box_z, rho)
        #np.save('./output/rho_output_NV{}_mu{}/rho_ite{}.npy'.format(NV_0, mu, n), rho)
        
        k_mem.append(k)
        k = k_iteration.k_iteration(k, T, N, NV_0, chi)
        
        print('{0:-^60.2%}'.format((n+1)/ite_num), end = '\r')

    k_mem = np.array(k_mem)

    return k_mem, rho