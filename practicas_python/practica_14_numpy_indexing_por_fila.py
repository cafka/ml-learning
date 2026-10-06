'''
Práctica 14 — selección por fila con indexing avanzado

La habilidad nueva es aprender a seleccionar un elemento distinto de cada fila usando índices. 
Esto aparece mucho en NumPy y es importante para CS231n porque permite trabajar con etiquetas, scores y selecciones 
por ejemplo sin escribir loops de Python.
Usá estos datos:
scores = np.array([    [0.2, 1.4, 0.7],    [2.1, 0.3, 1.2],    [0.5, 0.8, 1.9],    [1.7, 1.1, 0.4]])
clases = np.array([1, 0, 2, 1])

Interpretación:
- cada fila de scores corresponde a un ejemplo;
- cada columna corresponde a una clase;
- clases[i] indica qué columna interesa tomar en la fila i.
Tu objetivo es obtener un vector con un score por fila, usando para cada fila la columna indicada por clases.
Mostrá:
- scores.shape;
- clases.shape;
- el vector resultante;
- el shape del vector resultante.
Restricciones
- no uses for;
- no selecciones las filas manualmente una por una;
- usá indexing de NumPy.
Antes de ejecutar
Escribí un comentario explicando qué relación debería existir entre:
fila i de scores
clases[i]
resultado[i]

Como comprobación, verificá que el resultado tenga un solo valor por cada fila de scores.
No te doy la sintaxis exacta del indexing avanzado. Hacé tu intento y lo revisamos.
'''
import numpy as np

def main():
    scores = np.array([[0.2, 1.4, 0.7],    
                       [2.1, 0.3, 1.2],    
                       [0.5, 0.8, 1.9],    
                       [1.7, 1.1, 0.4]])
    
    clases = np.array([1, 0, 2, 1])
    

if __name__ == "__main__":
    main()