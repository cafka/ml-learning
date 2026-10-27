from autoencoder.modelo import Autoencoder
import torch
import numpy as np
import dataset as ds
from autoencoder.autoencoder import aplanar_triangulos, normalizar

def main():
    mi_primer_red = Autoencoder()
    #print("Hello nn =)")
    #tensor = torch.zeros([784])
    #print(tensor.shape)
    #out = mi_primer_red.forward(tensor)
    
    print(mi_primer_red)
   
    matriz = np.zeros((28,28))
    ds.crear_triangulo(matriz, (1,14),(20,5),(20,20))
    tensor_aplanado = aplanar_triangulos(matriz)
    tensor_aplanado = normalizar(tensor_aplanado)
    tensor = torch.tensor(tensor_aplanado, dtype = torch.float32)
    out = mi_primer_red(tensor)
    print(out)

if __name__ == "__main__":
    main()
    
