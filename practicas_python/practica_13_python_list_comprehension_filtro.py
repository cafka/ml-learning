'''
Práctica 13 — filtrado con list comprehension

La habilidad nueva es extender la list comprehension que ya usaste agregándole una condición de filtrado. 
Esto aparece mucho en Python puro: no solo transformar elementos, sino también decidir cuáles conservar.
Usá estos datos:
tamanios = [16, 24, 32, 48, 64, 96]

Cada valor representa el lado de una imagen cuadrada.
Tu objetivo es crear una nueva lista llamada tamanios_seleccionados 
que contenga solamente los tamaños cuyo lado sea mayor o igual que 32.
Mostrá:
- la lista original;
- la lista filtrada;
- la cantidad de elementos de cada una.
Restricciones
- no uses NumPy;
- no uses un for tradicional;
- usá una list comprehension con condición.
Antes de ejecutar
Escribí un comentario explicando qué debería pasar con cada elemento de tamanios: 
bajo qué condición entra en la nueva lista y bajo qué condición queda afuera.
'''

def main():
    tamanios = [16, 24, 32, 48, 64, 96]
    print(f"tamanios: {tamanios}\n cantidad elementos: {len(tamanios)}")
    tamanios_seleccionados = [x for x in tamanios if x >= 32]
    print(f"tamanios_seleccionados: {tamanios_seleccionados}\n cantidad elementos: {len(tamanios_seleccionados)}")

if __name__ == "__main__":
    main()