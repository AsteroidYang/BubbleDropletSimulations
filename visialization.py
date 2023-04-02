def visial_kappa(ite_num, k_mem):

    import numpy as np
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(np.linspace(1, ite_num, ite_num), np.array(k_mem), linewidth=2.0)
    plt.xlabel('iteration number')
    plt.ylabel('kappa')
    plt.show()


def visial_chi(box_x, box_y, box_z,chi):

    import numpy as np
    import matplotlib.pyplot as plt

    

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