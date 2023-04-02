"""
fill in paramaters: box_x, box_y, box_z, T, mu, e_ff, phi, ite_num
boundry conditions are mirror now
"""

box_x = 60
box_y = 60
box_z = 60
T = 0.8               # tempreture
mu = -2.9               # chemical potential
e_ff = 0.99              # fluid-fluid interaction
phi = 0               # external potential
ite_num = 2000        # iteration number
NL_0 = 10000            # constrained volume
kappa = 0.1                 # Lanrangen paramater

import initialization
rho, chi = initialization.init(box_x, box_y, box_z)


import iteration
rho, kappa, k_mem, chi = iteration.iteration(ite_num, box_x, box_y, box_z, rho, T, phi, mu, kappa, e_ff, chi, NL_0)


import visialization as vs
vs.visial_kappa(ite_num, k_mem)
vs.visial_chi(box_x, box_y, box_z,chi)
