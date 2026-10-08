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
