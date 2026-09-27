'''
Práctica 02 — Slicing, operaciones y dtype con NumPy

Objetivo

Seguir practicando slicing y observar qué ocurre con
el tipo de dato cuando realizamos operaciones sobre
un array.

Usá esta matriz:

10   20   30   40
50   60   70   80
90  100  110  120

Consigna

1. Crear la matriz con NumPy.
2. Mostrar su shape.
3. Mostrar su dtype.
4. Seleccionar las columnas de índices 1 y 2
   para todas las filas.
5. Dividir los valores seleccionados entre 10.
6. Mostrar el resultado.
7. Observar el dtype del nuevo array.
8. Comprobar que la matriz original no cambió.

Idea clave

El slicing permite seleccionar regiones completas
de un array sin recorrerlo elemento por elemento.

También es importante observar que una operación puede
producir un array con un dtype diferente al original.
'''
import numpy as np

def main ():
    matriz = np.array([[10,   20,   30,   40],
                       [50,   60,   70,   80],
                       [90,  100,  110,  120]]) 
    print(f"shape: {matriz.shape}")
    print(f"dtype: {matriz.dtype}")
    
    #columnas 1 y 2 de todas las filas
    print(matriz[:,1:3])
    res = matriz[:,1:3]/10
    print(res)
    print(f"dtype: {res.dtype}")
    print(matriz)

if __name__ == "__main__":
    main()