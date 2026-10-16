'''
Práctica 17 — reshape con dimensión inferida

La habilidad nueva es usar -1 en reshape() para que NumPy infiera una dimensión sin que tengas que calcularla manualmente.
Usá:
import numpy as np
datos = np.array([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

Tu objetivo es crear, a partir de datos, dos arrays nuevos:
- uno con 3 columnas, dejando que NumPy calcule cuántas filas necesita;
- otro con 2 filas, dejando que NumPy calcule cuántas columnas necesita.
Antes de ejecutar, escribí como comentarios:
- datos.shape;
- qué shape esperás para cada nuevo array;
- cómo llegaste a esa predicción usando la cantidad total de elementos.
Después mostrá el contenido y el shape de los tres arrays.
Restricciones: no uses bucles, no construyas listas nuevas a mano y en cada reshape debe aparecer exactamente un -1.
Comprobación final: verificá que los tres arrays tengan la misma cantidad total de elementos, aunque sus shapes sean diferentes.
'''

import numpy as np

def main():
    '''
    Tu objetivo es crear, a partir de datos, dos arrays nuevos:
    - uno con 3 columnas, dejando que NumPy calcule cuántas filas necesita;
    - otro con 2 filas, dejando que NumPy calcule cuántas columnas necesita.
    Antes de ejecutar, escribí como comentarios:
    - datos.shape;
    - qué shape esperás para cada nuevo array;
    - cómo llegaste a esa predicción usando la cantidad total de elementos.
    '''
    datos = np.array([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])
    # datos.shape = (12,)
    array_3_columnas = datos.reshape(-1,3)
    #array_3_columnas.shape = (4,3)
    array_2_filas = datos.reshape(2,-1)
    #array_2_filas.shape = (2,6)
    # son 12 elementos en el array, si tiene 3 columnas tiene que tener 4 filas
    # y si tiene 2 filas debe tener 6 columnas
    print(f"datos.shape = {datos.shape} - size = {datos.size}")
    print(datos)
    print("====================================")
    print(f"array_3_columnas.shape = {array_3_columnas.shape} - size = {array_3_columnas.size}")
    print(array_3_columnas)
    print("====================================")
    print(f"array_2_filas.shape = {array_2_filas.shape} - size = {datos.size}")
    print(array_2_filas)
    print("====================================")

if __name__ == "__main__":
    main()