'''
Usá:
X = np.array([    [1, 2, 3],    [4, 2, 0],    [2, 1, 5],    [3, 3, 3]])
consulta = np.array([2, 2, 3])


Tu tarea es calcular, sin for, la distancia cuadrática entre consulta y cada fila de X. No calcules todavía la raíz cuadrada: 
el objetivo es obtener un vector con una distancia por cada ejemplo.
Antes de escribir el código de la operación principal, dejá como comentario qué shape esperás obtener después de X - consulta. 
Mostrá los shape intermedios y después usá una reducción para convertir las diferencias por característica en un único valor por fila.
Pista inicial, solamente conceptual: pensá qué hace broadcasting entre un array de shape (4, 3) y uno de shape (3,), 
y luego preguntate qué eje tiene que desaparecer para que te queden cuatro valores.
Esto prepara una habilidad importante para el Assignment 1 de CS231n: operar vectorizadamente sobre muchos ejemplos a la vez, 
sin resolverte ninguna parte del assignment.
'''
import numpy as np

def main():
    X = np.array([ [1, 2, 3],
                   [4, 2, 0],    
                   [2, 1, 5],    
                   [3, 3, 3] ])
    consulta = np.array([2, 2, 3])
    resta = X - consulta
    #shape esperado: (4,3)
    print(f"shape resta: {resta.shape}")
    print(f"resta:\n{resta}")
    cuad = resta**2
    print(f"cuad:\n{cuad}")
    suma = np.sum(cuad,axis=(1))
    print(f"suma:\n{suma}")
    dist = np.sqrt(suma)
    print(f"distancias: {dist}")


if __name__ == "__main__":
    main()
