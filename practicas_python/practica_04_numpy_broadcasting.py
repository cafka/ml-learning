'''
Práctica 04 — Broadcasting básico con NumPy

Objetivo

Introducir el concepto de broadcasting y observar cómo
NumPy puede operar con arrays de formas diferentes cuando
sus dimensiones son compatibles.

Usá esta matriz:

10   20   30   40
50   60   70   80
90  100  110  120

Y este array de una dimensión:

1  2  3  4

Consigna

1. Crear ambos arrays con NumPy.
2. Mostrar el shape de cada uno.
3. Sumarlos directamente, sin usar for.
4. Guardar el resultado en una nueva variable.
5. Mostrar el resultado.
6. Mostrar el shape del resultado.
7. Explicar qué hizo NumPy con el array
   de shape (4,).

No usar reshape ni tile.

Idea clave

La matriz tiene shape (3, 4) y el otro array tiene
shape (4,).

NumPy compara las dimensiones desde la derecha.
Como los valores 4 coinciden, puede aplicar el array
de cuatro elementos a cada fila de la matriz.

A este mecanismo se lo llama broadcasting.
'''

import numpy as np

def crear_matriz() -> np.ndarray:
    return (np.array([[10, 20, 30, 40],
             [50, 60, 70, 80],
             [90, 100, 110, 120]]))

def main():
    matriz = crear_matriz()
    arreglo = np.array([1, 2, 3, 4])
    print(f"shape matriz: {matriz.shape}")
    print(f"shape arreglo: {arreglo.shape}")
    suma = matriz + arreglo
    print(f"suma = {suma} - shape = {suma.shape}")
    #Lo que hizo el broadcasting fue esto conceptualmente: 
    #matriz:    (3, 4)
    #arreglo:   (4,)
    #NumPy compara las dimensiones desde la derecha. Encuentra que el 4 coincide con el 4, así que puede aplicar:
    #[1 2 3 4]
    #a cada una de las tres filas:
    #10   20   30   40     +    1  2  3  4
    #50   60   70   80     +    1  2  3  4
    #90  100  110  120     +    1  2  3  4

if __name__ == "__main__": 
    main()