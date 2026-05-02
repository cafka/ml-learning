## Nota personal - ¿Por qué la función sigmoide usa `e` y no π?

Mientras repasaba el Lab03 me surgió una duda bastante natural:

> Entiendo que necesitamos una función que transforme cualquier valor en un número entre `0` y `1`, pero ¿por qué aparece la constante de Euler `e`?  
> ¿Por qué no π, por decir algo?

La respuesta corta es:

> Porque `e` aparece naturalmente cuando trabajamos con exponenciales, logaritmos, tasas de cambio y derivadas.  
> Y todo eso encaja perfecto con el entrenamiento de un modelo mediante descenso de gradiente.

La función sigmoide es:

```python
g(z) = 1 / (1 + e^(-z))
```

Esta función toma cualquier valor real de `z` y lo transforma en un valor entre `0` y `1`.

Eso sirve porque en regresión logística queremos interpretar la salida como una probabilidad.

Por ejemplo:

```text
z muy negativo  → probabilidad cercana a 0
z = 0           → probabilidad 0.5
z muy positivo  → probabilidad cercana a 1
```

La constante `e` no aparece por decoración matemática. Aparece porque la sigmoide está construida a partir de una función exponencial.

Y la función exponencial con base `e` tiene una propiedad especialmente cómoda:

```text
la derivada de e^x es e^x
```

Eso hace que la derivada de la sigmoide sea muy simple:

```text
g'(z) = g(z) * (1 - g(z))
```

Esa simplicidad es muy útil para el descenso de gradiente, porque permite calcular de forma limpia cómo ajustar los parámetros `w` y `b`.

También hay una interpretación más profunda.

En regresión logística no se modela directamente la probabilidad `p` con una recta, porque una recta puede dar valores menores que `0` o mayores que `1`.

En cambio, se modelan los **log-odds**:

```text
log(p / (1 - p)) = z
```

donde:

```text
z = w * x + b
```

Las odds comparan la probabilidad de que algo ocurra contra la probabilidad de que no ocurra:

```text
odds = p / (1 - p)
```

Y los log-odds son el logaritmo de esas odds:

```text
log-odds = log(p / (1 - p))
```

Al despejar `p` desde:

```text
log(p / (1 - p)) = z
```

se obtiene:

```text
p = 1 / (1 + e^(-z))
```

Es decir, aparece exactamente la función sigmoide.

Entonces la idea importante es:

```text
función lineal → log-odds → sigmoide → probabilidad
```

En mi ejemplo del laboratorio:

```text
horas de estudio → z → probabilidad de aprobar
```

La constante π aparece naturalmente en geometría, círculos, trigonometría y ondas.

La constante `e`, en cambio, aparece naturalmente en exponenciales, logaritmos, crecimiento, decaimiento, tasas de cambio y derivadas.

Por eso `e` encaja perfecto en regresión logística.

Versión informal para recordarlo:

> `e` está ahí porque la regresión logística vive en el mundo de exponenciales, logaritmos y derivadas.  
> π no tenía nada útil que hacer en esta fiesta, salvo acompañar la pizza circular.
