'''
Práctica 24 — Producto matricial en NumPy
Concepto nuevo: multiplicación matricial
Hasta ahora realizamos operaciones elemento a elemento, reducciones y broadcasting.

El producto matricial es diferente: combina filas de una matriz con columnas de otra, mediante productos y sumas.
El producto completo es:
A @ B

Y produce:
[[ 5 13]
 [14 31]]

Su shape es (2, 2).

Atención: @ no es equivalente a *. 
En NumPy, * realiza multiplicación elemento a elemento, mientras que @ realiza multiplicación matricial. 
También existe np.matmul() para esta operación.

Como contraejemplo, intentar A @ A con la matriz anterior produce un error, porque las dimensiones interiores serían 3 y 2, que no coinciden.
Objetivo de código
En un taller tenemos tres lotes de producción. Cada uno utiliza cantidades de cuatro materiales diferentes:
import numpy as np

lotes = np.array([[2, 0, 1, 3],[0, 4, 2, 1],[3, 1, 0, 2]])
caracteristicas = np.array([[5, 2],[3, 1],[8, 4],[2, 3]])

Cada fila de caracteristicas corresponde a uno de los cuatro materiales. 
La primera columna indica el costo por unidad y la segunda el peso por unidad.

Tu objetivo: construir una matriz que contenga, para cada lote, su costo total y su peso total.

Restricciones: no utilizar bucles, no modificar los arrays originales y realizar la operación mediante multiplicación matricial.

Antes de ejecutar, escribí comentarios indicando los shapes originales, si el producto es compatible y el shape que esperás obtener. 
Después imprimí la matriz resultante y su .shape.
Conexión con CS231n y las redes neuronales
El producto matricial es una operación fundamental del álgebra lineal utilizada en machine learning. 
Comprender cómo combina dimensiones y valores es un prerrequisito para estudiar las transformaciones que realizan las capas de una red neuronal.

En esta práctica nos concentramos exclusivamente en dominar la operación matemática y su implementación en NumPy. 

Ahora te toca programarlo en Codespaces. La Práctica 24 queda abierta hasta revisar tu intento y tus predicciones.
'''

import numpy as np


def main():
    lotes = np.array([[2, 0, 1, 3],[0, 4, 2, 1],[3, 1, 0, 2]])
    caracteristicas = np.array([[5, 2],[3, 1],[8, 4],[2, 3]])
    print(lotes.shape) #shape esperado (3,4)
    print(caracteristicas.shape) #shape esperado (4,2)
    # shape de resultado de producto matricial (3,2) Los 3 lotes con sus costos y pesos
    resultado = lotes@caracteristicas
    print(resultado, resultado.shape)

if __name__== "__main__":
    main()