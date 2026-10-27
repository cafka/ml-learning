'''
Práctica 25 — Identidad de objetos, referencias y funciones
Una herramienta nueva: is frente a ==
Hasta ahora venimos razonando sobre qué variables comparten objetos. 
Python tiene dos operadores para comprobar dos cosas distintas.
- == pregunta si dos objetos tienen el mismo contenido o valor.
- is pregunta si son exactamente el mismo objeto.
Por ejemplo:
A = [5, 10, 15]
B = A.copy()
C = A
print(A == B)  # True
print(A is B)  # False
print(A is C)  # True

Aunque A y B tienen los mismos valores, son listas diferentes. 
En cambio, C es otra referencia al mismo objeto que A.

Ahora observá un caso más interesante:
A = [[2, 4], [6, 8]]
B = A.copy()
print(A is B) # False
print(A[0] is B[0])  # True

¿Por qué? Porque copiamos el contenedor externo, pero no sus listas internas.

Un contraejemplo importante: dos números pueden ser iguales sin que debamos asumir que son el mismo objeto. 
Para comparar valores numéricos utilizamos ==, no is.

Esta distinción se aplica a objetos de Python en general. 
En arrays NumPy, == tiene un comportamiento especial: compara elementos individualmente, 
no devuelve necesariamente un único booleano.
Tu objetivo de código
Tenemos un registro de dos equipos:
registros = [["equipo_A", 10],["equipo_B", 20]]

Quiero que escribas una función llamada crear_revision que reciba esa lista anidada y realice estas operaciones, en este orden:
1. Agregue el texto "revisado" a la primera lista interna del argumento recibido.
2. Cree una copia superficial de la lista externa y haga que la variable local utilizada para trabajar con los registros apunte a esa copia.
3. Agregue a esa nueva lista externa un tercer registro: ["equipo_C", 30].
4. Devuelva esa nueva lista externa.
Esta práctica simula deliberadamente una modificación compartida y una reasignación para estudiar sus efectos. 
No significa que debamos programar siempre así.
Restricciones y comprobaciones
- No utilizar NumPy ni bibliotecas de copia profunda.
- No modificar directamente registros desde fuera de la función.
- Utilizar una función y main().
- Guardar el resultado de la función en una variable distinta de registros.
- Imprimir ambas listas después de llamar a la función.
- Comprobar con is si ambas listas externas son el mismo objeto y si comparten su primera lista interna.
Antes de ejecutar, escribí como comentarios qué contenido esperás que tengan registros y el resultado devuelto, 
y qué booleanos esperás obtener con las dos comparaciones de identidad.

No te doy el código de resolución: quiero observar cómo combinás lo que ya sabés sobre funciones, listas anidadas, 
copias superficiales y referencias con el operador nuevo is.
'''

def crear_revision(lista_anidada):
    '''
    1. Agregue el texto "revisado" a la primera lista interna del argumento recibido.
    2. Cree una copia superficial de la lista externa y haga que la variable local utilizada para trabajar con los registros apunte a esa copia.
    3. Agregue a esa nueva lista externa un tercer registro: ["equipo_C", 30].
    4. Devuelva esa nueva lista externa.
    '''
    lista_anidada[0].append("revisado")
    copia_superficial = lista_anidada.copy()
    lista_anidada = copia_superficial
    lista_anidada.append(["equipo_C", 30])
    return lista_anidada

def main():
    registros = [["equipo_A", 10],["equipo_B", 20]]
    lista = crear_revision(registros)
    print(registros)
    print(lista)
    #Comprobar con is si ambas listas externas son el mismo objeto y si comparten su primera lista interna.
    print(registros is lista)
    print(registros[0] is lista[0])

if __name__ == "__main__":
    main()

