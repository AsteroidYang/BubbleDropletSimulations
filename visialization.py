import numpy as np
import matplotlib.pyplot as plt

def visial_kappa(ite_num, k_mem):

    fig, ax = plt.subplots()
    ax.plot(np.linspace(1, ite_num, ite_num), np.array(k_mem))
    plt.xlabel('iteration number')
    plt.ylabel('k')
    plt.show()


def visial_chi(box_x, box_y, box_z, rho):
    
    interval = np.array([0.5])
    chi = np.digitize(rho, interval)

    bubble = np.abs(chi-1) * True
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    ax.voxels(bubble)

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


def visial_rho_slice(box_x, box_y, box_z, rho_slice):

    
    return None



box_x, box_y, box_z, T, e_ff, ite_num = 60, 60, 60, 0.8, 1, 10000
mu = -3.05
NV_0 = 12000
target_slice = 10000

k_mem = np.load('./output/k_NV{}_mu{}.npy'.format(NV_0, mu))

rho = np.load('./output/rho_output_NV{}_mu{}/rho_ite{}'.format(NV_0, mu, target_slice-1))

rho_slice = rho[:, :, 30]