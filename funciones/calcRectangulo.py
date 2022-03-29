import numpy as np
import sympy as sp
from sympy import *

x = symbols('x')
expresionf = input('Intruduce la funcion ')
f = sp.lambdify(x, expresionf, "numpy")

LimInf = float(input('Intruduzca el limite inferior '))

LimSup = float(input('Introduzca el limite superior '))

NumPar = int(input('Introduzca el numero de particiones '))

Pab = np.linspace(LimInf, LimSup, NumPar, endpoint=True)
print(Pab)  # Y

hPm = ((Pab[0] + Pab[1]) / 2) - LimInf
PmPab = Pab + hPm
print(PmPab)

fPm = f(PmPab)
print(fPm)  # x

ARect = 2 * hPm * fPm
print(ARect)

IntegralNum = np.sum(ARect)
print('La aproximacion a la integral es: ', IntegralNum)

# https://es.planetcalc.com/5494/
