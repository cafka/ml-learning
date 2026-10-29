# =====================================================
# PRACTICA 27 - MANEJO DE EXCEPCIONES EN PYTHON
# =====================================================
#
# CONCEPTO NUEVO: try y except
#
# Cuando un programa encuentra una operación
# que no puede realizar, Python puede lanzar
# una excepción.
#
# Por ejemplo:
#
# numero = int("hola")
#
# Esto produce un ValueError porque el texto
# no puede convertirse en un número entero.
#
#
# MANEJO DE ERRORES CON try Y except
#
# Podemos manejar ese error de esta forma:
#
# texto = "12.5"
#
# try:
#     numero = int(texto)
#     print(numero)
# except ValueError:
#     print("No es un entero válido")
#
# Python intenta ejecutar el bloque try.
#
# Si se produce un ValueError, ejecuta el
# bloque except correspondiente.
#
#
# OTRAS CLAUSULAS
#
# else:
# Se ejecuta si el bloque try termina
# sin producir ninguna excepción.
#
# finally:
# Se ejecuta al salir de la estructura,
# haya ocurrido una excepción o no.
# Suele utilizarse para liberar recursos.
#
#
# LIMITES Y CONTRAEJEMPLOS
#
# except ValueError no captura cualquier error.
#
# Por ejemplo, acceder a un índice inexistente
# de una lista produce un IndexError.
#
# Ese error no sería capturado por un bloque
# except ValueError.
#
# Es preferible capturar los errores específicos
# que sabemos manejar.
#
# Evitamos ocultar indiscriminadamente los
# errores que puedan aparecer en un programa.
#
#
# =====================================================
# CONTEXTO
# =====================================================
#
# Una aplicación recibe registros de mediciones.
#
# Cada registro contiene:
# - El nombre de una medición.
# - Su valor numérico representado como texto.
#
# Algunos valores pueden ser inválidos.
#
# DATOS INICIALES

registros = [
    ["temperatura", "21"],
    ["humedad", "desconocido"],
    ["presion", "1013"],
    ["viento", "18a"],
    ["luz", "350"]
]


# =====================================================
# OBJETIVO
# =====================================================
#
# Crear una función llamada procesar_registros.
#
# La función debe recibir una lista de registros.
#
# Cada registro contiene un nombre y un valor
# numérico representado como texto.
#
# Convertir cada valor a un número entero.
#
# Si un valor no puede convertirse,
# sustituir ese valor por None.
#
# Devolver una nueva lista anidada.
#
# Mantener el orden original de los registros.
#
# Conservar los nombres de las mediciones.
#
# No modificar la lista original.
#
#
# =====================================================
# RESTRICCIONES
# =====================================================
#
# Utilizar try y except ValueError.
#
# No utilizar NumPy.
#
# Organizar el programa utilizando main().
#
# La función debe recibir los datos
# mediante un parámetro.
#
# No construir manualmente los resultados.
#
#
# =====================================================
# RAZONAMIENTO PREVIO
# =====================================================
#
# Antes de ejecutar:
#
# Predecir cómo quedará la lista original.
#
# Predecir cómo quedará la lista procesada.
#
# Considerar qué objetos deben ser nuevos
# y cuáles podrían compartir referencias.
#
# Escribir las predicciones como comentarios.
#
#
# =====================================================
# COMPROBACIONES
# =====================================================
#
# Imprimir la lista original.
#
# Imprimir la lista procesada.
#
# Comprobar mediante is si ambas listas
# externas son el mismo objeto.
#
# Comprobar mediante is si comparten
# sus primeras listas internas.
#
# Contrastar los resultados con las
# predicciones escritas previamente.
#
#
# =====================================================
# CONEXION CON CS231n Y MACHINE LEARNING
# =====================================================
#
# Esta práctica introduce el manejo de
# excepciones durante el procesamiento de datos.
#
# En proyectos de machine learning pueden
# aparecer datos inválidos o inesperados.
#
# Necesitamos identificar esos errores
# y decidir cómo tratarlos.
#
# También es importante controlar cuándo
# nuestros programas modifican los datos
# originales.
#
# En esta práctica recuperamos conceptos
# que ya estudiamos:
#
# - Funciones y parámetros.
# - Listas anidadas.
# - Mutabilidad.
# - Copias y referencias.
# - Identidad de objetos con is.
#
# Todo forma parte de un mismo objetivo.
#
# =====================================================
# IMPLEMENTACION
# =====================================================
#
# Escribir aquí la solución.

def copia_profunda(lista) -> list:
    nueva_lista = lista.copy()
    largo_lista = len(lista)
    for i in range(largo_lista):
        nueva_lista[i] = lista[i].copy()
    return nueva_lista

def procesar_registros(registros) -> list:
    resultado = copia_profunda(registros)
    for i in range(len(registros)):
        try:
            resultado[i][1] = int(registros[i][1])
        except ValueError:
            resultado[i][1] = None
    return resultado

def main():
    registros = [
        ["temperatura", "21"],
        ["humedad", "desconocido"],
        ["presion", "1013"],
        ["viento", "18a"],
        ["luz", "350"]
    ]
    # al hacer una copia profunda la copia original deberia permanecer igual
    # luego de procesar la lista, la nueva deberia quedar
    #  [
    #    ["temperatura", 21],
    #    ["humedad", None],
    #    ["presion", 1013],
    #    ["viento", None],
    #    ["luz", 350]
    #]
    # podria mantener la referencias a aquellos que no dan excepcion
    # si hubiera hecho una copia superficial, en caso de excepcion 
    # crearia un elemento nuevo y si no da excepcion sigo apuntando al mismo elemento de la lista original.
    print(registros)
    resultado = procesar_registros(registros)
    print(resultado)
    print(registros)
    print(registros is resultado)
    for i in range(len(resultado)):
        print(i,registros[i] is resultado[i])

if __name__ == "__main__":
    main()

'''
Ahora entendí, Clau. Estabas planteando una estrategia alternativa para evitar copiar todas las listas internas, conservando las referencias compartidas cuando fuera posible y creando objetos nuevos solamente cuando fuera necesario.

Esa estrategia existe y se conoce como copy-on-write (copia al escribir): compartir objetos mientras no necesitemos modificarlos.

Pero hay un detalle en este ejercicio.

Supongamos que tenemos:
original = ["temperatura", "21"]



Si la conversión funciona:
numero = int(original[1])



No modificamos original. Hasta ahí, perfecto.

Sin embargo, si queremos que el registro resultante contenga 21 como entero en lugar de "21" como texto, tenemos que reemplazar un elemento de la lista interna.

Y si esa lista interna sigue compartida, también modificaremos el original.

Lo mismo ocurre cuando la conversión falla y queremos colocar None.
Entonces, ¿cuándo podríamos compartir referencias?
- Si el registro no necesita cambios: podemos compartir su lista interna sin modificar el original.
- Si el registro necesita cambios: debemos crear una lista interna nueva antes de modificarla.
En nuestro ejercicio, todos los registros necesitan cambiar: unos de str a int y otros de str a None. Por eso tu implementación, que copia todas las listas internas, resulta apropiada.

Tu idea de minimizar las copias es válida. La condición fundamental no es si ocurrió una excepción, sino si necesitamos modificar un objeto compartido.

Y esa es una distinción importante entre reasignar una referencia, crear un objeto nuevo y modificar un objeto mutable.
'''    