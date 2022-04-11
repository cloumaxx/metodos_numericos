import matplotlib.pyplot as plt
import math
import numpy as np

def ieee(numero):
    def retornarExponente(bits):
        exponente = ""
        if bits == 32:
            for i in range(1, 9):
                exponente += arreglo32[i]
        else:
            for i in range(1, 12):
                exponente += arreglo64[i]

        return exponente

    def retornarMantisa(bits):
        mantisa = ""
        if bits == 32:
            mantisa = ""
            for i in range(9, len(arreglo32)):
                mantisa += str(arreglo32[i])
        else:
            for i in range(12, len(arreglo64)):
                mantisa += str(arreglo64[i])
        return mantisa

    def retornarSigno():
        return arreglo32[0]

    def convertirFraccionario(parteDecimal):
        msj = ""
        aux = 0
        decimal = parteDecimal
        while (decimal > 0 and aux < 64):
            res = decimal * 2
            msj += str(int(res))
            decimal = round(res - int(res), 64)
            aux += 1
        return msj

    arreglo32 = [32]  # 2 espacios extras para el espacio
    arreglo64 = [64]  # 2 espacios extras para el espacio
    aux32 = 0
    aux64 = 0
    numero = float(numero)

    if numero < 0:
        numero = numero * -1
        arreglo32[aux32] = 1;
        arreglo64[aux64] = 1;
        aux32 += 1
        aux64 += 1
    else:
        arreglo32[aux32] = 0;
        arreglo64[aux64] = 0;
        aux32 += 1
        aux64 += 1

    parteEntera, parteDecimal = str(numero).split(".")
    binEntero = bin(int(parteEntera)).replace("0b", "")

    binDecimal = convertirFraccionario(float("0." + parteDecimal))
    binCompleto = binEntero + "." + binDecimal
    if (numero < 0):
        binCompleto.replace("-", "")
    auxExponente = len(binEntero) - 1
    binExponente32 = str(bin(auxExponente + 127).replace("0b", ""))
    binExponente64 = str(bin(auxExponente + 1023).replace("0b", ""))
    binMantisa = (binCompleto.replace(".", ""))[1:]

    # Reglas Ieee

    for a in binExponente32:
        arreglo32.append(a)
        aux32 += 1

    for a in binExponente64:
        arreglo64.append(a)
        aux64 += 1

    if len(binMantisa) >= 23:
        for a in range(23):
            arreglo32.append(binMantisa[a])
    else:
        sumar = 23 - len(binMantisa)
        for a in range(len(binMantisa)):
            arreglo32.append(binMantisa[a])

        for a in range(sumar):
            arreglo32.append(0)

    if len(binMantisa) >= 53:
        for a in range(53):
            arreglo64.append(binMantisa[a])
    else:
        sumar = 53 - len(binMantisa)
        for a in range(len(binMantisa)):
            arreglo64.append(binMantisa[a])

        for a in range(sumar):
            arreglo64.append(0)

    asd = ''
    asd2 = ''
    for i in range(len(arreglo32)):
        if i == 1:
            asd += " "
        elif i == 9:
            asd += " "
        asd += str(arreglo32[i])

    for i in range(len(arreglo64)):
        if i == 1:
            asd2 += " "
        elif i == 12:
            asd2 += " "
        asd2 += str(arreglo64[i])
    arregloSal=[]
    # valor 32 bits
    # signo
    # eXponente
    # valor 64
    arregloSal.append(asd)

    arregloSal.append(asd2)
    return arregloSal
def ieeeInverso(numero):
    numeroDec = ' '

    def binarioDecimal(numero_binario):  # Cambiar
        numero_decimal = 0
        for posicion, digito_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion
        return numero_decimal

    def binarioFraccionario(aux):
        numi = 0
        num2 = aux
        cant = len(num2)
        for i in range(cant):
            numi = numi + (int(num2[0 + i:i + 1]) * (1 / (2 ** (i + 1))))
            numi = float(numi)
        return round(float(numi), 30)

    if len(numero) <= 32:
        aux = 0
        auxExpo = ''
        if numero[0] == 0:
            numeroDec += ""
            aux += 1
        else:
            numeroDec += "-"
            aux += 1

        for i in range(aux, 9):
            auxExpo += str(numero[i])

        aux += 8
        auxExpo = binarioDecimal(auxExpo)
        auxExpo += -127
        entero = ""
        fraccion = ""

        for j in range(aux, aux + auxExpo + 1):
            entero += str(numero[j])
        aux += auxExpo + 1

        for k in range(0, len(numero)):
            fraccion += str(numero[k])
        entero = binarioDecimal(entero)
        fraccion = binarioFraccionario(fraccion)
        numeroDec = float(entero) + float(fraccion)

    else:
        aux = 0
        auxExpo = ''
        if numero[0] == 0:
            numeroDec += ""
            aux += 1
        else:
            numeroDec += "-"
            aux += 1

        for i in range(aux, 12):
            auxExpo += numero[i]
        aux += 11
        auxExpo = binarioDecimal(auxExpo)
        auxExpo += -1023
        entero = ""
        fraccion = ""

        for j in range(aux, aux + auxExpo + 1):
            entero += str(numero[j])
        aux += auxExpo + 1

        for k in range(aux, len(numero)):
            fraccion += str(numero[k])
        entero = binarioDecimal(entero)
        fraccion = binarioFraccionario(fraccion)

        numeroDec = float(numeroDec + str(float(entero) + float(fraccion)))

    return numeroDec


#print(ieeeInverso('000010101'))
#ieee(78563.3084)
