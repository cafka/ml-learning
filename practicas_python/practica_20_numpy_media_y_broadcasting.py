'''
Práctica 20 — reducción y broadcasting sobre ejes distintos

Acá no agregamos una regla nueva. 
Quiero comprobar si podés combinar por tu cuenta dos cosas que ya practicamos: reducción por ejes y broadcasting.
Usá:
import numpy as np

X = np.array([[[10, 20, 30], [40, 50, 60]], [[15, 25, 35],[45, 55, 65]],[[20, 30, 40],[50, 60, 70]]])

X tiene tres dimensiones. 
Antes de ejecutar nada, escribí como comentarios qué representa cada eje según la estructura que ves y cuál es X.shape.
Objetivo
Calculá el promedio sobre axis=0 conservando ese eje con tamaño 1.
Después restale ese promedio a X directamente, dejando que NumPy determine si puede hacerlo mediante broadcasting.
Mostrá:
- X.shape;
- el array de promedios y su shape;
- el resultado de la resta y su shape.
Antes de ejecutar la resta
Dejá escrito como comentario:
X.shape            = ?
promedio.shape     = ?

y comprobá todos los pares de dimensiones, de derecha a izquierda, para predecir si la resta es compatible y qué shape debería producir.
Restricciones
No uses reshape, newaxis, expand_dims, tile, repeat ni bucles.
No calcules los promedios manualmente.
La comprobación importante esta vez es que razones primero sobre los tres ejes, no solo sobre el último par que resulte compatible.
'''

import numpy as np

X = np.array([[[10, 20, 30], [40, 50, 60]], [[15, 25, 35],[45, 55, 65]],[[20, 30, 40],[50, 60, 70]]])
# axis 0: 3
# axis 1: 2
# axis 2: 3
# X.shape = (3,2,3)
print(X)
print(f"X.shape = {X.shape}")
print("===============================")
prom = X.mean(axis = 0, keepdims = True)
print(prom)
print(f"prom.shape = {prom.shape}")
print("===============================")
# prom.shape = (1,2,3)
# broadcasting: para axis 1 y 2 las dimensiones son iguales, 
# y para la dimenion de mas a la izquierda es 1 contra 3
# por lo que son compatibles. Numpy debería replicar la primer fila a las dos siguientes 
resta = X - prom
print(resta)
print(f"resta.shape = {resta.shape}") #shape 3,2,3
