#!/usr/bin/env python 3

import numpy as np

#-----------funcion que calcula los puntos de muestreo y los pesos

def gaussxw(N):
    """Retorna los puntos de muestro x_k y sus respectivos pesos w_k para el polinomio de Legendre de orden N en el intervalo [-1, 1]

    Examples:
        >>> gaussxw(2)
        (array([-0.57735027,  0.57735027]), array([1., 1.]))

    Args:
        N (int): Argumento unico. Indica el orden del Polinomio de Legendre.

    Returns:
          (tuple): Tupla con dos `numpy.ndarray`: x(puntos d muestreo x_k) y w (pesos w_k)

    """

    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

#------------funcion que escala al intervalo en cuestion

def gaussxwab (a, b, x, w):
    """Escala los valores de muestro y sus pesos del intervalo [-1, 1] al intervalo de interes

    Examples:
        >>> gaussxwab(1.0, 3.0, gaussxw(2)[0], gaussxw(2)[1])
        (array([1.42264973, 2.57735027]), array([1., 1.]))

    Args:
        a (float): Limite inferior de interalo de interes
        b (float): Limite superior del intervalo de interes
        x (numpy.ndarray): Valores de muestros x_k
        w (numpy.ndarray): Pesos w_k para los x_k

    Returns:
          (tuple): Contiene los `numpy.ndarray` x y w, que a su vez contienes los  valores de x_k y w_k escalados en el intervalo de interes
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

#----calculo de los puntos de muestreo y los pesos segun el orden de interes

n2 = gaussxw(2)
print(n2)

n3 = gaussxw(3)
print(n3)

n4 = gaussxw(4)
print(n4)

n5 = gaussxw(5)
print(n5)

#------------escalado al intervalo de interes
# [1, 3] en nuestro caso

escalado_n2 = gaussxwab(1.0, 3.0, n2[0], n2[1])
print(escalado_n2)

escalado_n3 = gaussxwab(1.0, 3.0, n3[0], n3[1])
print(escalado_n3)

escalado_n4 = gaussxwab(1.0, 3.0, n4[0], n4[1])
print(escalado_n4)

escalado_n5 = gaussxwab(1.0, 3.0, n5[0], n5[1])
print(escalado_n5)

#-----------integrando de interes

def integrando(x):
    """ Contiene la funcion cuya integral deseamos aproximar y la evalua en x

    Examples:
        >>> integrando(2.0)
        4.0

    Args:
        x (float): Valor en el que se desea evaluar la funcion

    Returns:
        funcEval (float): Valor de la funcion evaluada en `x`



    """
    funcEval = x**6 - x**2 * np.sin(2*x)
    return funcEval

#----------Aproximacion del integrando con cuadraturas Gaussianas

Int_n2 = np.sum(escalado_n2[1] * integrando(escalado_n2[0]))
print(Int_n2)

Int_n3 = np.sum(escalado_n3[1] * integrando(escalado_n3[0]))
print(Int_n3)

Int_n4 = np.sum(escalado_n4[1] * integrando(escalado_n4[0]))
print(Int_n4)

Int_n5 = np.sum(escalado_n5[1] * integrando(escalado_n5[0]))
print(Int_n5)

