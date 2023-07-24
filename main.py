import numpy as np
from A import acceleration
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# SIMULATION PARAMETERS
k = 5  # number of bodies
G = 6.67 * (10 ** (-4))  # Universal Gravitational constant
dt = 0.001  # timestep in seconds
total_time = 5
n = int(total_time / dt)  # number of timesteps

# INITIAL PARAMETERS
# INITIAL positions
r0 = np.random.rand(2, k)
# INITIAL Velocities
v0 = np.random.rand(2, k)

# MASSES
m = np.random.uniform(0.1, 10000, [1, k])[0]

# Runge-Kutta 4th order method
r = np.zeros((2, k, n))
v = np.zeros((2, k, n))
r[:, :, 0] = r0
v[:, :, 0] = v0

for i in range(n - 1):
    k1_v = dt * acceleration(r[:, :, i], m)
    k1_r = dt * v[:, :, i]

    k2_v = dt * acceleration(r[:, :, i] + 0.5 * k1_r, m)
    k2_r = dt * (v[:, :, i] + 0.5 * k1_v)

    k3_v = dt * acceleration(r[:, :, i] + 0.5 * k2_r, m)
    k3_r = dt * (v[:, :, i] + 0.5 * k2_v)

    k4_v = dt * acceleration(r[:, :, i] + k3_r, m)
    k4_r = dt * (v[:, :, i] + k3_v)

    v[:, :, i + 1] = v[:, :, i] + (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
    r[:, :, i + 1] = r[:, :, i] + (k1_r + 2 * k2_r + 2 * k3_r + k4_r) / 6

# Plotting code remains the same
