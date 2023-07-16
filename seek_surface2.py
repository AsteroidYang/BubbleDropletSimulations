def seek_surface(box_x, box_y, box_z, rho):

    import numpy as np

    interval = np.array([0.5])
    chi = np.digitize(rho, interval)

    chi_expend = np.ones((box_x+2, box_y+2, box_z+2))
    chi_expend[1:box_x+1, 1:box_y+1, 1:box_z+1] = chi
    chi_sumption = np.zeros((box_x, box_y, box_z))

    chi_expend[0, 1:box_y+1, 1:box_z+1] = rho[box_x-1, :, :]
    chi_expend[1:box_x+1, 0, 1:box_z+1] = rho[:, box_y-1, :]
    chi_expend[1:box_x+1, 1:box_y+1, 0] = rho[:, :, box_z-1]

    chi_expend[box_x+1, 1:box_y+1, 1:box_z+1] = rho[0, :, :]
    chi_expend[1:box_x+1, box_y+1, 1:box_z+1] = rho[:, 0, :]
    chi_expend[1:box_x+1, 1:box_y+1, box_z+1] = rho[:, :, 0]

    chi_sumption += chi_expend[0:box_x, 1:box_y+1, 1:box_z+1]
    chi_sumption += chi_expend[1:box_x+1, 0:box_y, 1:box_z+1]
    chi_sumption += chi_expend[1:box_x+1, 1:box_y+1, 0:box_z]
    chi_sumption += chi_expend[2:box_x+2, 1:box_y+1, 1:box_z+1]
    chi_sumption += chi_expend[1:box_x+1, 2:box_y+2, 1:box_z+1]
    chi_sumption += chi_expend[1:box_x+1, 1:box_y+1, 2:box_z+2]

    surface_interval1 = np.array([0.5, 5.5])
    surface_interval2 = np.array([5.5, 0.5])
    surface = np.digitize(chi_sumption, surface_interval1) * np.digitize(chi_sumption, surface_interval2)

    liquid_surface = np.digitize(chi_sumption, interval)
    bubble = 1 - liquid_surface

    return surface, bubble, chi