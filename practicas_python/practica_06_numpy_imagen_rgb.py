'''
Objetivo
Entender cómo se representa una imagen a color en NumPy.
En vez de que cada píxel tenga un solo valor, ahora cada píxel tendrá tres:
[R, G, B]

donde:
- R = rojo
- G = verde
- B = azul
Consigna
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

Después:
1. Mostrá el array completo.
2. Mostrá su shape.
3. Mostrá su ndim.
4. Mostrá su dtype.
5. Obtené el píxel de la fila 1, columna 2.
6. Mostrá solamente el canal rojo de toda la imagen.
7. Visualizá la imagen con Matplotlib usando imshow().
8. Guardala como PNG.
Lo importante a observar
Espero que el shape sea algo de la forma:
(alto, ancho, canales)

Pero quiero que vos descubras los números concretos ejecutando el programa.
Para el punto 6, pensá en esta estructura:
imagen[fila, columna, canal]

y recordá que con : podés seleccionar todas las posiciones de una dimensión.
No uses OpenCV todavía. Esta práctica es solamente para que te quede completamente clara la diferencia entre:
imagen gris  -> array 2D
imagen RGB   -> array 3D
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