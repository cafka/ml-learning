'''
Práctica 21 — Indexación booleana en NumPy

Concepto nuevo
La indexación booleana permite seleccionar elementos de un array utilizando condiciones lógicas.

En NumPy, una comparación sobre un array produce una máscara de valores True y False.

Por ejemplo:
import numpy as np
datos = np.array([[4, 9, 2],[7, 1, 8]])
mascara = datos > 5

La máscara conserva el shape (2, 3):
[[False,  True, False],
 [ True, False,  True]]

Al utilizar una máscara booleana del mismo shape que el array para seleccionar elementos, 
NumPy devuelve los elementos seleccionados en un array 1D.

Una distinción importante: una máscara booleana completa no funciona igual que seleccionar filas mediante una máscara 1D. 
En el segundo caso se conserva la estructura de las dimensiones no seleccionadas.

Las máscaras deben tener dimensiones compatibles con los ejes que indexan. 
No se aplican automáticamente todas las reglas de broadcasting que ya estudiaste.
Objetivo de código
Tenemos mediciones de tres sensores durante cuatro momentos:
import numpy as np
mediciones = np.array([[12, 25,  8],[30, 15, 22],[18, 35, 10],[27,  9, 40]])

Queremos construir un array que contenga únicamente las filas en las que al menos una medición sea mayor que 30.

El resultado debe conservar las tres columnas originales y el orden de las filas.
Restricciones
- No usar bucles for ni while.
- No modificar mediciones.
- Utilizar operaciones de NumPy.
- Construir la selección mediante una condición booleana.
Tu trabajo
En GitHub Codespaces, escribí el código completo de esta práctica.

Antes de ejecutarlo, incluí como comentarios tus predicciones sobre el shape de la máscara que utilizarás 
para seleccionar filas y el shape del array resultante.

Para comprobarlo, imprimí el resultado y su .shape, sin utilizar valores esperados escritos manualmente como solución.
'''
import numpy as np

mediciones = np.array([[12, 25,  8],[30, 15, 22],[18, 35, 10],[27,  9, 40]])
#mascara tiene el mismo shape que mediciones: (4,3)
mascara = mediciones > 30
#quiero obtener el indice de fila con algun elemento en true

print(mascara)

filas_true = np.any(mascara, axis = 1)
print(filas_true) #shape (4,)
print(mediciones[filas_true]) #shape (2,4)
