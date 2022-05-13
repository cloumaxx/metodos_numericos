import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
#funciona el txt

def traductor(msj):
    msj=msj.replace('e(','exp(')
    msj=msj.replace('exp(','exp(')
    msj = msj.replace('sin(', 'sin(')
    msj = msj.replace('sen(', 'sin(')
    msj = msj.replace('cos(', 'cos(')
    msj = msj.replace('tan(', 'tan(')
    msj = msj.replace('sec(', 'math.asin(')
    msj = msj.replace('csc(', 'math.acos(')
    msj = msj.replace('cot(', 'math.atan(')
    msj = msj.replace('ln(', 'math.log(')
    msj = msj.replace('π','math.pi')
    msj = msj.replace('√(', 'math.sqrt(')
    msj = msj.replace('√', 'math.sqrt(')
    msj = msj.replace('sqrt(', 'math.sqrt(')
    msj = msj.replace('^', '**')
    return msj

def monte_carlo(fx, a, b, N):
    fx=traductor(fx)
    x = sp.symbols('x')  # Crea variable x
    fx = sp.lambdify(x, fx)
    for _ in range(N):
        # Apply the approximation formula
        answer = (b-a)/N * fx(np.random.uniform(a,b,N)).sum()


    return answer


def grafica(fx, a, b, N):
    fx = traductor(fx)
    x = sp.symbols('x')  # Crea variable x
    fx = sp.lambdify(x, fx)
    areas =[]

    for _ in range(N):
        # Apply the approximation formula
        answer = (b-a)/N * fx(np.random.uniform(a,b,N)).sum()
        areas.append(answer)

    fig, ax = plt.subplots(figsize=(10,8))

    mu = np.array(areas).mean()
    sigma = np.array(areas).std()
    textstr = '\n'.join((
        f'$\mu=${mu:.2f}',
        f'$\sigma=${sigma:.2f}' ))

    ax.hist(areas, bins=31, ec='b')
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='blue', alpha=0.1)

    # place a text box in upper left in axes coords
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)
    plt.xlabel("Areas")
    plt.show()


funcion = "(x*x)-2*x"#input('digita la funcion: ')
intervaloa = 0.0#float(input('digita el intervalo A: '))
intervalob = 2.0#float(input('digita el intervalo B: '))
tramos = 100#int(input('digita los tramos: '))
#print(monte_carlo(funcion,intervaloa,intervalob,tramos))