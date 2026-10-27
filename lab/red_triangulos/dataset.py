import numpy as np
import matplotlib.pyplot as plt

def crear_matriz (eje1: int, eje2: int) -> np.ndarray:
    matriz = np.zeros((eje1,eje2))
    return matriz

def pendiente_recta_mas_coef (x1,y1,x2,y2) -> tuple[float, float]:
    pendiente = (y2-y1)/(x2-x1)
    coef = y1 - pendiente*x1
    return pendiente, coef

def f_x (x,m,b) -> float:
    return m*x + b

def g_y (y,m,b) -> float:
    return (y - b)/m

def crear_lado(matriz, vertice_1, vertice_2):
    if vertice_1[0] == vertice_2[0]: #linea horizontal
        columna_inicio = min(vertice_1[1],vertice_2[1])
        columna_fin = max(vertice_1[1],vertice_2[1])
        matriz[vertice_1[0],columna_inicio:columna_fin+1] = 255        
    else:
        if vertice_1[1] == vertice_2[1]: #linea vertical
            fila_inicio = min(vertice_1[0],vertice_2[0])
            fila_fin = max(vertice_1[0],vertice_2[0])
            matriz[fila_inicio:fila_fin+1,vertice_1[1]] = 255
        else: #los vertices no comparten ni fila ni columna
            if abs(vertice_2[0]-vertice_1[0]) > abs(vertice_2[1]-vertice_1[1]):
                inicio = min(vertice_1[0] ,vertice_2[0])
                fin = max(vertice_1[0] ,vertice_2[0]) 
                avanzo_filas = True
            else:
                inicio = min(vertice_1[1] ,vertice_2[1])
                fin = max(vertice_1[1] ,vertice_2[1])
                avanzo_filas = False
            m,b = pendiente_recta_mas_coef(vertice_1[0],vertice_1[1],vertice_2[0],vertice_2[1]) 
            while  inicio <= fin:
                if avanzo_filas:
                    columna_pixel = int(np.round(f_x(inicio, m, b)))
                    matriz[inicio,columna_pixel] = 255
                else:
                    fila_pixel = int(np.round(g_y(inicio, m, b)))
                    matriz[fila_pixel,inicio] = 255
                inicio += 1

def crear_triangulo(matriz: np.array, v1, v2, v3):
    #v1-v2
    crear_lado(matriz,v1,v2)
    #v2-v3
    crear_lado(matriz,v2,v3)
    #v1-v3
    crear_lado(matriz,v1,v3)

def crear_triangulos(cant_triangulos, x, y) -> np.ndarray:
    np.random.seed(42)
    triangulos = np.zeros((cant_triangulos,x,y))
    for i in range(cant_triangulos):
        v1 = (np.random.randint(0,x), np.random.randint(0,y))
        v2 = (np.random.randint(0,x), np.random.randint(0,y))
        v3 = (np.random.randint(0,x), np.random.randint(0,y))
        crear_triangulo(triangulos[i], v1,v2,v3)
        
    return triangulos

def main():
    #triangulo = crear_matriz(28,28,1,14,10,7,10,21) 
    #triangulo = crear_matriz(256,256) 
    #v1 = (1,3)
    #v2 = (120,7)
    #v3 = (205,201)
    #crear_triangulo(triangulo, v1,v2,v3)
    #plt.imshow(triangulo,cmap='gray', vmin=0, vmax=255)
    #plt.savefig("triangulo2.png")

    data_set = crear_triangulos(5,28,28)
    #for i in (range(data_set.shape[0])):
    #    plt.imshow(data_set[i],cmap='gray', vmin=0, vmax=255)
    #    plt.savefig(f"triangulo_{i}.png")


if __name__ == "__main__":
    main()