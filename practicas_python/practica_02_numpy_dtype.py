import numpy as np

def main ():
    matriz = np.array([[10,   20,   30,   40],
                       [50,   60,   70,   80],
                       [90,  100,  110,  120]]) 
    print(f"shape: {matriz.shape}")
    print(f"dtype: {matriz.dtype}")
    
    #columnas 1 y 2 de todas las filas
    print(matriz[:,1:3])
    res = matriz[:,1:3]/10
    print(res)
    print(f"dtype: {res.dtype}")
    print(matriz)

if __name__ == "__main__":
    main()