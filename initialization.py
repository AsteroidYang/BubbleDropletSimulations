import numpy as np

def init(box_x, box_y, box_z):

    rho = np.full((box_x, box_y, box_z), 0.4) #density of fluid
    chi = np.ones((box_x, box_y, box_z)) #status of lattice point

    for i in range(box_x):#initial bubble/droplet
        for j in range(box_y):
            for k in range(box_z):
                if (i-30)**2 + (j-30)**2 + (k-30)**2 < 196:
                    rho[i, j, k] = 0.7
                else: rho[i, j, k] = 0.4

    for i in range(box_x):
        for j in range(box_y):
            for k in range(box_z):
                if rho[i, j, k] > 0.5 :
                    chi[i, j, k] = 1
                else : chi[i, j, k] = 0
    
    return rho, chi
