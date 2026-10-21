'''
Práctica 22 — Indexación avanzada (fancy indexing) en NumPy

Concepto nuevo
En la práctica anterior utilizaste una máscara booleana para seleccionar filas. 
Ahora conoceremos otra modalidad: seleccionar posiciones mediante índices enteros.

La diferencia fundamental es que los índices enteros permiten elegir posiciones concretas, cambiar su orden e incluso repetirlas.

Por ejemplo:
import numpy as np
datos = np.array([[11, 12],[21, 22],[31, 32],[41, 42]])
indices = np.array([3, 0, 3])
seleccion = datos[indices]

Aquí seleccionamos la cuarta fila, después la primera y nuevamente la cuarta.

El resultado es:
[[41 42]
 [11 12]
 [41 42]]

Shape: (3, 2).

A diferencia de una máscara booleana, los índices enteros pueden repetir filas y determinar explícitamente su orden.

También hay dos formas de utilizar índices enteros en una matriz 2D que no significan lo mismo:
filas = np.array([0, 2])
columnas = np.array([1, 0])
datos[filas, columnas]  

# Selección por pares de coordenadasdatos
# [np.ix_(filas, columnas)]  
# Todas las combinaciones de esas filas y columnas

La primera selecciona dos elementos: (0,1) y (2,0). Su shape es (2,).

La segunda selecciona una submatriz de dos filas y dos columnas. Su shape es (2,2).

Los índices deben existir dentro de las dimensiones correspondientes. 
Por ejemplo, intentar seleccionar la fila 8 de una matriz con cuatro filas provoca un IndexError. 
Los índices negativos también son válidos y cuentan desde el final.
Tu objetivo de código
Un laboratorio registró cuatro observaciones de tres variables:
import numpy as np

registros = np.array([[14, 23, 32],[45, 54, 63],[76, 85, 94],[17, 26, 35]])

Necesitamos construir una nueva matriz con las observaciones originales en este orden:

tercera observación, primera observación, cuarta observación y nuevamente tercera observación.

Además, de cada observación queremos conservar las variables en este orden: tercera, primera y segunda.

El resultado debe conservar su estructura 2D.
Restricciones y comprobaciones
- No utilizar bucles.
- No modificar registros.
- Utilizar indexación mediante índices enteros.
- No construir manualmente la matriz resultante.
- Imprimir el resultado y su .shape.
- Antes de ejecutar, escribir como comentario qué shape esperás y por qué.
Es un solo objetivo: reorganizar filas y columnas de una matriz mediante indexación avanzada.

No te indicaré cómo escribir la selección. Quiero ver qué herramientas elegís por tu cuenta y cómo razonás el shape.
'''
import numpy as np

def main():
    #Necesitamos construir una nueva matriz con las observaciones originales en este orden:
    #tercera observación, primera observación, cuarta observación y nuevamente tercera observación.

    registros = np.array([[14, 23, 32],[45, 54, 63],[76, 85, 94],[17, 26, 35]])
    filas = np.array([2,0,3,2])
    # shape que espero: (4,3) - selecciono 4 filas de la matriz original manteniendo sus columnas
    matriz_orden = registros[filas]
    print(matriz_orden)
    #Además, de cada observación queremos conservar las variables en este orden: tercera, primera y segunda.
    columnas = np.array([2,0,1]) #shape que espero: (4,3) no cambian la cantidad de columnas sino su orden
    resultado = matriz_orden[:,columnas]
    print(resultado, resultado.shape)
   

if __name__ == "__main__":
    main()
