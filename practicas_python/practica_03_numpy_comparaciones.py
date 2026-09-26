'''
Objetivo
Aprender qué ocurre cuando comparás un array entero contra un valor, en vez de comparar elemento por elemento manualmente.
Esto después es muy útil con datos e imágenes: por ejemplo, seleccionar valores que cumplen determinada condición. Pero hoy trabajamos solamente con NumPy.
'''
import numpy as np


def crear_array()-> np.array:
    return np.array([[12, 80, 150, 220],
              [35, 125, 90, 255]
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
    mayor_100 = np.greater()