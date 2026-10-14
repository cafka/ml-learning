'''
Consigna
Escribí una función llamada preparar_lote(tareas) que reciba una lista de tareas, cada una representada por un diccionario, 
y devuelva un lote preparado para procesar las tareas pendientes.

Datos de entrada
Conjunto principal
tareas = [
    {
        "id": 101,
        "estado": "pendiente",
        "historial": ["creada"],
    },
    {
        "id": 102,
        "estado": "completada",
        "historial": ["creada", "completada"],
    },
    {
        "id": 103,
        "estado": "pendiente",
        "historial": ["creada", "corregida"],
    },
]
Otros datos de entrada
tareas_vacias = []

tareas_terminadas = [
    {
        "id": 104,
        "estado": "completada",
        "historial": ["creada", "completada"],
    },
]
Condiciones que debe cumplir el programa
La función debe devolver el lote como una lista.
El lote debe incluir únicamente las tareas cuyo estado sea "pendiente", 
manteniendo el orden en que aparecen en la entrada.
En cada tarea del lote, el estado debe pasar a ser "lista".
En cada tarea del lote, se debe agregar la cadena "preparada" al final de su historial, 
conservando sus entradas anteriores y su orden. 
El id debe conservarse.
La lista de entrada y todo su contenido deben permanecer intactos al ejecutar la función.
Si posteriormente se modifica el historial de una tarea del lote, 
ese cambio tampoco debe afectar al historial de la tarea original.
La función debe admitir también una lista vacía y una lista sin tareas pendientes, aplicando las mismas reglas.
Podés asumir que todas las tareas tienen exactamente las claves id, estado e historial. Los identificadores son enteros, 
los estados son cadenas y los historiales son listas de cadenas. No hace falta validar entradas incorrectas.

Usá Python estándar, sin bibliotecas externas.
'''
def preparar_lote(tareas):
    # Recibe una lista de tareas, cada una representada por un diccionario, 
    # Devuelve un lote preparado para procesar las tareas pendientes
    aux = [x.copy() for x in (tareas) if x['estado'] == 'pendiente']
    for i in range(len(aux)):
        aux[i]['historial'] = aux[i]['historial'].copy()
        aux[i]['estado'] = 'lista'
        aux[i]['historial'].append('preparada')
    print(f"Aux ==> {aux}")
    return aux

def main():
    #Datos de entrada
    #Conjunto principal
    tareas = [
        {
            "id": 101,
            "estado": "pendiente",
            "historial": ["creada"],
        },
        {
            "id": 102,
            "estado": "completada",
            "historial": ["creada", "completada"],
        },
        {
            "id": 103,
            "estado": "pendiente",
            "historial": ["creada", "corregida"],
        },
    ]
    #Otros datos de entrada
    tareas_vacias = []

    tareas_terminadas = [
        {
            "id": 104,
            "estado": "completada",
            "historial": ["creada", "completada"],
        },
    ]
    lotes_vacios = preparar_lote([])
    print(lotes_vacios)
    print("========== tareas antes del cambio =========================")
    print(tareas)
    print("\n")
    lotes_pendientes = preparar_lote(tareas)
    print("========== preparar_lote(tareas) =========================")
    print(lotes_pendientes)
    print("\n")
    
if __name__ == "__main__":
    main()