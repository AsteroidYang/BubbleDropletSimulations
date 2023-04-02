'''
This module is replaced by rho_iteration2.py as the latter is more effective.
'''
def rho_iteration(box_x, box_y, box_z, rho, T, phi, mu, kappa, e_ff):

    import delta_function
    import numpy as np
    
    belta = 1/T
    rho_new = rho


    for i in range(box_x):
        for j in range(box_y):
            for k in range(box_z):


                #*************************************************8 vertex
                if i == 0 and j == 0 and k == 0:    #(0, 0, 0)
                    rho_sumption = rho[box_x-1, j, k] + rho[i+1, j, k] + rho[i, box_y-1, k] + rho[i, j+1, k] + rho[i, j, box_z-1] + rho[i, j, k+1]
                
                elif i == 0 and j == 0 and k == box_z-1:    #(0, 0, 30)
                    rho_sumption = rho[box_x-1, j, k] + rho[i+1, j, k] + rho[i, box_y-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, 0]

                elif i == 0 and j == box_y-1 and k == 0:    #(0, 30, 0)
                    rho_sumption = rho[box_x-1, j, k] + rho[i+1, j, k] + rho[i, j-1, k] + rho[i, 0, k] + rho[i, j, box_z-1] + rho[i, j, k+1]

                elif i == 0 and j == box_y-1 and k == box_z-1:    #(0, 30, 30)
                    rho_sumption = rho[box_x-1, j, k] + rho[i+1, j, k] + rho[i, j-1, k] + rho[i, 0, k] + rho[i, j, k-1] + rho[i, j, 0]
                
                elif i == box_x-1 and j == 0 and k == 0:    #(30, 0, 0)
                    rho_sumption = rho[i-1, j, k] + rho[0, j, k] + rho[i, box_y-1, k] + rho[i, j+1, k] + rho[i, j, box_z-1] + rho[i, j, k+1]
                
                elif i == box_x-1 and j == 0 and k == box_z-1:    #(30, 0, 30)
                    rho_sumption = rho[i-1, j, k] + rho[0, j, k] + rho[i, box_y-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, 0]
                
                elif i == box_x-1 and j == box_y-1 and k == 0:    #(30, 30, 0)
                    rho_sumption = rho[i-1, j, k] + rho[0, j, k] + rho[i, j-1, k] + rho[i, 0, k] + rho[i, j, box_z-1] + rho[i, j, k+1]
                
                elif i == box_x-1 and j == box_y-1 and k == box_z-1:    #(30, 30, 30)
                    rho_sumption = rho[i-1, j, k] + rho[0, j, k] + rho[i, j-1, k] + rho[i, 0, k] + rho[i, j, k-1] + rho[i, j, 0]


                #**************************************************12 edges
                elif i == 0 and j == 0 and 0 < k < box_z-1:    #(0, 0, z)
                    rho_sumption = rho[box_x-1, j, k] + rho[i+1, j, k] + rho[i, box_y-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, k+1]

                elif i == 0 and j == box_y-1 and 0 < k < box_z-1:     #(0, 30, z)
                    rho_sumption = rho[box_x-1, j, k] + rho[i+1, j, k] + rho[i, j-1, k] + rho[i, 0, k] + rho[i, j, k-1] + rho[i, j, k+1]

                elif i == box_x-1 and j == 0 and 0 < k < box_z-1:   #(30, 0, z)
                    rho_sumption = rho[i-1, j, k] + rho[0, j, k] + rho[i, box_y-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, k+1]

                elif i == box_x-1 and j == box_y-1 and 0 < k < box_z-1:   #(30, 30, z)
                    rho_sumption = rho[i-1, j, k] + rho[0, j, k] + rho[i, j-1, k] + rho[i, 0, k] + rho[i, j, k-1] + rho[i, j, k+1]
                
                elif i == 0 and 0 < j < box_y-1 and k == 0:    #(0, y, 0)
                    rho_sumption = rho[box_x-1, j, k] + rho[i+1, j, k] +rho[i, j-1, k] + rho[i, j+1, k] + rho[i, j, box_z-1] + rho[i, j, k+1]

                elif i == 0 and 0 < j < box_y-1 and k == box_z-1:    #(0, y, 30)
                    rho_sumption = rho[box_x-1, j, k] + rho[i+1, j, k] +rho[i, j-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, 0]

                elif i == box_x-1 and 0 < j < box_y-1 and k == 0:    #(30, y, 0)
                    rho_sumption = rho[i-1, j, k] + rho[0, j, k] +rho[i, j-1, k] + rho[i, j+1, k] + rho[i, j, box_z-1] + rho[i, j, k+1]
                
                elif i == box_x-1 and 0 < j < box_y-1 and k == box_z-1:    #(30, y, 30)
                    rho_sumption = rho[i-1, j, k] + rho[0, j, k] +rho[i, j-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, 0]

                elif 0 < i < box_x-1 and j == 0 and k == 0:    #(x, 0, 0)
                    rho_sumption = rho[i-1, j, k] + rho[i+1, j, k] +rho[i, box_y-1, k] + rho[i, j+1, k] + rho[i, j, box_z-1] + rho[i, j, k+1]

                elif 0 < i < box_x-1 and j == 0 and k == box_z-1:    #(x, 0, 30)
                    rho_sumption = rho[i-1, j, k] + rho[i+1, j, k] +rho[i, box_y-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, 0]

                elif 0 < i < box_x-1 and j == box_y-1 and k == 0:    #(x, 30, 0)
                    rho_sumption = rho[i-1, j, k] + rho[i+1, j, k] +rho[i, j-1, k] + rho[i, 0, k] + rho[i, j, box_z-1] + rho[i, j, k+1]

                elif 0 < i < box_x-1 and j == box_y-1 and k == box_z-1:    #(x, 30, 30)
                    rho_sumption = rho[i-1, j, k] + rho[i+1, j, k] +rho[i, j-1, k] + rho[i, 0, k] + rho[i, j, k-1] + rho[i, j, 0]


                #***************************************************6 faces
                elif i == 0 and 0 < j < box_y-1 and 0 < k < box_z-1:    #(0, y, z)
                    rho_sumption = rho[box_x-1, j, k] + rho[i+1, j, k] +rho[i, j-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, k+1]
                
                elif i == box_x-1 and 0 < j < box_y-1 and 0 < k < box_z-1:      #(30, y, z)
                    rho_sumption = rho[i-1, j, k] + rho[0, j, k] +rho[i, j-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, k+1]

                elif 0 < i < box_x-1 and j == 0 and 0 < k < box_z-1:    #(x, 0, z)
                    rho_sumption = rho[i-1, j, k] + rho[i+1, j, k] +rho[i, box_y-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, k+1]
                
                elif 0 < i < box_x-1 and j == box_y-1 and 0 < k < box_z-1:    #(x, 30, z)
                    rho_sumption = rho[i-1, j, k] + rho[i+1, j, k] +rho[i, j-1, k] + rho[i, 0, k] + rho[i, j, k-1] + rho[i, j, k+1]
                
                elif 0 < i < box_x-1 and 0 < j < box_y-1 and k == 0:    #(x, y, 0)
                    rho_sumption = rho[i-1, j, k] + rho[i+1, j, k] +rho[i, j-1, k] + rho[i, j+1, k] + rho[i, j, box_z-1] + rho[i, j, k+1]
                
                elif 0 < i < box_x-1 and 0 < j < box_y-1 and k == box_z-1:    #(x, y, 30)
                    rho_sumption = rho[i-1, j, k] + rho[i+1, j, k] +rho[i, j-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, 0]
                
                
                #***************************************************body
                else: 
                    rho_sumption = rho[i-1, j, k] + rho[i+1, j, k] + rho[i, j-1, k] + rho[i, j+1, k] + rho[i, j, k-1] + rho[i, j, k+1]


                rho_new[i, j, k] = 1/(1 + np.exp(-belta*(e_ff*rho_sumption - phi + mu + kappa*delta_function.delta(rho[i, j, k] - 0.5))))
                print(rho_new[i, j, k], rho_sumption)
    return rho_new