## ¿Por qué en regresión logística usamos primero una función lineal?

En regresión logística, antes de aplicar la sigmoide se calcula:

$$
z = w \cdot x + b
$$

o, con varias variables:

$$
z = w_1x_1 + w_2x_2 + \dots + w_nx_n + b
$$

Esta parte se llama **combinación lineal de las variables**.

---

## ¿Qué representa `z`?

`z` representa una especie de **puntaje interno del modelo**.

No es todavía una probabilidad.

Es un valor numérico que combina la información de entrada:

- cada variable `x` aporta información;
- cada peso `w` indica cuánto pesa esa variable;
- `b` desplaza la decisión general del modelo.

Por ejemplo, si una variable aumenta el riesgo, su peso puede empujar `z` hacia valores positivos.  
Si una variable reduce el riesgo, puede empujar `z` hacia valores negativos.

---

## ¿Por qué una función lineal?

Porque es el modelo más simple que permite separar datos usando una frontera de decisión lineal.

La regresión logística básica intenta aprender una regla del tipo:

$$
w \cdot x + b = 0
$$

Esa ecuación define la **frontera de decisión**.

- Si `z > 0`, el modelo tiende a clasificar como clase 1.
- Si `z < 0`, el modelo tiende a clasificar como clase 0.
- Si `z = 0`, estamos justo en la frontera.

En una variable, esa frontera es un punto.  
En dos variables, es una recta.  
En más variables, es un hiperplano.

---

## ¿Por qué después usamos la sigmoide?

El problema es que `z` puede tomar cualquier valor:

$$
-\infty < z < +\infty
$$

Pero para clasificación binaria queremos una salida interpretable como probabilidad, es decir, un valor entre 0 y 1.

Por eso aplicamos la función sigmoide:

$$
g(z) = \frac{1}{1 + e^{-z}}
$$

Entonces:

$$
f_{w,b}(x) = g(z)
$$

o sea:

$$
f_{w,b}(x) = \frac{1}{1 + e^{-(w \cdot x + b)}}
$$

La sigmoide transforma el puntaje lineal `z` en una probabilidad.

---

## Interpretación

- Si `z` es muy positivo, la sigmoide se acerca a 1.
- Si `z` es muy negativo, la sigmoide se acerca a 0.
- Si `z = 0`, la sigmoide vale 0.5.

Por eso, con umbral 0.5:

$$
g(z) \geq 0.5 \Rightarrow y = 1
$$

$$
g(z) < 0.5 \Rightarrow y = 0
$$

Como la sigmoide vale 0.5 cuando `z = 0`, la frontera de decisión queda determinada por:

$$
w \cdot x + b = 0
$$

---

## Idea central

La regresión logística combina dos partes:

1. Una parte lineal:

$$
z = w \cdot x + b
$$

que define el puntaje y la frontera de decisión.

2. Una transformación sigmoide:

$$
g(z)
$$

que convierte ese puntaje en una probabilidad entre 0 y 1.

Por eso no usamos directamente otra función más compleja al inicio: la regresión logística básica busca aprender una frontera lineal simple, interpretable y eficiente. Si los datos requieren fronteras más complejas, se pueden agregar nuevas características, por ejemplo variables polinómicas, pero el modelo sigue aplicando una combinación lineal sobre esas características.
