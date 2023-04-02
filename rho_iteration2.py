def rho_iteration(box_x, box_y, box_z, rho, T, phi, mu, kappa, e_ff):

    import delta_function
    import numpy as np
    
    belta = 1/T
    rho_new = rho
    rho_expend = np.ones((box_x+2, box_y+2, box_z+2))
    rho_expend[1:box_x+1, 1:box_y+1, 1:box_z+1] = rho

    rho_expend[0, 1:box_y+1, 1:box_z+1] = rho[box_x-1, :, :]
    rho_expend[1:box_x+1, 0, 1:box_z+1] = rho[:, box_y-1, :]
    rho_expend[1:box_x+1, 1:box_y+1, 0] = rho[:, :, box_z-1]

    rho_expend[box_x+1, 1:box_y+1, 1:box_z+1] = rho[0, :, :]
    rho_expend[1:box_x+1, box_y+1, 1:box_z+1] = rho[:, 0, :]
    rho_expend[1:box_x+1, 1:box_y+1, box_z+1] = rho[:, :, 0]
    



    for i in range(box_x):
        for j in range(box_y):
            for k in range(box_z): 
                rho_sumption = rho_expend[i, j+1, k+1] + rho_expend[i+2, j+1, k+1] + rho_expend[i+1, j, k+1] + rho_expend[i+1, j+2, k+1] + rho_expend[i+1, j+1, k] + rho_expend[i+1, j+1, k+2]


                rho_new[i, j, k] = 1/(1 + np.exp(-belta*(e_ff*rho_sumption - phi + mu + kappa*delta_function.delta(rho[i, j, k]))))
                #rho_new[i, j, k] = 1/(1 + np.exp(-belta*(e_ff*rho_sumption - phi + mu)))
                #print(rho_new[i, j, k])
    
    return rho_new