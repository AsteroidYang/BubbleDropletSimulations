import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visial_k(ite_num, k_mem):

    fig, ax = plt.subplots()
    ax.plot(np.linspace(1, ite_num, ite_num), np.array(k_mem))
    plt.xlabel('iteration number')
    plt.ylabel('k')
    plt.show()


def visial_bubble(box_x, box_y, box_z, rho):
    
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


def visial_rho_slice(box_x, box_y, box_z, rho_slice, slice_layer):

    interval = np.array([0.5])
    chi = np.digitize(rho_slice, interval)
    bubble = np.abs(chi-1)
    bubble_slice = np.zeros((box_x, box_y, box_z))
    bubble_slice[:, slice_layer, :] = bubble[:, slice_layer, :]
    
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    ax.voxels(bubble_slice)

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


def visial_ite_animation(NV_0, mu, slice_layer, ite_num):

    ims = []
    fig, ax = plt.subplots()
    for i in np.linspace(1, ite_num, 200):
        
        rho_slice = np.load('./output/rho_output_NV{}_mu{}/rho_ite{}.npy'.format(NV_0, mu, int(i-1)))
        
        interval = np.array([0.5])
        chi = np.digitize(rho_slice, interval)
        chi = np.abs(chi-1)

        chi_slice_layer = chi[:, slice_layer, :]
        im = ax.imshow(chi_slice_layer)
        ims.append([im])

    
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

    plt.show()

    ani.save('./output/rho_animation.gif', writer='pillow')