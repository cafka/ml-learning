from autoencoder.modelo import Autoencoder
import torch
import numpy as np
import dataset as ds
from autoencoder.autoencoder import aplanar_triangulos, normalizar
import matplotlib.pyplot as plt

def main():
    mi_primer_red = Autoencoder()
    #print("Hello nn =)")
    #tensor = torch.zeros([784])
    #print(tensor.shape)
    #out = mi_primer_red.forward(tensor)
    
    print(mi_primer_red)
   
    matriz = np.zeros((28,28))
    #ds.crear_triangulo(matriz, (1,14),(20,5),(20,20))
    data_set = ds.crear_triangulos(5,28,28)
    for i in (range(data_set.shape[0])):
        plt.imshow(data_set[i],cmap='gray', vmin=0, vmax=255)
        plt.savefig(f"triangulo_{i}.png")

    tensor_aplanado = aplanar_triangulos(matriz)
    tensor_aplanado = normalizar(tensor_aplanado)
    tensor = torch.tensor(tensor_aplanado, dtype = torch.float32)
    out = mi_primer_red(tensor)
    print(out)

if __name__ == "__main__":
    main()
    
