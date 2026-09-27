'''
Introducimos una idea nueva: broadcasting.
Tenés una matriz:
10   20   30   40
50   60   70   80
90  100  110  120

y otro array de una dimensión:
1   2   3   4

Consigna
1. Creá ambos arrays con NumPy.
2. Mostrá el shape de cada uno.
3. Sumá ambos arrays sin usar for.
4. Guardá el resultado en una nueva variable.
5. Mostrá el resultado y su shape.
6. Explicame con tus palabras qué creés que hizo NumPy con el array [1, 2, 3, 4].
Pauta mínima
Antes de programarlo, fijate:
- matriz: shape (3, 4)
- vector: shape (4,)
NumPy puede realizar ciertas operaciones entre arrays de formas distintas cuando sus dimensiones son compatibles. A eso se le llama broadcasting.
No uses reshape, tile ni otras funciones para forzarlo. Queremos observar primero el comportamiento natural de NumPy.
Escribilo vos y pasame código + salida. La parte que más me interesa esta vez es tu explicación del punto 6.
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