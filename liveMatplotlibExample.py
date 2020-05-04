import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random
import numpy as np

fig, ax = plt.subplots()

data = []
def animate(i):
    # data = np.random.rand(100)
    data.append( random.randint(0, 100))
    if(len(data) > 100):
        del data[0]
    npData = np.asarray(data)
    timeStamps = np.arange(0.0, len(data), 1)

    ax.clear()
    ax.set_title("'__' Axis")
    ax.set_xlabel("Time")
    ax.set_ylabel("Acceleration")
    ax.plot(timeStamps,data)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()