import sympy as sp
import math
import cmath


def remplazoFuncion(funcion, ele):
    usar = '' + str(ele)
    elemeto = str(funcion)
    accion = elemeto.replace('f', usar)
    return accion

def primerDerivada(funcion1):
        variable1 = 'x'
        funcion1=funcion1.replace('f','x')
        imprimir1 = sp.diff(funcion1, variable1)
        #print(imprimir1,'----')
        return imprimir1
#funcion='(exp(1)**(2*x))'
#print(primerDerivada(funcion))
#print(eval(str(primerDerivada(funcion))))
def primeraDerivadaNewton(funcion1):
        variable1 = 'x'
        imprimir1 = sp.diff(funcion1, variable1)
        print(imprimir1, '----')

        return imprimir1
#primerDerivada('exp(0)')
def solucionPrimeraDerivada(funcion1,variable1):
        derivada1 = primerDerivada(funcion1)
        imprimir1 = str(derivada1).replace('exp', ':><:')
        imprimir1 = str(imprimir1).replace('x', 'f')
        imprimir1 = str(imprimir1).replace(':><:', 'math.exp')
        imprimir1 = str(imprimir1).replace('cos','math.cos')
        imprimir1 = str(imprimir1).replace('sin','math.sin')
        imprimir1 = str(imprimir1).replace('tan', 'math.tan')
        imprimir1 = str(imprimir1).replace('acos','math.acos')
        imprimir1 = str(imprimir1).replace('asin','math.asin')
        imprimir1 = str(imprimir1).replace('atan', 'math.atan')
        imprimir1 = str(imprimir1).replace('sqrt', 'math.sqrt')
        calcular = remplazoFuncion(imprimir1,variable1)
        try:
            solucion1 = eval(calcular)
        except:
            solucion1 = calcular
        return solucion1
def segundaDerivada(funcion1):
        variable1 = 'x'
        funcion1=funcion1.replace('f','x')
        imprimir1 = sp.diff(funcion1, variable1)
        imprimir2 = sp.diff(imprimir1,variable1)
        return imprimir2
def solucionSegundaDerivada(funcion1,variable1):
        derivada1 = segundaDerivada(funcion1)
        imprimir1 = str(derivada1).replace('exp', ':><:')
        imprimir1 = str(imprimir1).replace('x', 'f')
        imprimir1 = str(imprimir1).replace(':><:', 'math.exp')
        imprimir1 = str(imprimir1).replace('sqrt', 'math.sqrt')
        imprimir1 = str(imprimir1).replace('cos','math.cos')
        imprimir1 = str(imprimir1).replace('sin','math.sin')
        imprimir1 = str(imprimir1).replace('tan', 'math.tan')
        imprimir1 = str(imprimir1).replace('acos','math.acos')
        imprimir1 = str(imprimir1).replace('asin','math.asin')
        imprimir1 = str(imprimir1).replace('atan', 'math.atan')
        #solucion1 = eval(remplazoFuncion(imprimir1,variable1))
        try:
            solucion1 = eval(remplazoFuncion(imprimir1,variable1))
        except:
            solucion1 = remplazoFuncion(imprimir1,variable1)
        return solucion1
def terceraDerivada(funcion1):
    variable1 = 'x'
    funcion1 = funcion1.replace('f', 'x')

    imprimir1 = sp.diff(funcion1, variable1)
    imprimir2 = sp.diff(imprimir1, variable1)
    imprimir3 =sp.diff(imprimir2, variable1)
    return imprimir3
def solucionTerceraDerivada(funcion1,variable1):
    derivada1 = terceraDerivada(funcion1)
    imprimir1 = str(derivada1).replace('exp', ':><:')
    imprimir1 = str(imprimir1).replace('x', 'f')
    imprimir1 = str(imprimir1).replace(':><:', 'math.exp')
    imprimir1 = str(imprimir1).replace('sqrt', 'math.sqrt')
    imprimir1 = str(imprimir1).replace('cos', 'math.cos')
    imprimir1 = str(imprimir1).replace('sin', 'math.sin')
    imprimir1 = str(imprimir1).replace('tan', 'math.tan')
    imprimir1 = str(imprimir1).replace('acos', 'math.acos')
    imprimir1 = str(imprimir1).replace('asin', 'math.asin')
    imprimir1 = str(imprimir1).replace('atan', 'math.atan')
    #solucion1 = eval(remplazoFuncion(imprimir1, variable1))
    try:
        solucion1 = eval(remplazoFuncion(imprimir1, variable1))
    except:
        solucion1 = remplazoFuncion(imprimir1, variable1)
    return solucion1
def cuartaDerivada(funcion1):
    variable1 = 'x'
    funcion1 = funcion1.replace('f', 'x')

    imprimir1 = sp.diff(funcion1, variable1)
    imprimir2 = sp.diff(imprimir1, variable1)
    imprimir3 = sp.diff(imprimir2, variable1)
    imprimir4 = sp.diff(imprimir3, variable1)
    return imprimir4

def solucionCuartaDerivada(funcion1,variable1):
    derivada1 = cuartaDerivada(funcion1)
    imprimir1 = str(derivada1).replace('exp', ':><:')
    imprimir1 = str(imprimir1).replace('x', 'f')
    imprimir1 = str(imprimir1).replace('sqrt', 'math.sqrt')
    imprimir1 = str(imprimir1).replace(':><:', 'math.exp')
    funcion1 = funcion1.replace('f', 'x')

    imprimir1 = str(imprimir1).replace('cos', 'math.cos')
    imprimir1 = str(imprimir1).replace('sin', 'math.sin')
    imprimir1 = str(imprimir1).replace('tan', 'math.tan')
    imprimir1 = str(imprimir1).replace('acos', 'math.acos')
    imprimir1 = str(imprimir1).replace('asin', 'math.asin')
    imprimir1 = str(imprimir1).replace('atan', 'math.atan')

    #solucion1 = eval(remplazoFuncion(imprimir1, variable1))
    try:
        solucion1 = eval(remplazoFuncion(imprimir1, variable1))
    except:
        solucion1 = remplazoFuncion(imprimir1, variable1)
    return solucion1



def algoritmoDerivada(funcion,variable1):
    variable='x'

    imprimir1 = sp.diff(funcion, variable)
    print("F(x)=", funcion)


    print("F'(x)=",imprimir1)
    solucion1= 0#eval(remplazoFuncion(imprimir1,ingreeo))
    print("F'(x)=", imprimir1,' = ',solucion1)
    imprimir2 = sp.diff(imprimir1,variable)

    solucion2=0#eval(remplazoFuncion(imprimir2,ingreeo))
    print("F''(x)=", imprimir2,' = ',solucion2)

#algoritmoDerivada('(x-3/4)*exp(-1/4*x**2)+cos(x)',10)
#x = sp.Symbol('x')

