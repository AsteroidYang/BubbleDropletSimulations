import numpy as np

box_x, box_y, box_z, T, mu, e_ff, NV_0, kappa, ite_num = np.loadtxt('./BubbleSimulations/input/input.txt')
box_x = int(box_x)
box_y = int(box_y)
box_z = int(box_z)
NV_0 = int(NV_0)

rho = np.ones((box_x, box_y, box_z))  # density of fluid



for i in range(box_x):  # initial bubble/droplet
    for j in range(box_y):
        for k in range(box_z):
            if (i-29)**2 + (j-29)**2 + (k-29)**2 < (11)**2:
                rho[i, j, k] = 0
            
np.save('./BubbleSimulations/input/rho_NV{}_mu{}'.format(NV_0, mu), rho)
