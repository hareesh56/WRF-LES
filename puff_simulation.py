# puff_simulation.py

import numpy as np
from scipy import integrate
import pickle
import os

class WindInfo:
    def __init__(self, wind_speed, direction):
        self.wind = wind_speed
        self.direction = direction

class LeakInfo:
    def __init__(self, leak_size):
        self.leak_size = leak_size

class Atmos:
    def __init__(self, wind_speed):
        self.stab_class = []
        a = np.array([927, 370, 283, 707, 1070])
        l = np.array([0.102, 0.0962, 0.0722, 0.0475, 0.0335])
        q = np.array([-1.918, -0.101, 0.102, 0.465, 0.624])
        k = np.array([0.25, 0.202, 0.134, 0.0787, 0.0566])
        p = np.array([0.189, 0.162, 0.134, 0.135, 0.137])

        if wind_speed < 2:
            self.stab_class = 0
        elif wind_speed < 5:
            self.stab_class = 1
        elif wind_speed < 6:
            self.stab_class = 2
        else:
            self.stab_class = 3

        self.a = a[int(self.stab_class)]
        self.l = l[int(self.stab_class)]
        self.q = q[int(self.stab_class)]
        self.k = k[int(self.stab_class)]
        self.p = p[int(self.stab_class)]


class Time:
    def __init__(self, TSim, Tstep, Windstep):
        self.totaltime = int(TSim)
        self.timestep = int(Tstep)
        self.Windstep = int(Windstep)
        self.T = np.linspace(self.timestep, self.totaltime, int(self.totaltime // self.timestep))


class Results:
    def __init__(self, time, leak, ppm, x, y, z, height, winds, angles):
        self.time = time
        self.leak = leak
        self.ppm = ppm
        self.x = x
        self.y = y
        self.z = z
        self.height = height
        self.winds = winds
        self.angles = angles


class Leak:
    def __init__(self, leakrate, H):
        self.size = leakrate
        self.height = H + 0.01
        rhom = 681
        rhoa = 1225
        g = 9.8
        self.factors = g * leakrate * (1/np.pi) * (1/rhom - 1/rhoa)


def save_results(dir_out, results):
    if not os.path.exists(dir_out):
        os.makedirs(dir_out)
    n_scenario = len(os.listdir(dir_out))
    file_out = os.path.join(dir_out, f'scenario{n_scenario}.p')
    pickle.dump(results, open(file_out, 'wb'))


def puff_model(x, y, z, current_time, leak, atm, time, wind, angle):
    X, Y, Z = np.meshgrid(x, y, z)
    H = leak.height
    Q = leak.size
    Ffactor = leak.factors
    u = wind
    theta = angle

    X2 = X * np.cos(theta) + Y * np.sin(theta)
    Y2 = -X * np.sin(theta) + Y * np.cos(theta)
    X2[X2 < 0] = 0

    conc = np.zeros([len(x), len(y), len(z)])
    f2 = np.zeros([len(x), len(y), len(z)])
    f3 = np.zeros([len(x), len(y), len(z)])
    time_int = np.zeros([len(x), len(y), len(z)])

    if np.mod(current_time, time.Windstep) != 0:
        times = np.mod(current_time, time.Windstep)
    else:
        times = time.Windstep

    sigmay = atm.k * X2 / (1 + X2 / atm.a) ** atm.p
    sigmaz = atm.l * X2 / (1 + X2 / atm.a) ** atm.q
    Zm = H + 1.6 * Ffactor ** (1/3) * X2 ** (2/3) / u
    alpha = Q / (2 * np.pi * sigmay * sigmaz) ** 1.5
    alpha[alpha == np.inf] = 0

    f1a = np.exp(-Y2 ** 2 / (2 * sigmay ** 2))
    f1a[np.isnan(f1a)] = 0
    f2 = np.exp(-(Z - Zm) ** 2 / (2 * sigmaz ** 2))
    f3 = np.exp(-(Z + Zm) ** 2 / (2 * sigmaz ** 2))

    c1 = 2 * sigmay * sigmaz
    pp, qq, rr = X2.shape
    time_int = np.array([integrate.quad(lambda t: np.exp(-(X2[i, j, k] - u * t) ** 2 / c1[i, j, k]), 0, times) \
                         for i in range(0, pp) for j in range(0, qq) for k in range(0, rr)])
    conc_int = np.reshape(time_int[:, 0], X2.shape)
    conc = alpha * f1a * conc_int * (f2 + f3)

    cppm = conc * 1e6 / 656

    return cppm
    
def Sensor(Leaksize=None, LeakHeight=None, TSim=None, Tstep=None, x=None, y=None, z=None, dir_out='Results'):
    if Leaksize is None:
        AllLeaks = pickle.load(open('Data_Input/LeakData.p', 'rb'))
        Leaks = random.sample(AllLeaks.leak_size, 1)
        Leaksize = Leaks[0]

    if LeakHeight is None:
        LeakHeight = 2

    if TSim is None:
        TSim = 600

    if Tstep is None:
        Tstep = 30

    if x is None:
        xloc = np.linspace(-51, 49, 21)

    if y is None:
        yloc = np.linspace(-50, 50, 21)

    if z is None:
        zloc = np.linspace(0, 5, 6)

    Windstep = 60
    Windsize = int(TSim / Windstep)

    sim_time = Time(TSim, Tstep, Windstep)
    leak = Leak(Leaksize, LeakHeight)

    W = pickle.load(open('Data_Input/WindData.p', 'rb'))
    start = np.random.randint(0, len(W.wind) - Windsize)
    list1 = W.wind[start: start+Windsize]   #sequential selection
    list2 = W.direction[start: start+Windsize]
    wind_speed = np.array(list1)
    wind_angle = np.array(list2)
    wind_angles = (wind_angle - 180) * np.pi / 180

    rep_factor = int(Windstep / Tstep)

    winds = np.repeat(wind_speed, rep_factor)
    angles = np.repeat(wind_angles, rep_factor)

    concentration = np.empty((len(winds), 1), dtype=object)

    for ind in range(0, len(sim_time.T)):
        curr_time = sim_time.T[ind]
        atm = Atmos(winds[ind])
        concentration[ind, 0] = puff_model(xloc, yloc, zloc, curr_time, leak, atm, sim_time, winds[ind], angles[ind])

    quotient = (sim_time.T - 1) // Windstep
    index = (1 + quotient) * rep_factor - 1

    off = np.zeros((len(winds) + rep_factor, 1), dtype=object)

    for m in range(0, len(sim_time.T)):
        temp = int(index[m])
        off[m + rep_factor, 0] = concentration[temp, 0] - concentration[m, 0]

    final = np.empty((len(winds), 1), dtype=object)

    for p in range(0, len(sim_time.T)):
        final[p, 0] = concentration[p, 0] + off[p, 0]

    Result = Results(sim_time.T, Leaksize, final, xloc, yloc, zloc, LeakHeight, winds, wind_angle)
    save_results(dir_out, Result)
