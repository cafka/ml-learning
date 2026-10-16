'''
Práctica 19 — reducciones por eje y keepdims

keepdims significa literalmente “conservar las dimensiones”. 
Cuando una reducción normalmente elimina un eje, keepdims=True lo mantiene en esa misma posición, pero con tamaño 1. 
Esto después resulta muy útil cuando el resultado de una reducción tiene que volver a interactuar con el array original mediante broadcasting.
Usá:
import numpy as np
X = np.array([[[2, 4, 6, 8],[1, 3, 5, 7],[10, 20, 30, 40]],[[5, 10, 15, 20],[2, 4, 6, 8],[1, 1, 1, 1]]])

Tu único objetivo es sumar sobre axis=1 de dos maneras: 
primero con la reducción normal y después conservando el eje reducido con keepdims=True.
Antes de ejecutar, escribí como comentarios:
- qué representa cada eje de X;
- el shape que esperás después de la reducción normal;
- el shape que esperás manteniendo las dimensiones;
- cuál de los tres números del shape original debería convertirse en 1 cuando se conserva el eje.
Después mostrá X.shape, ambos resultados completos y sus respectivos shape.
No uses bucles, reshape, squeeze ni expand_dims. 
La única diferencia entre las dos reducciones debe ser si el eje reducido desaparece o queda conservado con tamaño 1.
Y una precisión importante para que no generalicemos a partir de un único caso: keepdims no cambia qué valores se suman; 
solo cambia la estructura dimensional del resultado.
'''
import numpy as np

def main():
    X = np.array([[[2, 4, 6, 8],[1, 3, 5, 7],[10, 20, 30, 40]],[[5, 10, 15, 20],[2, 4, 6, 8],[1, 1, 1, 1]]])
    print(X)
    print(f"X.shape = {X.shape}")
    # axis 0 → cuál de las 2 matrices
    # axis 1 → cuál de las 3 filas de cada matriz
    # axis 2 → cuál de las 4 columnas de cada fila
    # X.shape -> 2,3,4
    # 
    print("===============================")
    suma = X.sum(axis = 1)
    print(suma)
    print("===============================")
    print(f"suma.shape = {suma.shape}")
    # suma.shape = 2,4
    print("===============================")
    suma2 = X.sum(axis=1, keepdims=True)
    # suma2.shape = 2,1,4
    print(suma2)
    print("===============================")
    print(f"suma2.shape = {suma2.shape}")

if __name__ == "__main__":
    main()