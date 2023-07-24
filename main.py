import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D


def acceleration(r, m):
    G = 6.67 * (10 ** (-4))  # Universal Gravitational constant
    n = len(r[0])
    a = np.zeros((2, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                rij = r[:, i] - r[:, j]
                a[:, i] -= G * m[j] * rij / np.linalg.norm(rij) ** 3
    return a


# SIMULATION PARAMETERS
k = 5  # number of bodies
G = 6.67 * (10 ** (-4))  # Universal Gravitational constant
dt = 0.001  # timestep in seconds
total_time = 5
n = int(total_time / dt)  # number of timesteps

# INITIAL PARAMETERS
r0 = np.random.rand(2, k)
v0 = np.random.rand(2, k)
m = np.random.uniform(0.1, 10000, [1, k])[0]

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

# 3D plot
ax = plt.figure().add_subplot(projection='3d')
t = np.linspace(0, total_time, n)
for i in range(k):
    ax.plot(r[0, i, :], r[1, i, :], t, label=f'Particle mass = {m[i]}')

ax.legend()
plt.show()

# 2D animation
fig, ax = plt.subplots()
scatter = [ax.scatter([], [], marker='o', s=25, label=f'Mass = {m[i]} kg') for i in range(k)]
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)


def update(frame):
    for i in range(k):
        scatter[i].set_offsets([[r[0, i, frame], r[1, i, frame]]])
    return scatter


animation = FuncAnimation(fig, update, frames=len(range(n)), interval=1, blit=True)

plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Trajectory of particles')
plt.legend()
plt.grid(False)
plt.show()
