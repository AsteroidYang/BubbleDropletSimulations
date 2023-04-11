def G(box_x, box_y, box_z, T, e_ff, mu, NV_0, rho):
    import numpy as np

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

    grand_potential = T*np.sum(rho*np.log(rho) + (1-rho)*np.log(1-rho)) - np.sum(0.5*e_ff*rho*rho_sumption) - np.sum(mu*rho)

    with open('./BubbleSimulations/output/G_NV{}_mu{}.txt'.format(NV_0, mu), 'w') as f:
        f.write(str(grand_potential))