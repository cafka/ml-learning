'''
Práctica 06 — Imagen RGB como array NumPy 3D

Objetivo

Entender cómo se representa una imagen a color
dentro de un array NumPy.

En una imagen RGB cada píxel contiene tres valores:

[R, G, B]

R = rojo
G = verde
B = azul

Creá una imagen artificial de 2 filas × 3 columnas.

Fila 0:

rojo       verde       azul

Fila 1:

blanco     negro       amarillo

Usá estos valores:

rojo      = [255,   0,   0]
verde     = [  0, 255,   0]
azul      = [  0,   0, 255]

blanco    = [255, 255, 255]
negro     = [  0,   0,   0]
amarillo  = [255, 255,   0]

Consigna

1. Crear la imagen como un array NumPy.
2. Mostrar el array completo.
3. Mostrar su shape.
4. Mostrar su ndim.
5. Mostrar su dtype.
6. Obtener el píxel de la fila 1, columna 2.
7. Mostrar solamente el canal rojo de toda la imagen.
8. Visualizar la imagen RGB con Matplotlib.
9. Guardarla como imagen_rgb.png.

Idea clave

Una imagen en escala de grises puede representarse
con un array 2D:

fila × columna

Una imagen RGB necesita una tercera dimensión:

fila × columna × canal

Por eso una imagen RGB puede tener un shape como:

(alto, ancho, 3)

El tercer eje contiene los canales rojo, verde y azul.
'''

import numpy as np
import matplotlib.pyplot as plt

def crear_imagen() -> np.ndarray:
    '''
    Creá con NumPy una imagen artificial de 2 filas × 3 columnas con estos píxeles:
    fila 0:
    rojo       verde       azul

    fila 1:
    blanco     negro       amarillo

    Usá estos valores:
    rojo      = [255,   0,   0]
    verde     = [  0, 255,   0]
    azul      = [  0,   0, 255]

    blanco    = [255, 255, 255]
    negro     = [  0,   0,   0]
    amarillo  = [255, 255,   0]
    '''
    return np.array([[(255,0,0),(0,255,0),(0,0,255)],
             [(255,255,255),(0,0,0),(255,255,0)]
    ])

def main():
    '''
    Mostrá su shape, ndim y dtype.
    '''
    matriz_imagen_rgb = crear_imagen()
    print(f"matriz imagen: \n{matriz_imagen_rgb}")
    print(f"shape: {matriz_imagen_rgb.shape}")
    print(f"ndim: {matriz_imagen_rgb.ndim}")
    print(f"dtype: {matriz_imagen_rgb.dtype}")
    #Obtené el píxel de la fila 1, columna 2. Asumo son las filas reales y no las de numpy
    pixel_1_2 = matriz_imagen_rgb[0,1]
    print(f"pixel de fila 1, columna 2: {pixel_1_2}")
    #Mostrá solamente el canal rojo de toda la imagen.
    print(f"canal rojo de la imagen:\n {matriz_imagen_rgb[:,:,0]}")
    #Visualizá la imagen con Matplotlib usando imshow().
    plt.imshow(matriz_imagen_rgb)
    plt.savefig("imagen_rgb.png")

if __name__ == "__main__":
    main()g