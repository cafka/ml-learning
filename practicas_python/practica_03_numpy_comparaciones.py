'''
Práctica 03 — Comparaciones y máscaras booleanas en NumPy

Objetivo

Aprender qué ocurre cuando se compara un array completo
contra un valor, en lugar de comparar manualmente cada
elemento.

Usá esta matriz:

12   80  150  220
35  125   90  255
180  60  110   40

Consigna

1. Crear la matriz con NumPy.
2. Mostrar el array completo.
3. Mostrar su shape y su dtype.
4. Comparar todo el array con el valor 100.
5. Guardar el resultado de la comparación.
6. Mostrar la máscara booleana obtenida.
7. Mostrar el dtype de la máscara.
8. Usar la máscara para seleccionar solamente
   los valores mayores que 100.
9. Contar cuántos valores cumplen la condición.

Restricción

No usar for.

Idea clave

Una comparación vectorizada devuelve un array de valores
True y False con la misma forma que el array original.

Ese array booleano puede usarse como máscara para
seleccionar solamente las posiciones que cumplen
la condición.
'''
import numpy as np


def crear_array()-> np.ndarray:
    return np.array([[12, 80, 150, 220],
              [35, 125, 90, 255],
              [180, 60, 110, 40]])

def main():
    ''' 1. Mostrá el array.
        2. Mostrá su shape y su dtype.
        3. Compará todo el array con el valor 100 para saber qué elementos son mayores que 100.
        4. Guardá el resultado de esa comparación en una variable.
        5. Mostrá esa variable y observá qué dtype tiene.
        6. Usá esa variable para obtener solamente los valores del array original que sean mayores que 100.
        7. Mostrá cuántos valores cumplen la condición.
        Restricción importante
        No uses for.'''
    matriz = crear_array()
    print(matriz)
    print(f"Shape: {matriz.shape}")
    print(f"dtype: {matriz.dtype}")
    mayor_100 = matriz > 100
    print(f"dtype de mayor_100: {mayor_100.dtype}")
    print(f"mascara mayores a 100:\n {mayor_100}")
    valores_mayores_100 = matriz[mayor_100]
    print(f"selecciono solo mayores a 100: {valores_mayores_100}")
    print(f"cantidad de elementos mayores a 100: {np.count_nonzero(mayor_100)}")

if __name__ == "__main__":
    main()