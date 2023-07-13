import numpy as np
from A import acceleration
import matplotlib.pyplot as plt
# SIMULATION PARAMETERS
k = 4  # number of bodies
G = 6.67*(10**(-6))  # Universal Gravitational constant
dt = 0.001  # timestep in seconds
total_time = 5
n = int(total_time/dt)  # number of timesteps

# INITIAL PARAMETERS
# INITIAL positions
x0 = np.array([0, 0, 1, 1])
y0 = np.array([0, 1, 0, 1])

# INITIAL Velocities
vx0 = np.array([0, 0.1, 0, 0])
vy0 = np.array([0, 0, 0.1, -0.1])

# MASSES
m = np.array([100000, 1, 1, 1])

# Arrays to save states
x = [x0]
y = [y0]
ux = [vx0]
uy = [vy0]
t = [0]

for i in range(n):
    x_new = []
    y_new = []
    ux_new = []
    uy_new = []
    for j in range(k):
        a = acceleration([x[i], y[i]], m, j)
        x_new.append(dt*dt*a[0]*G + x[i][j] + dt*ux[i][j])
        y_new.append(dt * dt * a[1] * G + y[i][j] + dt * uy[i][j])
        ux_new.append((x_new[j]-x[i][j])/dt)
        uy_new.append((y_new[j] - y[i][j]) / dt)
    x.append(x_new)
    y.append(y_new)
    ux.append(ux_new)
    uy.append(uy_new)
    t.append(t[i] + dt)

x = np.transpose(x)
y = np.transpose(y)

ax = plt.figure().add_subplot(projection='3d')
for i in range(k):
    ax.plot(x[i], y[i], t, label=f'Particle {i+1}')

ax.legend()

plt.show()

# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# # Example data
# time = t # Time instants
# x1 = x[0]  # X-coordinates
# y1 = y[0]  # Y-coordinates
# x2 = x[1]
# y2 = y[1]
# x3 = x[2]
# y3 = y[2]
#
#
#
# # Create a figure and axes
# fig, ax = plt.subplots()
# # ax.set_xlim(min(min(x1), min(x2), min(x3)) - 1, max(max(x1), max(x2), max(x3)) + 1)
# # ax.set_ylim(min(min(y1), min(y2), min(y3)) - 1, max(max(y1), max(y2), max(y3)) + 1)
# ax.set_xlim(-0.5, 0.5)
# ax.set_ylim(-2, 2)
#
# scatter = []
# for i in range(k):
#     scatter.append(ax.scatter([], [], marker='o', label=f'Particle {i}'))
#
#
# # Animation update function
# def update(frame):
#
#     for i in range(k):
#         scatter[i].set_offsets([[x[i][frame], y[i][frame]]])
#
#     return scatter
#
# # Create the animation
# animation = FuncAnimation(fig, update, frames=len(time), interval=1, blit=True)
#
# # Display the animation
# plt.xlabel('X-coordinate')
# plt.ylabel('Y-coordinate')
# plt.title('Particle Trajectories Animation')
# plt.legend()
# plt.grid(True)
# plt.show()
# plt.show()

