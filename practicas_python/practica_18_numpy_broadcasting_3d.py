'''
Práctica 18 — broadcasting entre arrays de distinta dimensionalidad

La habilidad que vamos a comprobar es si podés trasladar el razonamiento de broadcasting a arrays de más dimensiones, 
entendiendo qué representa cada eje y qué valores se reutilizan.
Usá estos datos:
import numpy as np
A = np.array([[[10, 20, 30, 40]], [[50, 60, 70, 80]]])
B = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

Tu único objetivo es calcular:
A + B

usando directamente NumPy, sin modificar previamente ninguno de los dos arrays.
Antes de ejecutar, dejá comentarios donde indiques:
- el shape que esperás para A;
- el shape que esperás para B;
- cómo los alineás para aplicar las reglas de broadcasting;
- el shape que predecís para el resultado;
- en qué eje o ejes esperás que NumPy tenga que reutilizar valores de A y de B.
Después mostrá A, B, sus shapes, el resultado completo y su shape.
Restricciones
No uses reshape, newaxis, expand_dims, tile, repeat ni bucles. El objetivo es observar broadcasting puro.
Comprobación de comprensión
Después de ejecutar, elegí una posición cualquiera del resultado, por ejemplo una posición [i, j, k], 
y escribí como comentario de qué elemento de A y de qué elemento de B salió esa suma.
'''
import numpy as np

def main():
    A = np.array([[[10, 20, 30, 40]], [[50, 60, 70, 80]]])
    B = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(f"A.shape = {A.shape}") # (2,1,4)
    print(f"B.shape = {B.shape}") # (3,4)
    print(A)
    print("===========================")
    print(B)
    # son compatibles. De derecha a izquierda: 4 con 4, 3 con 1, 1 con 2
    # shape del resultado: (2,3,4), broadcasting debería repetir filas en ambas matrices de la matriz A
    # de modo que cada una tenga shape (3,4)
    suma = A + B
    print (f"suma = {suma} - shape = {suma.shape}")
    # lo siguiente lo pensé así: el 0 indica la primer matriz y dentro de ella el elemento que está en la posicion (1,3)
    # que en la matriz A con broadasting previo a sumar sería el 40 y en la matriz B el 8 ya que estamos trabajando con la segunda fila
    print(f"elemento [0,1,3] = 48? = {suma[0,1,3]}")

if __name__ == "__main__":
    main()