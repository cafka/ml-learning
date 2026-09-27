'''
Práctica 05 — Visualizar un array NumPy como imagen

Objetivo

Comprobar visualmente que una matriz de números puede
interpretarse como una imagen en escala de grises.

Usá esta matriz:

0    50   100   150   200
25   75   125   175   225
50  100   150   200   250
75  125   175   225   255
100 150   200   250   255

Consigna

1. Crear la matriz con NumPy.
2. Mostrar su shape y su dtype.
3. Visualizarla con Matplotlib usando imshow().
4. Indicar que debe mostrarse en escala de grises.
5. Usar valores entre 0 y 255 para la escala.
6. Observar qué ocurre con los valores bajos y altos.
7. Cambiar un solo elemento de la matriz a 255.
8. Volver a visualizar la imagen.
9. Observar dónde aparece el cambio.
10. Guardar la imagen en formato PNG.

Idea clave

En una imagen en escala de grises, cada posición
[fila, columna] contiene un único valor de intensidad.

Con una escala de 0 a 255:

0   representa negro.
255 representa blanco.

Los valores intermedios producen distintos tonos de gris.

Matplotlib permite visualizar el array con imshow()
y guardar la figura con savefig().
'''

import numpy as np
import matplotlib.pyplot as plt

def main():
    matriz = np.array([[0, 50, 100, 150, 200],
                       [25, 75, 125, 175, 225],
                       [50, 100, 150, 200, 250],
                       [75, 125, 175, 225, 255],
                       [255, 150, 200, 250, 255]])
    print(f"shape de matriz: {matriz.shape}")
    print(f"dtype de matriz: {matriz.dtype}")
    print(f"ndim de matriz: {matriz.ndim}")
    #Returns: AxesImage
    imagen = plt.imshow(matriz,cmap='gray', vmin=0, vmax=255)
    plt.show()
    #Y una sugerencia mínima: para estas imágenes artificiales usaría .png en vez de .jpg, porque PNG no introduce compresión con pérdida.
    plt.savefig("imagen_gris2.png")
    # 5. Observá qué ocurre con los valores bajos y los altos.
    # El 0 es negro y el 255 blanco. 
    # 6. Cambiá un solo elemento de la matriz a 255 y volvé a visualizarla.
    # Cambié la posición [4,0] por 255 y observo en el extremo inferior izquierdo que cambió a blanco

if __name__ == "__main__":
    main()
