# ====================================================
# PRACTICA 28 - CONCATENACION DE ARRAYS EN NUMPY
# ====================================================
#
# HABILIDAD NUEVA: np.concatenate()
#
# Hasta ahora aprendimos a seleccionar,
# modificar y reorganizar datos en arrays.
#
# Ahora veremos cómo unir varios arrays
# para construir uno nuevo.
#
# ----------------------------------------------------
# 1. QUE HACE np.concatenate()
# ----------------------------------------------------
#
# np.concatenate() une arrays existentes a lo largo de un eje determinado.
#
# Sintaxis general:
#
# np.concatenate((A, B), axis=0)
#
# El primer argumento contiene los arrays.
#
# axis indica el eje en el cual se unen.
#
# Para matrices 2D:
#
# axis=0 -> unir a lo largo de las filas.
# axis=1 -> unir a lo largo de las columnas.
#
# IMPORTANTE:
#
# No se agrega una dimensión nueva. Se aumenta el tamaño de un eje existente.
# ----------------------------------------------------
# 2. REGLAS DE COMPATIBILIDAD
# ----------------------------------------------------
#
# Los arrays deben tener el mismo numero
# de dimensiones.
#
# Las dimensiones deben coincidir, excepto en el eje de concatenacion.
#
# Ejemplo:
#
# A.shape = (2, 3)
# B.shape = (4, 3)
#
# Se pueden concatenar con axis=0.
#
# Resultado: (6, 3)
#
# Pero no con axis=1, porque tienen
# distinta cantidad de filas.
#
# La concatenacion crea un nuevo array. No modifica los arrays originales.
#
# Si axis=None, NumPy aplana los arrays antes de concatenarlos.
#
#
# ----------------------------------------------------
# 3. EJEMPLO
# ----------------------------------------------------
#
# Tenemos una matriz con dos filas y dos columnas.
#
# Queremos agregar una columna nueva.
#
# ejemplo_a = np.array([
#     [2, 4],
#     [6, 8]
# ])
#
# ejemplo_b = np.array([
#     [10],
#     [20]
# ])
#
# Shapes originales:
#
# ejemplo_a -> (2, 2)
# ejemplo_b -> (2, 1)
#
# Podemos unirlos por el eje 1:
#
# unido = np.concatenate(
#     (ejemplo_a, ejemplo_b),
#     axis=1
# )
#
# Resultado:
#
# [[ 2  4 10]
#  [ 6  8 20]]
#
# Shape: (2, 3)
#
# Conservamos las dos filas. Agregamos una tercera columna.
# ----------------------------------------------------
# 4. CONTRAEJEMPLO
# ----------------------------------------------------
#
# Con esos mismos arrays:
#
# np.concatenate(
#     (ejemplo_a, ejemplo_b),
#     axis=0
# )
#
# Produce un ValueError.
#
# Porque al concatenar por axis=0, las columnas deben coincidir.
#
# ejemplo_a tiene 2 columnas.
# ejemplo_b tiene 1 columna.
#
# Sus dimensiones no son compatibles para esa concatenacion.
#
# ====================================================
# CONTEXTO DEL EJERCICIO
# ====================================================
#
# Un laboratorio realiza controles de calidad durante dos turnos de trabajo.
#
# Cada fila corresponde a una muestra. Cada columna representa una medicion.
#
# Cada muestra tiene cuatro mediciones.
#
# Tenemos tres muestras del turno de mañana
# y dos muestras del turno de tarde.
#
# Queremos analizar todas las muestras como un unico conjunto de datos.
#
#
# ====================================================
# DATOS INICIALES
# ====================================================
'''
turno_manana = np.array([
    [18, 20, 19, 21],
    [24, 22, 25, 23],
    [26, 27, 24, 25]
])

turno_tarde = np.array([
    [29, 25, 26, 28],
    [23, 30, 22, 21]
])
'''
# ====================================================
# OBJETIVO
# ====================================================
#
# Construir una matriz que contenga las muestras de ambos turnos.
#
# Conservar primero las muestras del turno de mañana.
#
# Colocar después las muestras del turno de tarde.
#
# De ese conjunto, conservar solamente las muestras donde al menos una medicion sea mayor que 27.
#
# El resultado debe conservar las cuatro columnas originales.
#
# Mantener el orden de las muestras
#
# ====================================================
# RESTRICCIONES
# ====================================================
#
# Utilizar np.concatenate().
#
# No utilizar bucles.
#
# No modificar los arrays originales.
#
# No construir manualmente el resultado.
#
# Utilizar operaciones de NumPy.
#
# Organizar el programa con main().
#
#
# ====================================================
# RAZONAMIENTO PREVIO
# ====================================================
#
# Antes de ejecutar, escribir como comentarios:
#
# Shape de turno_manana.
#
# Shape de turno_tarde.
#
# Shape esperado de los datos concatenados.
#
# Shape esperado de la matriz final.
#
# Explicar qué sucede con los ejes.
#
#
# ====================================================
# COMPROBACIONES
# ====================================================
#
# Imprimir el array concatenado y su shape.
#
# Imprimir la matriz final y su shape.
#
# Imprimir los arrays originales para verificar que no cambiaron.
#
# Comparar los resultados obtenidos con las predicciones anteriores.
#
# ====================================================
# CONEXION CON CS231n
# ====================================================
#
# En machine learning trabajamos frecuentemente con conjuntos de datos organizados en arrays y tensores.
#
# Es importante saber combinar datos conservando correctamente sus dimensiones.
#
# Tambien necesitamos seleccionar muestras que cumplen determinadas condiciones.
#
# Esta practica integra:
#
# - Concatenacion de arrays (nuevo).
# - Indexacion booleana (anterior).
# - Reducciones por ejes (anterior).
# - Prediccion de shapes (anterior).
#
# Todas estas operaciones contribuyen a desarrollar autonomia con NumPy.
#
#
# ====================================================
# IMPLEMENTACION
# ====================================================
#
# Escribir aqui tu codigo.
import numpy as np

def ambos_turnos(turno_mañana:np.ndarray, turno_tarde:np.ndarray) -> np.ndarray | None:
    try:
        concat = np.concatenate((turno_mañana, turno_tarde), axis = 0)
        # axis = 0 significa que la union se realiza en el eje de las filas
        return concat
    except ValueError:
        print("No se puede concatenar")

def main():
    turno_manana = np.array([
        [18, 20, 19, 21],
        [24, 22, 25, 23],
        [26, 27, 24, 25]
    ]) #shape (3,4)

    turno_tarde = np.array([
        [29, 25, 26, 28],
        [23, 30, 22, 21]
    ]) #shape (2,4)
    #shape esperado de datos concatenados (5,4)
    union_turnos = ambos_turnos(turno_manana, turno_tarde)
    if union_turnos is not None:
        print(union_turnos,union_turnos.shape)
        # De ese conjunto, conservar solamente las muestras donde al menos una medicion sea mayor que 27.
        mayor_27 = union_turnos > 27
        print(mayor_27)
        mascara = np.any(mayor_27,axis=1)
        resultado = union_turnos[mascara]
        print("Resultado:")
        print(resultado)
        print("Shape:", resultado.shape)
    print("arrays originales")        
    print(turno_manana, turno_manana.shape)
    print(turno_tarde, turno_tarde.shape)

if __name__ == "__main__":
    main()