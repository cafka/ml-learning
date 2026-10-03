'''
Práctica 11 — seleccionar el vecino más cercano

Para esta práctica, por distancia cuadrática entendemos:

sum_j (x_j-q_j)^2

No hace falta aplicar raíz cuadrada.
Datos de entrada
import numpy as np
X = np.array([    [1, 2, 3],    [4, 2, 0],    [2, 1, 5],    [3, 3, 3]])
consulta = np.array([2, 2, 3])

Objetivo único
Reutilizá el procedimiento vectorizado de la práctica 10 para obtener la distancia cuadrática entre consulta y cada fila de X.
A partir de ese vector de distancias, tu programa debe:
1. determinar el índice del ejemplo con menor distancia cuadrática;
2. usar ese índice para recuperar la fila correspondiente de X;
3. usar el mismo índice para recuperar la distancia cuadrática de ese ejemplo.
Mostrá al final:
- el vector completo de distancias cuadráticas;
- el índice seleccionado;
- la fila seleccionada de X;
- la distancia cuadrática asociada a esa fila.

Y explicá también, en una línea de comentario, por qué el índice obtenido puede usarse tanto sobre X como sobre el vector de distancias.
Restricciones
Trabajá de forma vectorizada para el cálculo de las distancias, sin for. 
No uses sqrt: en esta práctica comparamos directamente distancias cuadráticas.
Comprobación
Sin calcular el resultado a mano, verificá conceptualmente que:
- haya una sola distancia por cada fila de X;
- el índice seleccionado sea válido para X;
- la fila recuperada y la distancia recuperada correspondan al mismo ejemplo.
Esta habilidad aparece naturalmente antes de trabajar con clasificadores tipo k-NN en CS231n: 
primero calculás distancias, después necesitás identificar qué ejemplos corresponden a las menores. 
Acá practicamos solamente esa selección, sin resolver ninguna parte del assignment.
'''
import numpy as np

def main():
    X = np.array([[1, 2, 3],    
                  [4, 2, 0],    
                  [2, 1, 5],    
                  [3, 3, 3]])
    
    consulta = np.array([2, 2, 3]) 
    aux = (X-consulta)**2 #(4,3)
    print(f"aux:\n {aux} \nshape: {aux.shape}")
    distancia = np.sum(aux,axis=1) # sumo por fila (4,)
    print(f"distancia:\n {distancia} \nshape: {distancia.shape}")
    #1. determinar el índice del ejemplo con menor distancia cuadrática;
    indice_menor_distancia = np.argmin(distancia)
    print(f"indice con menor distancia: {indice_menor_distancia}")
    #2. usar ese índice para recuperar la fila correspondiente de X;
    print(f"fila con menor distancia: {X[indice_menor_distancia]}")
    #3. usar el mismo índice para recuperar la distancia cuadrática de ese ejemplo.
    print(f"distancia para indice {indice_menor_distancia} => {distancia[indice_menor_distancia]}")
    #Explicá también, en una línea de comentario, por qué el índice obtenido puede usarse tanto sobre X como sobre el vector de distancias.
    # El indice fue obtenido del vector de distancias donde cada elemento
    # del array corresponde a la distancia de consulta a una fila de la matriz X.

if __name__ == "__main__":
    main()