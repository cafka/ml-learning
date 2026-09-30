'''
Usá esta imagen RGB artificial:
[    [[10, 20, 30], [40, 50, 60], [70, 80, 90]],    
     [[20, 30, 40], [50, 60, 70], [80, 90, 100]]]

Tu ejercicio es: 
1) convertir esos datos en un array NumPy; 
2) mostrar shape, ndim y dtype; 
3) calcular, sin for, el promedio del canal rojo de toda la imagen; 
4) calcular, también sin for, un único array con los tres promedios —rojo, verde y azul—; 
5) mostrar el shape del resultado; 
6) antes de ejecutar el punto 4, escribir como comentario qué shape esperás obtener y por qué.
No uses bucles, no calcules cada promedio a mano y no modifiques la imagen original. 
La habilidad nueva de hoy es reducir dimensiones por ejes, algo que después aparece de forma natural 
en preprocesamiento de imágenes y operaciones vectorizadas de CS231n. No te doy la línea necesaria: 
primero quiero que razones qué dimensiones deben desaparecer y cuál debe conservarse.
'''
import numpy as np

def main():
    imagen_artificial = np.array([[[10, 20, 30], [40, 50, 60], [70, 80, 90]],    
                                [[20, 30, 40], [50, 60, 70], [80, 90, 100]]])
    print(f"shape: {imagen_artificial.shape} - ndim: {imagen_artificial.ndim} - dtype: {imagen_artificial.dtype}")
    suma_canal_rojo = imagen_artificial[:,:,0].sum()
    cantidad_rojo = imagen_artificial[:,:,0].size
    print(f"promedio rojo: {suma_canal_rojo/cantidad_rojo}")
    #arreglo_promedio = np.array([suma_canal_rojo/cantidad_rojo,imagen_artificial[:,:,1].sum()/imagen_artificial[:,:,1].size,imagen_artificial[:,:,2].sum()/imagen_artificial[:,:,2].size])
    #print(f"promedio rojo - verde - azul: {arreglo_promedio}")
    #print(f"shape: {arreglo_promedio.shape}")

    promedio = np.mean(imagen_artificial,axis=(0,1))
    print(f"promedio usando mean: {promedio}")

if __name__ == "__main__":
    main()