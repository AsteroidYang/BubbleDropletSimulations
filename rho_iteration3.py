def rho_iteration(box_x, box_y, box_z, rho, T, phi, mu, k, e_ff):

    import delta_function3
    import numpy as np
    
    belta = 1/T
    rho_new = rho
    rho_expend = np.ones((box_x+2, box_y+2, box_z+2))
    rho_expend[1:box_x+1, 1:box_y+1, 1:box_z+1] = rho
    rho_sumption = np.zeros((box_x, box_y, box_z))

    rho_expend[0, 1:box_y+1, 1:box_z+1] = rho[box_x-1, :, :]
    rho_expend[1:box_x+1, 0, 1:box_z+1] = rho[:, box_y-1, :]
    rho_expend[1:box_x+1, 1:box_y+1, 0] = rho[:, :, box_z-1]

    rho_expend[box_x+1, 1:box_y+1, 1:box_z+1] = rho[0, :, :]
    rho_expend[1:box_x+1, box_y+1, 1:box_z+1] = rho[:, 0, :]
    rho_expend[1:box_x+1, 1:box_y+1, box_z+1] = rho[:, :, 0]
    
    rho_sumption += rho_expend[0:box_x, 1:box_y+1, 1:box_z+1]
    rho_sumption += rho_expend[1:box_x+1, 0:box_y, 1:box_z+1]
    rho_sumption += rho_expend[1:box_x+1, 1:box_y+1, 0:box_z]
    rho_sumption += rho_expend[2:box_x+2, 1:box_y+1, 1:box_z+1]
    rho_sumption += rho_expend[1:box_x+1, 2:box_y+2, 1:box_z+1]
    rho_sumption += rho_expend[1:box_x+1, 1:box_y+1, 2:box_z+2]

    surface_interval1 = np.array([0.5, 5.5])
    surface_interval2 = np.array([5.5, 0.5])
    surface = np.digitize(rho_sumption, surface_interval1) * np.digitize(rho_sumption, surface_interval2)


    rho_new = 1/(1 + np.exp(-belta * (e_ff * rho_sumption - phi + mu + k*surface*delta_function3.delta(rho))))

    return rho_new