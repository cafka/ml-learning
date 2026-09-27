'''
Objetivo
Comprobar visualmente que una matriz de números puede interpretarse como una imagen en escala de grises.
Usá esta matriz:
0    50   100   150   200
25   75   125   175   225
50   100  150   200   250
75   125  175   225   255
100  150  200   250   255

Consigna
1. Creá la matriz con NumPy.
2. Mostrá su shape y su dtype.
3. Usá Matplotlib para mostrarla como una imagen.
4. Indicá que querés verla en escala de grises.
5. Observá qué ocurre con los valores bajos y los altos.
6. Cambiá un solo elemento de la matriz a 255 y volvé a visualizarla.
7. Contame qué cambio viste en la imagen y dónde apareció.
Pautas mínimas
Vas a necesitar importar:
- numpy
- matplotlib.pyplot
En Matplotlib, investigá/usá imshow() para mostrar la matriz y show() para abrir la visualización.
Para escala de grises, imshow() tiene un parámetro llamado cmap.
No hace falta usar OpenCV todavía y no uses una imagen real. Hoy queremos mantener control total sobre los números para entender qué estamos viendo.
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
