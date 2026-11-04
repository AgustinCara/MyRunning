class HeapEntrenamientos:

    def __init__(self):
        self.datos = []

    def insertar(self, entrenamiento):
        self.datos.append(entrenamiento)
        self.subir(len(self.datos) - 1)

    def subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2

            if self.datos[indice].ritmo < self.datos[padre].ritmo:
                self.datos[indice], self.datos[padre] = (
                    self.datos[padre], self.datos[indice]
                )
                indice = padre
            else:
                break

    def bajar(self, indice):
        cantidad = len(self.datos)

        while True:
            izquierdo = 2 * indice + 1
            derecho = 2 * indice + 2
            menor = indice

            if izquierdo < cantidad:
                if self.datos[izquierdo].ritmo < self.datos[menor].ritmo:
                    menor = izquierdo

            if derecho < cantidad:
                if self.datos[derecho].ritmo < self.datos[menor].ritmo:
                    menor = derecho

            if menor == indice:
                break

            self.datos[indice], self.datos[menor] = (
                self.datos[menor], self.datos[indice]
            )

            indice = menor

    def extraer_mejor(self):
        if len(self.datos) == 0:
            return None

        mejor = self.datos[0]
        ultimo = self.datos.pop()

        if len(self.datos) > 0:
            self.datos[0] = ultimo
            self.bajar(0)

        return mejor