'''
Práctica 08B — reducción por ejes + broadcasting

Usá esta imagen:
[    [[10, 20, 30], [40, 50, 60]],    [[20, 30, 40], [50, 60, 70]]]


Tu único ejercicio es obtener, sin for y sin tratar R, G y B por separado, 
un vector con el promedio de cada canal y después crear una nueva imagen 
restándole ese vector a todos los píxeles mediante broadcasting. 
Mostrá el shape del vector y el shape de la nueva imagen, y comprobá que la imagen original no cambió.
No uses tile ni repitas manualmente el vector. 
Antes de escribir la resta, pensá por qué un array de shape (3,) puede operar con uno de shape (2, 2, 3).
'''
import numpy as np

def main():
    imagen = np.array([    [[10, 20, 30], [40, 50, 60]],    [[20, 30, 40], [50, 60, 70]]])
    print(f"imagen:\n {imagen}")
    vector_promedio = np.mean(imagen,axis=(0,1))
    print(f"promedio: {vector_promedio}")
    nueva_imagen = imagen - vector_promedio
    print(f"nueva imagen:\n {nueva_imagen}")
    print(f"shape imagen = {imagen.shape}")
    print(f"shape vector promedio = {vector_promedio.shape}")
    print(f"shape nueva imagen = {nueva_imagen.shape}")
    print(f"imagen:\n {imagen}")

if __name__ == "__main__":
    main()

'''
Pregunta corta de cierre, sin ejecutar nada: ¿por qué tiene sentido que después de centrar los canales aparezcan números negativos en nueva_imagen?

Centrar los datos significa restarles su media. En tu caso, lo hiciste por canal:
pixel RGB - promedio RGB

Así, cada canal queda alrededor de 0.
Por eso aparecen valores negativos: si un valor de un canal estaba por debajo de su promedio, 
al restarle la media queda negativo. Si estaba por encima, queda positivo.
Ejemplo conceptual:
valor - media

menor que la media  → negativo
igual a la media    → 0
mayor que la media  → positivo

Eso es justamente el sentido de centrar.
'''

