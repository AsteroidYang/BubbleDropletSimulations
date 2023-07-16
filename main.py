import numpy as np

def main():
    
    phi = np.load('./input/phi.npy')               # external potential

    box_x, box_y, box_z, T, mu, e_ff, NV_0, k, ite_num = np.loadtxt('./input/input.txt')
    box_x = int(box_x)
    box_y = int(box_y)
    box_z = int(box_z)
    NV_0 = int(NV_0)
    ite_num = int(ite_num)


    rho = np.load('./input/rho.npy')

    import iteration
    k_mem, rho = iteration.iteration(ite_num, box_x, box_y, box_z, rho, T, phi, mu, k, e_ff, NV_0)


    import grand_potential
    grand_potential.G(box_x, box_y, box_z, T, e_ff, mu, NV_0, rho)


    np.save('./output/k_NV{}_mu{}.npy'.format(NV_0, mu), k_mem)

    return None


input_set = [60,    60,    60,    0.8,    -3.05,    1,      20000,      0.1,     10000]
    #        box_x, box_y, box_z, T,      @mu,      e_ff,   @NV_0,      kappa,   ite_num
input_set = np.array(input_set)
np.savetxt('./input/input.txt', input_set)

main()