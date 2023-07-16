import numpy as np


box_x = 60
box_y = 60
box_z = 60


rho = np.ones((box_x, box_y, box_z))  # density of fluid

for i in range(box_x):  # initial bubble/droplet
    for j in range(box_y):
        for k in range(box_z):
            if (i-29)**2 + (j-29)**2 + (k)**2 < (11)**2:
                rho[i, j, k] = 0

np.save('./input/rho', rho)


phi = np.zeros((box_x, box_y, box_z))  # external field induced by solid

phi[:, :, 0] = 0.7


np.save('./input/phi', phi)
