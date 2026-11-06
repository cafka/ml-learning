import numpy as np
import torch




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