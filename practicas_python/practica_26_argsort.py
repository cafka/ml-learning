'''
Práctica 26 — Ordenación por índices con NumPy

Concepto nuevo: np.argsort()
Hasta ahora utilizaste indexación avanzada para seleccionar y reorganizar filas y columnas.

Ahora vamos a aprender cómo obtener los índices que permitirían ordenar un array.

La función np.argsort() no devuelve los valores ordenados: devuelve sus posiciones originales en el orden correspondiente.

Por ejemplo:
import numpy as np
valores = np.array([32, 8, 25, 14])
indices = np.argsort(valores)
print(indices)

Resultado:
[1 3 2 0]

¿Por qué?
- El menor valor es 8 y está en el índice 1.
- Después viene 14, en el índice 3.
- Después 25, en el índice 2.
- Finalmente 32, en el índice 0.
Podés utilizar esos índices para reorganizar otro array asociado a los mismos elementos, una ventaja importante de argsort.
Diferencia con np.sort()
Operación	Resultado
np.sort(valores)	[8, 14, 25, 32]
np.argsort(valores)	[1, 3, 2, 0]

Un límite importante: en arrays multidimensionales, np.argsort() ordena los índices a lo largo del eje indicado. 
Por defecto utiliza el último eje (axis=-1). No reorganiza automáticamente filas completas en función de una columna.

Cuando hay valores repetidos, sus índices aparecen en el resultado, 
pero no debés asumir un orden particular entre empates con el algoritmo predeterminado.

Objetivo de código
Una empresa registra cinco envíos.

Cada fila contiene tres datos, en este orden:
1. Identificador del envío.
2. Tiempo de entrega, en minutos.
3. Cantidad de paquetes.
import numpy as np
envios = np.array([[201, 48, 3],[202, 15, 7],[203, 32, 2],[204, 24, 5],[205, 41, 4]])

Queremos obtener una nueva matriz donde los envíos estén ordenados de menor a mayor tiempo de entrega, conservando todos los datos de cada envío.
Restricciones
- Utilizar np.argsort().
- No utilizar bucles.
- No modificar envios.
- No construir manualmente la matriz resultante.
- Reutilizar las herramientas de indexación que ya estudiaste.
Antes de ejecutar, escribí como comentarios qué shape esperás para los índices de ordenación y para la matriz resultante.

Después imprimí el resultado, su .shape y el array original para comprobar que no cambió.
Conexión con CS231n
Esta práctica incorpora una herramienta para trabajar con posiciones ordenadas, 
algo útil cuando necesitamos seleccionar o comparar elementos según un criterio.

Además, reutiliza indexación y razonamiento sobre shapes, habilidades necesarias 
para trabajar autónomamente con NumPy en los assignments.

'''

import numpy as np

def main():
    envios = np.array([[201, 48, 3],[202, 15, 7],[203, 32, 2],[204, 24, 5],[205, 41, 4]])
    orden = np.argsort(envios[:,1],-1) #shape esperado: 5,
    print(orden.shape)
    #print(envios)
    print(envios.shape)

    nueva_matriz = envios[orden] #shape esperado: igual que matriz original (5,3)
    print(nueva_matriz)
    print(nueva_matriz.shape)
    print(envios)

if __name__ == "__main__":
    main()