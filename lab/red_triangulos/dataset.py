import numpy as np
import matplotlib.pyplot as plt
import torch

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

def triangulo_valido(v1, v2, v3) -> bool:
    '''
    calcula el determinante para verificar que los puntos no estén alineados
    '''
    matriz_det = np.zeros((2, 2))
    matriz_det[0][0] = v2[0]-v1[0]
    matriz_det[0][1] = v2[1]-v1[1]
    matriz_det[1][0] = v3[0]-v1[0]
    matriz_det[1][1] = v3[1]-v1[1]

    det = np.linalg.det(matriz_det)
    return (det != 0)

def longitud (u,v):
    long_x = u[0] - v[0]
    long_y = u[1] - v[1]
    suma = long_x**2 + long_y**2
    return np.sqrt(suma)

def altura_valida (v1,v2,v3):
    '''Para cada lado entre dos vértices, por ejemplo A y B, tomás el tercero C. 
    Calculás el determinante con A como origen, o sea, det igual (Bx - Ax) por (Cy - Ay) menos (By - Ay) por (Cx - Ax). 
    La longitud del lado AB es la raíz cuadrada de (Bx - Ax) al cuadrado más (By - Ay) al cuadrado.
    '''
    det = np.abs((v2[0]-v1[0])*(v3[1]-v1[1]) - ((v2[1]-v1[1])*(v3[0]-v1[0]))) #doble del area del triangulo
    
    longitud_v1_v2 = longitud (v1,v2)
    altura1 = det/longitud_v1_v2
    if altura1 < 2:
        return False
    else:
        longitud_v1_v3 = longitud (v1,v3)
        altura2 = det/longitud_v1_v3
        if altura2 < 2:
            return False
        else:
            longitud_v2_v3 = longitud (v2,v3)
            altura3 = det/longitud_v2_v3
            if altura3 < 2:
                return False
            else:
                return True

def crear_triangulo(matriz: np.array, v1, v2, v3):
    print(f"v1 : {v1} - v2 : {v2} - v3 : {v3}")
    #v1-v2
    crear_lado(matriz,v1,v2)
    #v2-v3
    crear_lado(matriz,v2,v3)
    #v1-v3
    crear_lado(matriz,v1,v3)

def crear_triangulos(cant_triangulos, x, y) -> np.ndarray:
    triangulos = np.zeros((cant_triangulos,x,y))
    i = 0
    while i < cant_triangulos:
        v1 = (np.random.randint(0,x), np.random.randint(0,y))
        v2 = (np.random.randint(0,x), np.random.randint(0,y))
        v3 = (np.random.randint(0,x), np.random.randint(0,y))
        if triangulo_valido(v1, v2, v3) and altura_valida(v1, v2, v3):
            crear_triangulo(triangulos[i], v1,v2,v3)
            i += 1
        
    return triangulos

def aplanar_triangulo(triangulo) -> np.ndarray:
    #triangulo_aplanado = matriz_triangulo.reshape(matriz_triangulo.shape[0] * matriz_triangulo.shape[1])
    triangulo_aplanado = triangulo.reshape(-1)
    #print(np.shares_memory(matriz_triangulo, triangulo_aplanado))
    return triangulo_aplanado

def normalizar(triangulo_aplanado) -> np.ndarray:
    return triangulo_aplanado/255

def crear_dataset(tamano_dataset=100, x = 28, y = 28):
    triangulos = crear_triangulos(tamano_dataset, x, y)
    return triangulos

def dataset_normalizado(triangulos_sin_normalizar):
    
    triangulos_norm_apl = torch.zeros(
        (triangulos_sin_normalizar.shape[0], 784),
        dtype=torch.float32
    )
    for i in range(len(triangulos_sin_normalizar)):
        triangulo_aplanado_norm = normalizar(aplanar_triangulo(triangulos_sin_normalizar[i].copy()))
        triangulo_tensor = torch.tensor(triangulo_aplanado_norm, dtype = torch.float32)
        triangulos_norm_apl[i] = triangulo_tensor
    return triangulos_norm_apl
    

def main():
    #triangulo = crear_matriz(28,28,1,14,10,7,10,21) 
    #triangulo = crear_matriz(256,256) 
    #v1 = (1,3)
    #v2 = (120,7)
    #v3 = (205,201)
    #crear_triangulo(triangulo, v1,v2,v3)
    #plt.imshow(triangulo,cmap='gray', vmin=0, vmax=255)
    #plt.savefig("triangulo2.png")
    np.random.seed(42)
    dataset = crear_dataset(5,28,28)
    datos_normalizados = dataset_normalizado(dataset)
    print(dataset)
    print(f"dataset.shape = {dataset.shape}")
    #print(datos_normalizados)
    print(torch.unique(datos_normalizados))
    print(f"dataset_normalizado.shape = {datos_normalizados.shape}")
    print(datos_normalizados[0])
    print("========================")
    print(datos_normalizados[1])
    #for i in (range(data_set.shape[0])):
    #    plt.imshow(data_set[i],cmap='gray', vmin=0, vmax=255)
    #    plt.savefig(f"triangulo_{i}.png")


if __name__ == "__main__":
    main()