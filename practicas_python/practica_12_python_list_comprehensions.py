'''
Práctica 12 — list comprehensions en Python
Esta vez trabajamos deliberadamente con Python puro, no con NumPy. 
La habilidad nueva es crear una lista transformando los elementos de otra lista mediante una list comprehension, 
que es una forma idiomática de Python que aparece seguido en código de CS231n.
Usá estos datos de entrada:
lados = [16, 24, 32, 48, 64]

Cada número representa el lado, en píxeles, de una imagen cuadrada.
Tu único objetivo es crear una lista llamada cantidad_pixeles que contenga, para cada valor de lados, 
la cantidad total de píxeles de esa imagen cuadrada.
Mostrá la lista original, la nueva lista y la cantidad de elementos de ambas.
La restricción es que para construir cantidad_pixeles no uses NumPy ni un for tradicional: usá una list comprehension.
Antes de ejecutar, escribí un comentario explicando qué relación esperás que exista entre 
la posición i de lados y la posición i de cantidad_pixeles.
Como comprobación, verificá que ambas listas tengan la misma cantidad de elementos y 
que cada elemento de cantidad_pixeles corresponda al elemento de lados que ocupa la misma posición.
No te doy la sintaxis ni la solución; escribís vos el código y después revisamos tu intento.
'''
def main():
    lados = [16, 24, 32, 48, 64]
    print(f"lados = {lados} - cantidad elementos = {len(lados)}")
    #lados[i] -> lado x lado
    cantidad_pixeles = [x*x for x in lados]
    print(f"cantidad_pixeles = {cantidad_pixeles} - cantidad elementos = {len(cantidad_pixeles)}")


if __name__ == "__main__":
    main()