"""arreglo1=[1,2,3,4,5]
arreglo2=[6,7,8,9,10]
arreglo3=[[11,12,13,14,15],[15,15,15,15,15,15]]
solucion=[]
solucion.append(arreglo1)
solucion.append(arreglo2)
print(solucion[1])
print(solucion[1][2])
for i in range(len(arreglo3)):
    for j in range(len[arreglo3[i]]):
        print()
print(arreglo3)"""
import numpy as np


def suma(m):
    cantidad = len(m)
    suma = None
    iguales = True
    for i in range(cantidad - 1):
        if iguales == False:
            break
        else:
            if len(m[i]) == len(m[i + 1]) and len(m[i][0]) == len(m[i + 1][0]):
                iguales = True
            else:
                iguales = False

    if iguales == True:
        for i in range(cantidad):
            if i == 0:
                suma = m[i]
            else:
                suma = np.add(suma, m[i])

    return suma


def resta(m):
    cantidad = len(m)
    resta = None
    iguales = True
    for i in range(cantidad - 1):
        if iguales == False:
            break
        else:
            if len(m[i]) == len(m[i + 1]) and len(m[i][0]) == len(m[i + 1][0]):
                iguales = True
            else:
                iguales = False

    if iguales == True:
        for i in range(cantidad):
            if i == 0:
                resta = m[i]
            else:
                resta = np.subtract(resta, m[i])

    return resta


"""
def producto():


def determinante():

def inversa():


def transpuesta():


def gauss():
"""

a = [[[1, 2, 3], [4, 5, 6], [7, 8, 9],[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
c = [[1, 5, 2], [5, 5, 5], [3, 3, 6]]
d = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

m = [b, c, d]

def nombrarMatrices(arreglo):
    abecedario="abcdefghijklmnopqrstuvwxyz".upper()
    for i in range(0,len(arreglo)):
        for j in range(0,len(arreglo[i])):
            arreglo[i][j].append(abecedario[j])

    #for x in range(0,len(arreglo[0])):
        #print('->',arreglo[0][x][len(arreglo[0][x])-1])
    return arreglo
def returnarPosArregloPorletra(arreglo,letra):
    arreglo=nombrarMatrices(arreglo)
    lugar = 0
    for x in range(0, len(arreglo[0])):
        if arreglo[0][x][len(arreglo[0][x])-1]==letra:
            lugar=x
    return lugar
#returnarPosArregloPorletra(a,'D')
#nombrarMatrices(a)