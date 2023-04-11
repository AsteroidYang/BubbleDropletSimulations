box_x = 60
box_y = 60
box_z = 60

import numpy as np
import matplotlib.pyplot as plt

rho = np.full((box_x, box_y, box_z), 0.4)
chi = np.ones((box_x, box_y, box_z))

'''for i in range(box_x):
        for j in range(box_y):
                if 155 < (i-30)**2 + (j-30)**2 < 185:
                    rho[i, j, 0] = 0.7
                else: rho[i, j, 0] = 0.4'''
rho = rho/2

for i in range(box_x):
        for j in range(box_y):
            for k in range(box_z):
                if rho[i, j, k] > 0.5 :
                    chi[i, j, k] = 1
                else : chi[i, j, k] = 0

chi = chi * True
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.voxels(chi)

ax.set_xbound(0, box_x)
ax.set_ybound(0, box_y)
ax.set_zbound(0, box_z)

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()