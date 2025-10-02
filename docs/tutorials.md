# Ejemplo de uso

## Introduccion

Se aproxima el valor de la integral \( \int_1 ^3 dx \left[ x^6 - x^2\sin(2x)   \right] \) con el polinomio de Legendre de orden 2, \( P_2(x) \)

## Paso 1: Puntos de muestreo \( x_k  \) y pesos \( w_k \) para \( N = 2\) en el intervalo \( [-1, 1]\).

``` python
n2 = gaussxw(2)
print(n2)
(array([-0.57735027,  0.57735027]), array([1., 1.]))
```

## Paso 2: Escalado al intervalo de interes \( [1, 3]\)

``` python
escalado_n2 = gaussxwab(1.0, 3.0, n2[0], n2[1])
print(escalado_n2)
(array([1.42264973, 2.57735027]), array([1., 1.]))
```

## Paso 3: Evaluacion de la funcion con \( N = 2 \).

``` python
Int_n2 = np.sum(escalado_n2[1] * integrando(escalado_n2[0]))
print(Int_n2)
306.8199344959197
```
