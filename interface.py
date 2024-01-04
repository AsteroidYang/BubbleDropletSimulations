import numpy as np
from tqdm import tqdm

class SimulationBox():
    
    def __init__(self, temp = 0.8, mu = -3.0, rho = np.zeros((3, 3, 3)), phi = np.zeros((3, 3, 3)), 
                x_bound = 'p', y_bound = 'p', z_bound = 'p'):
        self.temp = temp
        self.mu = mu
        self.rho = rho
        self.phi = phi
        self.e_ff = 1.
        self.x_bound = x_bound
        self.y_bound = y_bound
        self.z_bound = z_bound
        self.expend_box_update()
        self.cache = []
    
    def expend_box_update(self):
        x, y, z = np.shape(self.rho)
        self.expend_box = np.zeros((x+2, y+2, z+2))
        self.expend_box[1:x+1, 1:y+1, 1:z+1] = self.rho.copy()
        
        if self.x_bound not in ['p', 'm']:
            raise Exception('Undefined x_axis boundary condtion!')
        if self.y_bound not in ['p', 'm']:
            raise Exception('Undefined y_axis boundary condtion!')
        if self.z_bound not in ['p', 'm']:
            raise Exception('Undefined z_axis boundary condtion!')
            
        if self.x_bound == 'p':
            self.expend_box[0, 1:y+1, 1:z+1] = self.rho[x-1, :, :]
            self.expend_box[x+1, 1:y+1, 1:z+1] = self.rho[0, :, :]
            
        if self.x_bound == 'm':
            self.expend_box[0, 1:y+1, 1:z+1] = self.rho[1, :, :]
            self.expend_box[x+1, 1:y+1, 1:z+1] = self.rho[x-2, :, :]

        if self.y_bound == 'p':
            self.expend_box[1:x+1, 0, 1:z+1] = self.rho[:, y-1, :]
            self.expend_box[1:x+1, y+1, 1:z+1] = self.rho[:, 0, :]

        if self.y_bound == 'm':
            self.expend_box[1:x+1, 0, 1:z+1] = self.rho[:, 1, :]
            self.expend_box[1:x+1, y+1, 1:z+1] = self.rho[:, y-2, :]
            
        if self.z_bound == 'p':
            self.expend_box[1:x+1, 1:y+1, 0] = self.rho[:, :, z-1]
            self.expend_box[1:x+1, 1:y+1, z+1] = self.rho[:, :, 0]
            
        if self.z_bound == 'm':
            self.expend_box[1:x+1, 1:y+1, 0] = self.rho[:, :, 1]
            self.expend_box[1:x+1, 1:y+1, z+1] = self.rho[:, :, z-2]
            
    def set_temp(self, temp):
        self.temp = temp
    
    def set_rho(self, rho):
        self.rho = rho
        self.expend_box_update()

    def set_phi(self, phi):
        self.phi = phi
        if np.shape(self.phi) != np.shape(self.rho):
            raise Exception('The size of phi array is different from simulation box!')
    
    def set_mu(self, mu):
        self.mu = mu

    def set_eff(self, e_ff):
        self.e_ff = e_ff
        print("Attention! e_ff is defined as 1. Check what you did!")

    def __repr__(self) -> str:
        title = 'Simulation box imformation:\n'
        temp_info = 'Tempreture: {}\n'.format(str(self.temp))
        mu_info = 'Chemical potential: {}\n'.format(str(self.mu))
        size_info = 'Box size: {}\n'.format(str(np.shape(self.rho)))
        output = title + temp_info + mu_info + size_info
        return output

class Simulator():
    def __init__(self, NV_0, ite_num, init_k = 0.1, k_history = [], snapshots = []) -> None:
        self.NV_0 = NV_0
        self.ite_num = ite_num
        self.init_k = init_k
        self.k_history = k_history
        self.snapshots = snapshots


def iterator(box, ite_num, NV_0, init_k = 0.1, dump = 1000):
        
    def __chi_func(box):
        interval = np.array([0.5])
        chi = np.digitize(box.rho, interval)
        return chi

    def __seek_surface(box):
        x, y, z = np.shape(box.rho)
        chi_expend = np.ones((x+2, y+2, z+2))
        chi_expend[1:x+1, 1:y+1, 1:z+1] = __chi_func(box)
        chi_sumption = np.zeros((x, y, z))
        box.cache = []

        chi_expend[0, 1:y+1, 1:z+1] = box.rho[x-1, :, :]
        chi_expend[1:x+1, 0, 1:z+1] = box.rho[:, y-1, :]
        chi_expend[1:x+1, 1:y+1, 0] = box.rho[:, :, z-1]

        chi_expend[x+1, 1:y+1, 1:z+1] = box.rho[0, :, :]
        chi_expend[1:x+1, y+1, 1:z+1] = box.rho[:, 0, :]
        chi_expend[1:x+1, 1:y+1, z+1] = box.rho[:, :, 0]

        chi_sumption += chi_expend[0:x, 1:y+1, 1:z+1]
        chi_sumption += chi_expend[1:x+1, 0:y, 1:z+1]
        chi_sumption += chi_expend[1:x+1, 1:y+1, 0:z]
        chi_sumption += chi_expend[2:x+2, 1:y+1, 1:z+1]
        chi_sumption += chi_expend[1:x+1, 2:y+2, 1:z+1]
        chi_sumption += chi_expend[1:x+1, 1:y+1, 2:z+2]

        surface_interval1 = np.array([0.5, 5.5])
        surface_interval2 = np.array([5.5, 0.5])
        surface = np.digitize(chi_sumption, surface_interval1) * np.digitize(chi_sumption, surface_interval2)
        box.cache.append(surface)

        liquid_surface = np.digitize(chi_sumption, np.array([0.5]))
        bubble = 1 - liquid_surface
        box.cache.append(bubble)
        liquid = 1 - bubble - surface
        box.cache.append(liquid)

    def __delta_func(box):
        result = 1-np.abs(1-2*box.rho)
        return result

    def __rho_iteration(box, k):
        belta = 1/box.temp
        x, y, z = np.shape(box.rho)
        rho_sumption = np.zeros(np.shape(box.rho))
        __seek_surface(box)
        
        rho_sumption += box.expend_box[0:x, 1:y+1, 1:z+1]
        rho_sumption += box.expend_box[1:x+1, 0:y, 1:z+1]
        rho_sumption += box.expend_box[1:x+1, 1:y+1, 0:z]
        rho_sumption += box.expend_box[2:x+2, 1:y+1, 1:z+1]
        rho_sumption += box.expend_box[1:x+1, 2:y+2, 1:z+1]
        rho_sumption += box.expend_box[1:x+1, 1:y+1, 2:z+2]

        rho_new = 1/(1 + np.exp(-belta * (box.e_ff * rho_sumption - box.phi + box.mu
                                            + k*box.cache[0]*__delta_func(box))))
        box.expend_box_update()
        return rho_new

    def __k_iteration(box, NV_0, k):
        x, y, z = np.shape(box.rho)
        N = x*y*z
        NL_0 = N - NV_0
        #NL_n = np.sum(__chi_func(box))
        NV_n = np.sum(box.cache[1])
        NL_n = N - NV_n
        k = k + box.temp*np.log(np.sqrt((NL_0/NL_n)*(NV_n/NV_0)))
        return k    

    k_history = [init_k]
    snapshots = []
    for i in tqdm(range(ite_num)):
        box.rho = __rho_iteration(box, k_history[i])
        if i % dump == 0:
            snapshots.append(box.rho)
        k = __k_iteration(box, NV_0, k_history[i])
        k_history.append(k)
    del k_history[0]
    result = Simulator(NV_0, ite_num, init_k, k_history, snapshots)

    return result