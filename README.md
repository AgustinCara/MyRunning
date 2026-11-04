# 🏃 My Running - Running Personal Manager

Proyecto práctico para **Estructuras de Datos y Algoritmos en Python**.

---

## 📌 ¿De qué trata el proyecto?

**My Running** es un programa sencillo para corredores amateurs. Permite anotar entrenamientos, ver cuántos kilómetros llevamos acumulados, consultar próximas carreras y buscar circuitos para salir a correr según los kilómetros que queramos hacer.

---

## 📂 Organización de los Archivos

El proyecto está separado en dos archivos principales:

- **`Index.py`**: Contiene las clases del sistema (`Entrenamiento`, `Recorrido` y `GestorMyRunning`).
- **`menu.py`**: Contiene el menú interactivo, los datos y las opciones del programa.

---

## 🧱 Clases del Dominio (`Index.py`)

```python
class Entrenamiento:
    def __init__(self, id_entrenamiento: int, fecha: str, distancia_km: float, tiempo_min: float, hr_promedio: int, lugar: str):
        self.id = id_entrenamiento
        self.fecha = fecha
        self.distancia_km = distancia_km
        self.tiempo_min = tiempo_min
        self.hr_promedio = hr_promedio
        self.lugar = lugar
        self.ritmo = self.tiempo_min / self.distancia_km if self.distancia_km > 0 else 0.0

class Recorrido:
    def __init__(self, id_recorrido: int, nombre: str, distancia_km: float, dificultad: str):
        self.id = id_recorrido
        self.nombre = nombre
        self.distancia_km = distancia_km
        self.dificultad = dificultad

class GestorMyRunning:
    def __init__(self):
        self.entrenamientos = [] 
        self.carreras = []       
        self.recorridos = []
```

---

## TP2 - Análisis de complejidad

Para este punto elegimos comparar dos formas de buscar recorridos según la distancia.

### Estrategias utilizadas

- **Búsqueda secuencial:** recorre los recorridos uno por uno hasta encontrar la distancia buscada.
- **Búsqueda binaria:** trabaja con los recorridos ordenados por distancia y va dividiendo la búsqueda en partes.

### Resultados

Probamos las dos búsquedas con distintas cantidades de recorridos.

| Cantidad de recorridos | Búsqueda secuencial | Búsqueda binaria |
|---|---|---|
| 100 | 0.0060 ms | 0.0006 ms |
| 1.000 | 0.0152 ms | 0.0024 ms |
| 10.000 | 0.1374 ms | 0.0041 ms |

Los tiempos pueden variar según la computadora donde se realice la prueba.

### Complejidad

- Búsqueda secuencial: **O(n)**
- Búsqueda binaria: **O(log n)**

### Conclusión

En las pruebas vimos que la búsqueda secuencial tarda más a medida que aumenta la cantidad de recorridos, porque puede tener que revisar toda la lista.

La búsqueda binaria resultó más rápida porque en cada paso descarta una parte de los recorridos. Para utilizarla, los datos tienen que estar ordenados por distancia.


---

## TP3 - Árbol binario de búsqueda

Para este trabajo incorporamos un árbol binario de búsqueda (ABB) a My Running para organizar y buscar recorridos según su distancia en kilómetros.

### Implementación

Creamos el archivo `arbol_recorridos.py`, que contiene las clases `Nodo` y `ArbolRecorridos`.

El árbol permite:

- Insertar recorridos según su distancia.
- Buscar recorridos por kilómetros.
- Guardar varios recorridos que tengan la misma distancia.
- Recorrer el árbol en inorden, preorden y postorden.

### Integración con My Running

Incorporamos el árbol a la opción 3 del menú, que permite buscar recorridos por distancia.

Agregamos lugares de Zona Sur, como Quinta Rocca - UNaB, Parque Finky, Parque de Lomas y un circuito urbano de Longchamps.

Las distancias son objetivos de entrenamiento sugeridos, excepto el circuito urbano, que se basa en un entrenamiento real de aproximadamente 8 km.

### Pruebas

Creamos `prueba_tp3.py` para comprobar la inserción, la búsqueda y los tres recorridos del árbol.

También comprobamos que el programa puede encontrar varios recorridos con la misma distancia.

### Comparación de tiempos

Usamos `comparacion_tp3.py` para comparar la búsqueda secuencial del TP2 con la búsqueda mediante el árbol binario.

| Cantidad de recorridos | Búsqueda secuencial | Árbol binario |
|---|---|---|
| 100 | 0.001377 ms | 0.000277 ms |
| 1.000 | 0.013841 ms | 0.000456 ms |
| 10.000 | 0.149765 ms | 0.000638 ms |

Para las pruebas usamos recorridos generados automáticamente. Insertamos los datos mezclados en el árbol y repetimos cada búsqueda 1.000 veces para obtener un tiempo promedio.

Los tiempos corresponden solamente a la búsqueda y no incluyen la construcción del árbol.

### Complejidad

- Búsqueda secuencial: **O(n)** en el peor caso.
- Árbol binario de búsqueda: **O(log n)** cuando está razonablemente equilibrado.
- En el peor caso, si el árbol queda muy desbalanceado, su búsqueda puede ser **O(n)**.

### Conclusión

En las pruebas vimos que la búsqueda con el árbol binario fue más rápida que la búsqueda secuencial, especialmente cuando aumentó la cantidad de recorridos.

El árbol nos permite organizar los recorridos por distancia y encontrar distintas opciones para correr. También aprendimos que su rendimiento depende de cómo estén acomodados los datos dentro del árbol.


## TP4 - Árbol AVL

En esta etapa incorporamos un árbol AVL para organizar los recorridos de My Running según su distancia.

A diferencia del árbol binario del TP3, el AVL utiliza rotaciones para mantenerse equilibrado cuando se agregan nuevos recorridos.

### Pruebas realizadas

Insertamos las distancias 3, 5, 8, 10, 12, 15 y 18 km en ambos árboles, en orden ascendente.

Luego buscamos el recorrido de 18 km y comparamos los resultados.

| Prueba | Árbol binario | Árbol AVL |
|---|---|---|
| Nodos recorridos | 7 | 3 |
| Tiempo de 10.000 búsquedas | 0,004076 s | 0,001660 s |

### Conclusión

En esta prueba, el árbol AVL necesitó recorrer menos nodos y realizó las búsquedas en menos tiempo que el árbol binario.

Esto ocurrió porque los recorridos se insertaron en orden ascendente, provocando que el árbol binario quedara desbalanceado. El AVL, en cambio, realizó rotaciones para mantener su equilibrio.

Los tiempos pueden variar entre ejecuciones y corresponden a esta prueba específica.


## TP5 - Árbol general (n-ario)

En esta etapa incorporamos un árbol general para organizar los recorridos de My Running en categorías.

A diferencia del ABB y del AVL, que tienen como máximo dos hijos por nodo y sirven para ordenar por distancia, en el árbol general cada nodo puede tener **cualquier cantidad de hijos**. Por eso sirve para representar una jerarquía.

### Jerarquía elegida

```text
Recorridos
├── Fácil
│   ├── Quinta Rocca - UNaB
│   │   ├── 2.0 km
│   │   └── 3.0 km
│   ├── Parque Finky
│   │   └── 3.0 km
│   └── ...
└── Media
    ├── Parque de Lomas
    │   └── 7.0 km
    └── ...
```

- **Raíz:** todos los recorridos.
- **Nivel 1:** la dificultad (Fácil, Media).
- **Nivel 2:** el lugar donde se corre.
- **Hojas:** cada distancia disponible en ese lugar. Solo las hojas guardan el objeto `Recorrido`.

### Implementación

Creamos el archivo `arbol_general.py`, que contiene las clases `NodoGeneral` y `ArbolGeneral`. Cada nodo guarda su nombre y una lista de hijos.

El árbol permite:

- Agregar hijos a cualquier nodo.
- Buscar categorías o lugares por nombre, sin importar mayúsculas.
- Mostrar el camino desde la raíz hasta un nodo (ejemplo: `Recorridos > Media > Parque Finky`).
- Obtener todos los recorridos que hay debajo de una categoría.
- Recorrer el árbol en preorden, postorden y por niveles.
- Calcular la altura y la cantidad de nodos.
- Dibujar el árbol en la terminal.

El árbol se arma automáticamente a partir de la lista de recorridos del menú.

### Integración con My Running

Agregamos la opción **5. Explorar categorías** al menú principal.

Esta opción permite visualizar el árbol completo, buscar una categoría o lugar y consultar los recorridos que pertenecen a cada categoría.

### Pruebas

Creamos `prueba_tp5.py` para comprobar la construcción del árbol, la búsqueda, el camino, los recorridos y la altura.

Realizamos una prueba con las categorías Fácil y Media, incorporando lugares y distintas distancias.

Obtuvimos los siguientes resultados:

- La búsqueda de Plaza encontró correctamente su ubicación dentro del árbol.
- Se recuperaron los recorridos de 2 y 3 km de la categoría Fácil.
- Los recorridos en preorden, postorden y por niveles funcionaron correctamente.
- La altura del árbol fue de **4 niveles**.
- La cantidad total de nodos fue de **8**.

También comprobamos desde el menú que la opción 5 muestra correctamente los lugares y las distancias agrupados por dificultad.

### Complejidad

- Búsqueda por nombre: **O(n)**, porque puede ser necesario revisar todos los nodos.
- Preorden, postorden y por niveles: **O(n)**, porque visitan cada nodo una vez.
- Cantidad de nodos: **O(n)**, porque utiliza el recorrido en preorden.

### Conclusión

El árbol general no sirve para buscar más rápido como el ABB o el AVL, sino para representar cómo se relacionan los datos.

Nos permitió agrupar los recorridos por dificultad y lugar, y navegarlos de forma más natural desde el menú.

---

## TP6 - Heap y ranking de entrenamientos

En esta etapa incorporamos una estructura de datos **Heap (montículo)** para organizar los entrenamientos de My Running según su ritmo y obtener un ranking de los mejores resultados.

Elegimos implementar un **Min-Heap**, porque cuanto menor es el tiempo que tardamos en recorrer un kilómetro, mejor es el ritmo.

### Implementación

Creamos el archivo `heap_entrenamientos.py`, que contiene la clase `HeapEntrenamientos`.

Implementamos el Heap manualmente, sin utilizar la biblioteca `heapq`, para comprender cómo funciona esta estructura.

El Heap permite:

- Insertar entrenamientos.
- Comparar los entrenamientos según su ritmo.
- Reorganizar los elementos para mantener la propiedad del Min-Heap.
- Extraer el entrenamiento con mejor ritmo.
- Obtener los tres mejores entrenamientos.

Para mantener el orden utilizamos los métodos `subir()` y `bajar()`, que intercambian elementos cuando es necesario.

### Integración con My Running

Agregamos la opción **6. Ranking de mejores ritmos** al menú principal.

Esta opción toma los entrenamientos registrados, los incorpora al Heap y muestra los tres mejores resultados, indicando el lugar, la distancia y el ritmo expresado en minutos y segundos por kilómetro.

Los entrenamientos nuevos también participan del ranking mientras el programa está en ejecución.

### Pruebas

Creamos `prueba_heap_tp6.py` para comprobar el funcionamiento de la estructura.

Utilizamos siete entrenamientos de ejemplo basados en registros reales, sin incluir datos personales.

Comprobamos que el Heap identifica correctamente el mejor ritmo y permite extraer los tres mejores entrenamientos en orden.

También verificamos desde el menú que un entrenamiento nuevo con mejor ritmo pasa a ocupar el primer puesto.

### Comparación de tiempos

Creamos `comparacion_tp6.py` para comparar dos maneras de obtener los tres mejores entrenamientos:

- **Min-Heap:** insertar los entrenamientos y extraer los tres mejores.
- **sorted():** ordenar todos los entrenamientos por ritmo y seleccionar los tres primeros.

Realizamos pruebas con 1.000 y 10.000 entrenamientos generados automáticamente.

| Cantidad de entrenamientos | Min-Heap | sorted() |
|---|---|---|
| 1.000 | 0,000568 s | 0,000244 s |
| 10.000 | 0,007203 s | 0,001752 s |

Además, repetimos cinco veces la comparación con 10.000 entrenamientos para obtener un tiempo promedio.

Los resultados fueron:

- **Min-Heap:** 0,013843 segundos.
- **sorted():** 0,001659 segundos.

En nuestras pruebas, `sorted()` resultó más rápido que la implementación manual del Heap.

Los tiempos pueden variar según la computadora y las condiciones de ejecución.

### Complejidad

- Insertar un entrenamiento en el Heap: **O(log n)**.
- Extraer el mejor entrenamiento: **O(log n)**.
- Consultar el mejor elemento sin extraerlo: **O(1)**.
- Construir el Heap mediante inserciones sucesivas: **O(n log n)**.
- Ordenar todos los entrenamientos con `sorted()`: **O(n log n)** en el peor caso.

### Conclusión

El Heap nos permitió incorporar una estructura de prioridad a My Running y obtener un ranking de entrenamientos según el ritmo.

Aunque `sorted()` fue más rápido en nuestros experimentos, el Heap resulta útil cuando necesitamos incorporar nuevos elementos y consultar o extraer repetidamente el de mayor prioridad, sin ordenar toda la colección en cada operación.

Esta etapa nos permitió comprender el funcionamiento de los montículos y comparar su comportamiento con una herramienta de ordenamiento de Python.
