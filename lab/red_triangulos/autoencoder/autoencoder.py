import numpy as np
import torch

def aplanar_triangulos(matriz_triangulo) -> np.ndarray:
    #triangulo_aplanado = matriz_triangulo.reshape(matriz_triangulo.shape[0] * matriz_triangulo.shape[1])
    triangulo_aplanado = matriz_triangulo.reshape(-1)
    print(np.shares_memory(matriz_triangulo, triangulo_aplanado))
    return triangulo_aplanado

def normalizar(triangulo_aplanado) -> np.ndarray:
    return triangulo_aplanado/255


def main():
    matriz = np.array([[1,2],[3,4],[5,6]])
    matriz_aplanada = aplanar_triangulos(matriz)
    triangulo_aplanado_norm = normalizar(matriz_aplanada)
    print(matriz_aplanada)
    print(triangulo_aplanado_norm)
    triangulo_tensor = torch.tensor(triangulo_aplanado_norm, dtype = torch.float32)
    print(triangulo_tensor)
    print(triangulo_tensor.dtype)

if __name__ == "__main__":
    main()  