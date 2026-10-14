'''
Un dispositivo registra seis mediciones consecutivas. 
Los datos llegan como un array unidimensional, pero necesitamos poder representarlos también como una fila o como una columna.
Usaremos estos datos:
import numpy as np

def main():    
    mediciones = np.array([12.5, 13.0, 12.8, 13.4, 12.9, 13.1])

if __name__ == "__main__":    
    main()

Objetivo
A partir de mediciones, construí dos nuevos arrays:
- mediciones_fila: una matriz de shape (1, 6).
- mediciones_columna: una matriz de shape (6, 1).
Los valores deben conservarse en el mismo orden. No debés modificar el array original.
Resultados que debe mostrar el programa
Imprimí el contenido y el shape de los tres arrays: el original, 
la representación como fila y la representación como columna.
Además, imprimí los shape que resultan de aplicar .T al array original y a la matriz mediciones_columna.
Restricciones
No utilices bucles de Python ni construyas manualmente nuevas listas con los valores. 
Las dos representaciones deben obtenerse a partir del array original mediante operaciones de NumPy.
Antes de ejecutar
Escribí un comentario en tu código donde expliques brevemente:
1. Qué diferencia estructural hay entre (6,), (1, 6) y (6, 1).
2. Qué esperás que ocurra al aplicar .T a un array de una dimensión y a una matriz de dos dimensiones.
Después ejecutá y comprobá si tus predicciones coinciden con los resultados.
'''

import numpy as np

def main():    
    mediciones = np.array([12.5, 13.0, 12.8, 13.4, 12.9, 13.1])
    # mediciones es un vector de numpy de shape (6,)
    print(mediciones.shape)
    # construí dos nuevos arrays:
    # mediciones_fila: una matriz de shape (1, 6).
    # mediciones_columna: una matriz de shape (6, 1).
    mediciones_fila = np.array([mediciones])
    print(mediciones_fila.shape)
    
    mediciones_columna = mediciones_fila.reshape(6,1)
    print(mediciones_columna.shape)
    #otra forma de obtener mediciones_columna
    mediciones_columna = mediciones_fila.T
    print(mediciones_columna.shape)

    #print(mediciones.T)
    #print(mediciones.T.shape)
    #1. Qué diferencia estructural hay entre (6,), (1, 6) y (6, 1).
    # (6,) es un array de una dimensión con 6 elementos, (1, 6) es una matriz de una fila y 6 columnas y (6, 1) es una matriz de 6 filas y una columna
    #2. Qué esperás que ocurra al aplicar .T a un array de una dimensión y a una matriz de dos dimensiones.
    # aplicar .T a un array de una dimensión creí que pasaba de un vector fila a un vector columna pero vi que el vector queda igual
    # transponer una matriz de dos dimensiones debería pasar de matriz: filas x columnas a columnas x filas

    print(f"mediciones.T.shape = {mediciones.T.shape}")
    print(f"mediciones_columna.T.shape = {mediciones_columna.T.shape}")

if __name__ == "__main__":    
    main()
