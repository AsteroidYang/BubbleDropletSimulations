def iteration(ite_num, box_x, box_y, box_z, rho, T, phi, mu, kappa, e_ff, chi, NL_0):

    import rho_iteration2
    import kappa_iteration
    import visialization as vs

    k_mem = []
    N = box_x * box_y * box_z
    
    for n in range(ite_num):
        rho = rho_iteration2.rho_iteration(box_x, box_y, box_z, rho, T, phi, mu, kappa, e_ff)
        for i in range(box_x):
            for j in range(box_y):
                for k in range(box_z):
                    if rho[i, j, k] > 0.5 :
                        chi[i, j, k] = 1
                    else : chi[i, j, k] = 0
        
        k_mem.append(kappa)
        kappa = kappa_iteration.kappa_iteration(kappa, T, N, NL_0, chi)
        print('{0:-^60.2%}'.format((n+1)/ite_num), end = '\r')

        '''import surface_num
        surface_num.surf_num(rho)'''
        
        
        '''if n%9 == 0:
            vs.visial_chi(box_x, box_y, box_z,chi)'''

    return rho, kappa, k_mem, chi