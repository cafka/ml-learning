'''
Práctica 07 — Manipulación de canales RGB con NumPy

Hoy seguimos exactamente desde donde quedaste: ya sabés representar una imagen como un array de shape (alto, ancho, 3) y extraer un canal. 
Ahora vas a modificar un canal completo usando slicing.
Creá una imagen artificial de 2 filas × 4 columnas con estos píxeles:
fila 0:
rojo      verde      azul       blanco

fila 1:
amarillo  cian       magenta    negro

Usá:
rojo      = [255,   0,   0]
verde     = [  0, 255,   0]
azul      = [  0,   0, 255]
blanco    = [255, 255, 255]

amarillo  = [255, 255,   0]
cian      = [  0, 255, 255]
magenta   = [255,   0, 255]
negro     = [  0,   0,   0]

Tu consigna es:
1. Crear la imagen con NumPy y mostrar shape, ndim y dtype.
2. Crear una copia independiente de la imagen original. Para esto sí te doy la herramienta que necesitás: .copy().
3. En la copia, poner en 0 el canal rojo de todos los píxeles, usando slicing. No recorras la imagen con for.
4. Imprimir el canal rojo de la imagen original y el de la modificada, para comprobar qué ocurrió.
5. Mostrar con imshow() primero la imagen original y después la imagen modificada.
6. Guardar la modificada como imagen_sin_rojo.png.
Antes de ejecutar el programa, pensá qué color esperás que tengan en la imagen modificada estos tres píxeles: rojo, blanco y amarillo. 
No hace falta que me contestes ahora; quiero que compares tu predicción con lo que veas.
Pista mínima
Ya usaste:
imagen[:, :, 0]

para leer todo el canal rojo. Esta vez necesitás usar esa misma idea para asignarle un valor.
No te doy la línea: esa parte te toca a vos. 😄
Esta habilidad después sirve para entender operaciones sobre imágenes completas sin modificar píxel por píxel, 
que es justamente una de las ventajas importantes de NumPy.
'''
