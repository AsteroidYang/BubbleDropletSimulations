import numpy as np
import time

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
    np.save('./output/rho_NV{}_mu{}.npy'.format(NV_0, mu), rho)

    return None



start = time.time()

box_z = 20
CV = 3000

input_set = [60,    60,    box_z,    0.8,    -3.05,    1,      CV,         0.1,     10000]
    #        box_x, box_y, box_z,    T,      @mu,      e_ff,   @NV_0,      kappa,   ite_num
input_set = np.array(input_set)
np.savetxt('./input/input.txt', input_set)

main()

end = time.time()
print('\nrunning time: '+str(end-start)+'s')


'''
start = time.time()
flag = 1

startPoint_volume = 2000
endPoint_volume = 8000
interval_volume = 400

box_z = 20

num_sample = int((endPoint_volume - startPoint_volume)/interval_volume) + 1
constrained_volumes = np.linspace(startPoint_volume, endPoint_volume, num = num_sample)

for i in constrained_volumes:
    
    input_set = [60,    60,    box_z,    0.8,    -3.03,    1,      i,      0.1,     10000]
    #            box_x, box_y, box_z, T,      @mu,      e_ff,   @NV_0,  kappa,   ite_num
    input_set = np.array(input_set)
    np.savetxt('./input/input.txt', input_set)
    
    main()
    
    print('\ntotal progress:{0:.2%}'.format(flag/num_sample))
    flag += 1


end = time.time()
print('\nrunning time: '+str(end-start)+'s')
'''