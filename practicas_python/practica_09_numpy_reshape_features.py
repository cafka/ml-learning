'''
Usá este pequeño lote de dos imágenes en escala de grises:
[    [[10, 20],     [30, 40]],    [[50, 60],     [70, 80]]]


Tu ejercicio es crear el array con NumPy, mostrar shape, ndim y dtype, e interpretar qué representa cada dimensión. 
Después, usando reshape(), creá un nuevo array en el que cada imagen quede convertida en una sola fila de características. 
Mostrá el nuevo array y su shape, comprobá que la cantidad total de elementos no cambió y, finalmente, 
reconstruí desde ese array la forma original y comprobá nuevamente el shape.
No uses for, no copies manualmente los valores, no modifiques el array original y, en esta práctica, no uses flatten() ni ravel().
Antes de escribir el reshape, dejá como comentario qué shape esperás obtener y por qué. La única pista, 
si te trabás, es pensar qué dimensión identifica cuántas imágenes hay y cuáles querés juntar dentro de cada imagen.
'''
import numpy as np

def main():
    imagen_gris_x2 = np.array([[[10, 20],
                                [30, 40]],
                               [[50, 60],
                                [70, 80]]])
    print(f"shape: {imagen_gris_x2.shape} - ndim: {imagen_gris_x2.ndim} - dtype: {imagen_gris_x2.dtype}")
    #shape: (2, 2, 2) 
    #(cantidad de imágenes, alto, ancho)
    #2 imágenes
    #cada una de 2 filas
    #cada fila de 2 columnas
    #axis 0 → cuál imagen
    #axis 1 → qué fila dentro de esa imagen
    #axis 2 → qué columna dentro de esa fila
    #La diferencia es importante: no pensarlo solo como “un objeto 3D”, sino como una colección de imágenes.
    #imagen_gris_x2[0] selecciona la primera imagen completa, por lo que desaparece el eje 0 y queda un array de shape:(2, 2)
    imagenes_aplanadas = np.reshape(imagen_gris_x2,(2,4))
    print(f"aplano imagen:\n {imagenes_aplanadas}\n shape: {imagenes_aplanadas.shape}")
    print("(2, 4) Eso significa: 2 imágenes, cada una representada por 4 características.")
    imagenes_reconstruidas = np.reshape(imagenes_aplanadas, (2,2,2))
    print(f"imagen reconstruida:\n {imagenes_reconstruidas}\n shape: {imagenes_reconstruidas.shape}")
    #reshape() no cambia la cantidad de elementos ni sus valores; cambia cómo NumPy interpreta su organización en dimensiones.

if __name__ == "__main__":
    main()


#pregunta extra
#Si tuvieras un lote de 100 imágenes RGB de tamaño 32×32, con shape: (100, 32, 32, 3)
#y quisieras representar cada imagen como una sola fila de características, 
#¿qué shape esperarías obtener después del reshape? 
#respuesta: (100,3072)
#Porque cada imagen tiene: 32 × 32 × 3 = 3072 características, 
#y conservás las 100 imágenes como filas independientes.
#(100, 32, 32, 3)
#   ↓ reshape
#(100, 3072)

