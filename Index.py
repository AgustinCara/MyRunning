import Menu
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
        self.entrenamientos = [] # List[Entrenamiento]
        self.carreras = []       # List[Carrera]
        self.recorridos = []     # List[Recorrido]