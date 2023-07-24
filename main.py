import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def acceleration(r, m):
    G = 6.67*(10**(-11))  # Universal Gravitational constant in m^3 kg^-1 s^-2
    G = G * (60*60*24)**2 / (1.496*10**11)  # Convert to AU^3 kg^-1 day^-2
    n = len(r[0])
    a = np.zeros((2,n))
    for i in range(n):
        for j in range(n):
            if i != j:
                rij = r[:,i] - r[:,j]
                a[:,i] -= G * m[j] * rij / np.linalg.norm(rij)**3
    return a

# SIMULATION PARAMETERS
k = 5  # number of bodies (Sun + 4 inner planets)
G = 6.67*(10**(-11))  # Universal Gravitational constant in m^3 kg^-1 s^-2
G = G * (60*60*24)**2 / (1.496*10**11)  # Convert to AU^3 kg^-1 day^-2
dt = 1.0  # timestep in days
total_time = 365.25*2  # simulate for 2 years
n = int(total_time/dt)  # number of timesteps

# INITIAL PARAMETERS
# names of the bodies
names = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars']
# masses (in kg)
m_sun = 1.989 * 10**30
m = np.array([m_sun, 0.330*m_sun, 4.87*m_sun, 5.97*m_sun, 0.642*m_sun]) / m_sun  # in sun masses
# initial positions (in AU)
r0 = np.array([[0, 0], [0.39, 0], [0.723, 0], [1, 0], [1.524, 0]]).T
# initial velocities (in AU/day)
v0 = np.array([[0, 0], [0, 0.205], [0, 0.245], [0, 0.297], [0, 0.241]]).T

r = np.zeros((2, k, n))
v = np.zeros((2, k, n))
r[:,:,0] = r0
v[:,:,0] = v0

for i in range(n-1):
    k1_v = dt * acceleration(r[:,:,i], m)
    k1_r = dt * v[:,:,i]

    k2_v = dt * acceleration(r[:,:,i] + 0.5*k1_r, m)
    k2_r = dt * (v[:,:,i] + 0.5*k1_v)

    k3_v = dt * acceleration(r[:,:,i] + 0.5*k2_r, m)
    k3_r = dt * (v[:,:,i] + 0.5*k2_v)

    k4_v = dt * acceleration(r[:,:,i] + k3_r, m)
    k4_r = dt * (v[:,:,i] + k3_v)

    v[:,:,i+1] = v[:,:,i] + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
    r[:,:,i+1] = r[:,:,i] + (k1_r + 2*k2_r + 2*k3_r + k4_r) / 6

# 3D plot
ax = plt.figure().add_subplot(projection='3d')
t = np.linspace(0, total_time, n)
for i in range(k):
    ax.plot(r[0,i,:], r[1,i,:], t, label=names[i])

ax.legend()
plt.show()

# 2D animation
fig, ax = plt.subplots()
scatter = [ax.scatter([], [], marker='o', s=25*(1 if i>0 else 5), label=names[i]) for i in range(k)]
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

def update(frame):
    for i in range(k):
        scatter[i].set_offsets([[r[0,i,frame], r[1,i,frame]]])
    return scatter

animation = FuncAnimation(fig, update, frames=len(range(n)), interval=1, blit=True)

plt.xlabel('X-coordinate (AU)')
plt.ylabel('Y-coordinate (AU)')
plt.title('Trajectory of Sun and inner planets')
plt.legend()
plt.grid(False)
plt.show()
