import numpy as np
import sympy as sym


def ajusteCurvasGrado1CC(xi, yi, n):
    # PROCEDIMIENTO
    xi = np.array(xi, dtype=float)
    yi = np.array(yi, dtype=float)

    # sumatorias y medias
    xm = np.mean(xi)
    ym = np.mean(yi)
    sx = np.sum(xi)
    sy = np.sum(yi)
    sxy = np.sum(xi * yi)
    sx2 = np.sum(xi ** 2)
    sy2 = np.sum(yi ** 2)

    # coeficientes a0 y a1
    a1 = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
    a0 = ym - a1 * xm

    # polinomio grado 1
    x = sym.Symbol('x')
    f = a0 + a1 * x

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # coeficiente de correlación
    numerador = n * sxy - sx * sy
    raiz1 = np.sqrt(n * sx2 - sx ** 2)
    raiz2 = np.sqrt(n * sy2 - sy ** 2)
    r = numerador / (raiz1 * raiz2)

    # coeficiente de determinacion
    r2 = r ** 2

    # SALIDA
    return r


def ajusteCurvasGrado1(xi, yi, n):
    # PROCEDIMIENTO
    xi = np.array(xi, dtype=float)
    yi = np.array(yi, dtype=float)

    # sumatorias y medias
    xm = np.mean(xi)
    ym = np.mean(yi)
    sx = np.sum(xi)
    sy = np.sum(yi)
    sxy = np.sum(xi * yi)
    sx2 = np.sum(xi ** 2)
    sy2 = np.sum(yi ** 2)

    # coeficientes a0 y a1
    a1 = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
    a0 = ym - a1 * xm

    # polinomio grado 1
    x = sym.Symbol('x')
    f = a0 + a1 * x

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # coeficiente de correlación
    numerador = n * sxy - sx * sy
    raiz1 = np.sqrt(n * sx2 - sx ** 2)
    raiz2 = np.sqrt(n * sy2 - sy ** 2)
    r = numerador / (raiz1 * raiz2)

    # coeficiente de determinacion
    r2 = r ** 2

    # SALIDA
    return f


def ajusteCurvasGrado2CC(xi, yi, n):
    m = 2
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA
    return r


def ajusteCurvasGrado2(xi, yi, n):
    m = 2
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA
    return f


def ajusteCurvasGrado3(xi, yi, n):
    m = 3
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA
    return f


def ajusteCurvasGrado3CC(xi, yi, n):
    m = 3
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA

    return r


def ajusteCurvasGrado4(xi, yi, n):
    m = 4
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA
    return f


def ajusteCurvasGrado4CC(xi, yi, n):
    m = 4
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA

    return r


def ajusteCurvasGrado5(xi, yi, n):
    m = 5
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA

    return f


def ajusteCurvasGrado5CC(xi, yi, n):
    m = 5
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA
    return r


def ajusteCurvasGrado6(xi, yi, n):
    m = 6
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA

    return f


def ajusteCurvasGrado6CC(xi, yi, n):
    m = 6
    # procedimiento
    xi = np.array(xi)
    yi = np.array(yi)

    # llenar matriz a y vector B
    k = m + 1
    A = np.zeros(shape=(k, k), dtype=float)
    B = np.zeros(k, dtype=float)
    for i in range(0, k, 1):
        for j in range(0, i + 1, 1):
            coeficiente = np.sum(xi ** (i + j))
            A[i, j] = coeficiente
            A[j, i] = coeficiente
        B[i] = np.sum(yi * (xi ** i))

    # coeficientes, resuelve sistema de ecuaciones
    C = np.linalg.solve(A, B)

    # polinomio
    x = sym.Symbol('x')
    f = 0
    fetiq = 0
    for i in range(0, k, 1):
        f = f + C[i] * (x ** i)
        fetiq = fetiq + np.around(C[i], 4) * (x ** i)

    fx = sym.lambdify(x, f)
    fi = fx(xi)

    # errores
    ym = np.mean(yi)
    xm = np.mean(xi)
    errado = fi - yi

    sr = np.sum((yi - fi) ** 2)
    # syx = np.sqrt(sr / (n - (m + 1)))
    st = np.sum((yi - ym) ** 2)

    # coeficiente de determinacion
    r = (st - sr) / st

    # SALIDA
    return r


def ajusteCurvas(n):
    xi = []
    yi = []
    # INGRESO
    for a in range(n):
        xi.append(float(input('Digita el x: ')))
        yi.append(float(input('Digita el y: ')))

    ajusteCurvasGrado1(xi, yi, n)
    ajusteCurvasGrado2(xi, yi, n)
    ajusteCurvasGrado3(xi, yi, n)
    ajusteCurvasGrado4(xi, yi, n)
    ajusteCurvasGrado5(xi, yi, n)
    ajusteCurvasGrado6(xi, yi, n)


#n = int(input('Digita la cantidad de puntos: '))
#ajusteCurvas(n)
