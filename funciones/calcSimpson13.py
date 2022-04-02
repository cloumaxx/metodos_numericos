import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(x) * np.sin(x)


def s13(f, a, b):
    m = (a + b) / 2
    integral = (b - a) / 6 * (f(a) + 4 * f(m) + f(b))
    return integral


a = 0  # Limite inferior
b = np.pi  # Limite superior
n = 10  # Intervalos
h = (b - a) / n
suma = 0

for i in range(n):
    b = a + h
    area = s13(f, a, b)
    suma += area
    a = b

print(suma)
vt = np.exp(np.pi) / 2 + 1 / 2
errorport = abs((vt - suma) / vt) * 100
print('Error % =', errorport)