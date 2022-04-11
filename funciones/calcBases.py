def control():
    opcion = 0
    while opcion != 5:

        print("--> En que base se encuentra: ")
        opcion = input("1) Decimal \n2) Binario \n3) Octagonal \n4) Hexadecimal\n5) Salir\n")
        num = input("--> Digita el numero a convertir: ")
        if opcion == "1":
            algoritmoAbase(num, 2)
            algoritmoAbase(num, 8)
            algoritmoAbase(num, 16)
            return
        elif opcion == "2":
            aux = algoritmoAdecimal(num, 2)
            algoritmoAbase(aux, 8)
            algoritmoAbase(aux, 16)
            return
        elif opcion == "3":
            aux = algoritmoAdecimal(num, 8)
            algoritmoAbase(aux, 2)
            algoritmoAbase(aux, 16)
            return
        elif opcion == "4":
            aux = algoritmoAdecimal(num, 16)
            algoritmoAbase(aux, 2)
            algoritmoAbase(aux, 8)
            return
        elif opcion == "5":
            return
        else:
            print('marca una opcion valida')


def algoritmoAbase(numero, base):
    numero = float(numero)
    partEntera = int(numero)
    aux = str(numero).split('.')
    parteDecimal = '0.' + str(aux[1])

    def remplazo16(num):
        num = int(num)
        if num == 10:
            return 'A'
        elif num == 11:
            return 'B'
        elif num == 12:
            return 'C'
        elif num == 13:
            return "D"
        elif num == 14:
            return "E"
        elif num == 15:
            return "F"
        else:
            return str(num)

    def traduccionPartEntera():
        msj = ""
        num = partEntera

        fin = False
        while fin == False:
            residuo = num // base
            concatenar = num % base
            num = residuo
            msj = remplazo16(concatenar) + msj + ""
            if residuo == 0:
                fin = True
        return (msj)

    def traduccionParteDecimal():
        msj = ""
        num = str(parteDecimal)
        auxiliar = float(num)
        for i in range(0, len(parteDecimal)):
            operacion = auxiliar * base
            msj = msj + "" + str(remplazo16(int(operacion)))
            decimal = str(operacion).split('.')
            auxiliar = float("0." + decimal[1])
        return msj
    msj=traduccionPartEntera()+traduccionParteDecimal()

    if parteDecimal != '0.0' or parteDecimal != "0.0":
        #print('--->',str(traduccionPartEntera())+'.'+str( traduccionParteDecimal()))
        return str(traduccionPartEntera())+'.'+str( traduccionParteDecimal())
    else:
        #print('--->',str(traduccionPartEntera()))
        return str(traduccionPartEntera())


def algoritmoAdecimal(numero, base):
    if base != 16:
        numero = float(numero)
        auxi = str(numero).split('.')
        partEntera = auxi[0]
        parteDecimal = auxi[1]
    else:
        try:
            auxi = str(numero).split('.')
            partEntera = auxi[0]
            parteDecimal = auxi[1]
        except:

            partEntera = numero
            parteDecimal = '0.0'

    def remplazo16(num):
        if num == "A" or num == "a":
            return "10"
        elif num == "B" or num == "b":
            return "11"
        elif num == "C" or num == "c":
            return "12"
        elif num == "D" or num == "d":
            return "13"
        elif num == "E" or num == "e":
            return "14"
        elif num == "F" or num == "f":
            return "15"
        else:
            return num

    def traduccionEntero(aux):
        transf = str(aux)
        s = str(transf[::-1])
        resultado = 0

        for i in range(0, len(s)):
            conver = remplazo16(s[i])
            resultado += (base ** i) * int(conver)
        return resultado

    def traduccionDecimal(aux):
        transf = str(aux)
        s = str(transf[::-1])
        resultado = 0
        for i in range(0, len(s)):
            conver = remplazo16(s[i])
            resultado += (base ** i) * int(conver)
        return resultado

    if parteDecimal != '0.0':
        devolucion = str(traduccionEntero(partEntera)) + '.' + str(traduccionDecimal(parteDecimal))
        #print('El numero ', numero, ' en base 10  es : ', devolucion)
        return devolucion
    else:
        devolucion = str(traduccionEntero(partEntera))
        #print('El numero ', numero, ' en base 10 es : ', devolucion)
        return devolucion


