'''
Práctica 23 — Incorporar nuevos ejes con np.newaxis
Concepto nuevo
Ya trabajamos con reshape, transposición y broadcasting. 
Ahora vamos a incorporar otra herramienta para controlar las dimensiones de un array: np.newaxis.

np.newaxis permite insertar un eje de longitud 1 en cualquier posición, sin cambiar los valores del array.

Por ejemplo:
import numpy as np

datos = np.array([[2, 4, 6],[8, 10, 12]])
ampliado = datos[:, np.newaxis, :]

El shape original es (2, 3) y el nuevo es (2, 1, 3).
Cómo cambian las dimensiones
Original
(2, 3)
2 ejes
Con nuevo eje
(2, 1, 3)
3 ejes

También podríamos insertar el nuevo eje al principio y obtener (1, 2, 3), o al final y obtener (2, 3, 1).

Puntos importantes:
- np.newaxis es equivalente a None cuando se utiliza dentro de una expresión de indexación.
- Introduce un eje de tamaño 1; no intercambia ejes como .T.
- Normalmente crea una vista, no una copia de los datos.
- Resulta especialmente útil para orientar arrays antes de aplicar broadcasting.
Contraejemplo: si transponemos datos, obtenemos (3, 2), no (2, 1, 3). 
La transposición reorganiza ejes existentes; np.newaxis agrega uno.
Objetivo de código
En un laboratorio tenemos tres sensores. Cada sensor registró cuatro mediciones:
import numpy as np
mediciones = np.array([[20, 22, 21, 23],[18, 19, 20, 17],[25, 27, 26, 24]])
correcciones = np.array([2, -1, 3])

Cada valor de correcciones corresponde a un sensor, siguiendo el orden de las filas de mediciones.

Queremos construir una nueva matriz en la que a cada medición se le reste la corrección correspondiente a su sensor.

Por ejemplo, la corrección del primer sensor debe aplicarse a sus cuatro mediciones.
Restricciones
No utilizar bucles, no modificar mediciones y no utilizar reshape. 
En esta práctica quiero que utilices np.newaxis y broadcasting.

Antes de ejecutar, dejá comentarios con los shapes que esperás para el array 
de correcciones después de incorporar el nuevo eje y para la matriz resultante.

Imprimí el resultado final y su .shape.
Conexión con CS231n
Estamos entrenando la capacidad de controlar explícitamente las dimensiones para realizar operaciones vectorizadas. 
Es una habilidad fundamental para manipular tensores, preparar datos y trabajar posteriormente con redes neuronales. 
Las decisiones concretas de implementación de tus assignments siguen siendo tuyas.

No te voy a indicar dónde insertar el nuevo eje: quiero comprobar si podés deducirlo a partir de las dimensiones y de la operación que necesitás.
'''
import numpy as np

def main():
    mediciones = np.array([[20, 22, 21, 23],[18, 19, 20, 17],[25, 27, 26, 24]])
    correcciones = np.array([2, -1, 3])
    #mediciones tiene shape (3,4)
    #correcciones tiene shape (3,)
    print(correcciones, correcciones.shape)
    corrector = correcciones[:, np.newaxis] #shape esperado (3,1)
    resta = mediciones - corrector # resta va a tener shape (3,4)
    print(resta, resta.shape)
    print("===========================")
    print(mediciones, mediciones.shape) 
    print("===========================")
    print(corrector, corrector.shape)


if __name__=="__main__":
    main()