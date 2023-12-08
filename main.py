import matplotlib.pyplot as plt
import numpy as np

from matplotlib import animation
from math import sin, pi, sinh


if __name__ == "__main__":
    position_samples, step_size = np.linspace(-1, 1, num=100, retstep=True)
    velocities = np.zeros_like(position_samples)

    def wave(frame: int, line: plt.Line2D, position_samples: np.ndarray, step_size: float, delta_time: float):
        field = line.get_ydata()
        for i in range(1, len(field) - 1):
            WAVE_SPEED = 1
            laplacian = (field[i - 1] + field[i + 1] - 2 * field[i]) / (step_size ** 2)
            velocities[i] += (WAVE_SPEED ** 2) * laplacian * delta_time

        line.set_ydata(field + velocities * delta_time)

        return line,


    fig, ax = plt.subplots()

    # \left(x-1\right)\left(x+1\right)\sinh\left(x^{2}\right)+0.1\sin\left(\pi x\right)
    line, = ax.plot(position_samples, np.array([(x**2 - 1) * sinh(x**2) + 0.1 * sin(pi * x) for x in position_samples]))

    ax.set_title("Numerical Wave Simulation")
    ax.grid(True)
    ax.set_xlabel("Position x")
    ax.set_ylabel("Field u(x,t)")
    ax.set_xlim(left=-1, right=1)
    ax.set_ylim(bottom=-1.5, top=1.5)

    ani = animation.FuncAnimation(fig, wave,
                                  save_count=1000,
                                  interval=20,
                                  blit=True,
                                  fargs=(line, position_samples, step_size, 0.02))

    ani.save("wave.mp4")
