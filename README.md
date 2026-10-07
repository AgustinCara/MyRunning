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
