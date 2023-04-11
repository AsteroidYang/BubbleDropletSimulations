import numpy as np
import time

start = time.time()

phi = 0               # external potential

box_x, box_y, box_z, T, mu, e_ff, NV_0, kappa, ite_num = np.loadtxt('./BubbleSimulations/input/input.txt')
box_x = int(box_x)
box_y = int(box_y)
box_z = int(box_z)
NV_0 = int(NV_0)
ite_num = int(ite_num)


rho = np.load('./BubbleSimulations/input/rho_NV{}_mu{}.npy'.format(NV_0, mu))
interval = np.array([0.5])
chi = np.digitize(rho, interval)

import iteration
rho, kappa, k_mem = iteration.iteration(ite_num, box_x, box_y, box_z, rho, T, phi, mu, kappa, e_ff, chi, NV_0)


import grand_potential
grand_potential.G(box_x, box_y, box_z, T, e_ff, mu, NV_0, rho)


np.save('./BubbleSimulations/output/rho_NV{}_mu{}.npy'.format(NV_0, mu), rho)
np.save('./BubbleSimulations/output/k_NV{}_mu{}.npy'.format(NV_0, mu), k_mem)

end = time.time()
print('\nrunning time: '+str(end-start)+'s')