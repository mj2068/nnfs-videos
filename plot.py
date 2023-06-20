import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')


def double(x):
    return x * 2


def square(x):
    return x**2


def f2xSquare(x):
    return 2 * x**2


def f4x(x):
    return 4 * x;

x = np.arange(0, 5)

y = f2xSquare(x)
y2 = f4x(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
