import numpy as np


def main():
    #Creá con NumPy una matriz de 4 filas × 5 columnas que contenga estos valores:
    #10  11  12  13  14
    #20  21  22  23  24
    #30  31  32  33  34
    #40  41  42  43  44

    #Crear el array.
    matriz = np.array([[10,  11,  12, 13,  14],
                       [20,  21,  22,  23,  24],
                       [30,  31,  32,  33,  34],
                       [40,  41,  42,  43,  44]
                        ])
    #Mostrar el array completo.
    print("array completo:")
    print(matriz)
    #Mostrar cuántas dimensiones tiene.
    print(f"dimensiones: {matriz.ndim}")
    #Mostrar su shape.
    print(f"shape: {matriz.shape}")
    #Sin usar bucles, obtener:
    #el número 23;
    #fila 1, columna 3
    print(f"numero 23: {matriz[1,3]}")
    #toda la tercera fila;
    print(f"tercera fila: {matriz[2,]}")
    #las últimas dos columnas de todas las filas.
    print(matriz[:,3:5])
    

if __name__ == "__main__":
    main()