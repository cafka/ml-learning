'''
Marco general
Para operar arrays de shapes diferentes, NumPy:
1. alinea sus dimensiones desde la derecha;
2. compara todos los pares de dimensiones;
3. cada par es compatible si:
   - ambas dimensiones son iguales, o
   - una de ellas vale 1;
4. si a un array le faltan dimensiones a la izquierda, para esta comparación se consideran dimensiones de tamaño 1;
5. si algún par no cumple la regla, la operación falla.
Broadcasting determina cómo pueden combinarse los shapes. 
No determina qué hace matemáticamente la operación. 
Por eso hoy usamos resta en vez de suma.
Datos
import numpy as np

columna = np.array([[5],[10],[15]])
fila = np.array([1, 2, 4, 8])

Antes de ejecutar
Escribí comentarios con tu predicción para las dos expresiones:
columna - fila 
fila - columna

Para cada una, razoná:
- shape de columna;
- shape de fila;
- si son compatibles por broadcasting;
- qué shape tendría el resultado;
- si esperás que ambas restas produzcan los mismos valores o no, y por qué.
No calcules los números a mano.
Objetivo
Después de escribir tus predicciones, hacé que el programa calcule ambas restas.
Mostrá:
- los dos arrays originales y sus shapes;
- el resultado de columna - fila y su shape;
- el resultado de fila - columna y su shape.
Finalmente, compará lo que ocurrió con lo que habías predicho en los comentarios.
Restricciones
No uses reshape, tile, repeat, newaxis ni bucles. No construyas manualmente las matrices resultantes.
'''

import numpy as np

columna = np.array([[5],[10],[15]]) #shape (3,1)
fila = np.array([1, 2, 4, 8]) #shape (4,)

# 4 es compatible con 1 y 1 es compatible con 3
# el resultado tendrá shape 3,4 en caso de columna - fila 
# y shape 4,3 en caso de fila - columna, en este caso 4 es compatible con 1 y 1 es compatible con 3
# la resta no es conmutativa por lo que esperaría resultados diferentes
print(columna, columna.shape)
print("=======================")
print(fila, fila.shape)
print("=======================")
resta1 = columna - fila
print(resta1, resta1.shape)
print("=======================")
resta2 = fila - columna
print(resta2, resta2.shape)

