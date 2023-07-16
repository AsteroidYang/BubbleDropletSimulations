import numpy as np
import visialization as vs



box_x, box_y, T, e_ff, ite_num = 60, 60, 0.8, 1, 10000

mu = -3.05
box_z = 20
NV_0 = 3000

#target_slice = 10000
#slice_layer = 30

k_mem = np.load('./output/k_NV{}_mu{}.npy'.format(NV_0, mu))
rho = np.load('./output/rho_NV{}_mu{}.npy'.format(NV_0, mu))
#rho = np.load('./output/rho_output_NV{}_mu{}/rho_ite{}.npy'.format(NV_0, mu, target_slice-1))


rho_slice = np.ones((box_x, box_y, box_z))
#rho_slice[:, :, slice_layer] = rho[:, :, slice_layer]



vs.visial_k(ite_num, k_mem)

vs.visial_bubble(box_x, box_y, box_z, rho)

#vs.visial_rho_slice(box_x, box_y, box_z, rho_slice, slice_layer)

#vs.visial_ite_animation(NV_0, mu, slice_layer, ite_num)
