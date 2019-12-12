import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

max_coor = 150
fig, ax = plt.subplots()
minmax = [-max_coor, max_coor]
ax.scatter(x=[0, 0, 0, 0] + minmax, y=[0, 0, 0, 0] + minmax)
fig.set_tight_layout(True)
(ln,) = plt.plot(minmax, minmax, "ro")
def update(i):
    minmax = [-max_coor, max_coor]
    sim.step()  # Step forward in orbital simulation!
    xs = [moon.pos.x for moon in in_data] + minmax
    ys = [moon.pos.y for moon in in_data] + minmax
    ln.set_data(xs + minmax, ys + minmax)
    return (ln,)
anim = FuncAnimation(fig, update, frames=np.arange(0, 650), interval=40,)
anim.save("orbit.gif", dpi=80, writer="imagemagick")