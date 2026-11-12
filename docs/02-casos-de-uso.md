# 02 - Casos de uso de My Running

## 1. Introducción

Para diseñar My Running pensamos en las acciones que una persona realiza cuando quiere organizar sus entrenamientos.

Por ejemplo, después de salir a correr puede querer registrar cuántos kilómetros hizo, consultar otros recorridos o comparar su ritmo con entrenamientos anteriores.

A partir de estas situaciones identificamos los principales casos de uso de nuestra aplicación.

## 2. Actor principal

**Corredor o corredora:** persona que utiliza My Running desde la terminal para registrar entrenamientos y consultar información.

El programa no requiere iniciar sesión ni crear una cuenta.

## 3. Casos de uso

### CU01 - Registrar un entrenamiento

**Objetivo:** guardar los datos de una salida de running durante la ejecución del programa.

**Situación de ejemplo:** una persona corre 5 km en 30 minutos y quiere registrar el resultado.

**Pasos:**

1. El usuario abre My Running.
2. Selecciona la opción para registrar un entrenamiento.
3. Ingresa los datos solicitados, como lugar, distancia y tiempo.
4. El programa incorpora el entrenamiento a los registros disponibles.

**Resultado esperado:** el entrenamiento queda registrado y puede utilizarse en otras funcionalidades mientras el programa permanece abierto.

### CU02 - Consultar recorridos

**Objetivo:** conocer los recorridos disponibles para entrenar.

**Situación de ejemplo:** una persona quiere salir a correr y busca un recorrido de aproximadamente 5 km.

**Pasos:**

1. El usuario abre el menú principal.
2. Selecciona la opción de consulta de recorridos.
3. El programa muestra los recorridos disponibles.
4. El usuario revisa los lugares y las distancias.

**Resultado esperado:** el usuario puede conocer las alternativas disponibles para elegir dónde correr.

### CU03 - Explorar categorías

**Objetivo:** consultar recorridos organizados por dificultad, lugar y distancia.

**Situación de ejemplo:** una persona quiere conocer qué recorridos de dificultad fácil están disponibles.

**Pasos:**

1. El usuario selecciona la opción **5. Explorar categorías**.
2. El programa muestra las categorías organizadas en un árbol general.
3. El usuario puede visualizar la estructura o buscar una categoría o lugar.
4. El programa muestra la información correspondiente.

**Resultado esperado:** los recorridos aparecen agrupados jerárquicamente, facilitando su exploración.

**Estructura utilizada:** árbol general (TP5).

### CU04 - Consultar los mejores ritmos

**Objetivo:** conocer los tres entrenamientos con mejor ritmo.

**Situación de ejemplo:** una persona tiene varios entrenamientos registrados y quiere identificar sus mejores resultados.

**Pasos:**

1. El usuario selecciona la opción **6. Ranking de mejores ritmos**.
2. El programa toma los entrenamientos registrados.
3. Los incorpora a un Min-Heap ordenado por ritmo.
4. Extrae y muestra hasta tres entrenamientos con los ritmos más bajos.

**Resultado esperado:** el programa muestra los mejores entrenamientos indicando lugar, distancia y ritmo.

**Estructura utilizada:** Min-Heap (TP6).

### CU05 - Comparar resultados después de un nuevo entrenamiento

**Objetivo:** comprobar cómo cambia el ranking al registrar un entrenamiento con mejor ritmo.

**Situación de ejemplo:** una persona registra 5 km en 30 minutos, equivalentes a 6:00 min/km.

**Pasos:**

1. El usuario registra un entrenamiento nuevo.
2. Regresa al menú principal.
3. Selecciona la opción **6. Ranking de mejores ritmos**.
4. El programa construye el ranking con los entrenamientos disponibles.
5. El usuario observa si el nuevo entrenamiento aparece entre los tres mejores.

**Resultado esperado:** si el nuevo ritmo es mejor que los anteriores, el entrenamiento aparece en una posición superior del ranking.

Este caso nos permitió comprobar durante las pruebas que los entrenamientos nuevos participan del ranking.

## 4. Relación entre los casos de uso y las estructuras de datos

| Caso de uso | Funcionalidad | Estructura o recurso |
|---|---|---|
| CU01 | Registrar entrenamientos | Registros en memoria |
| CU02 | Consultar recorridos | Catálogo de recorridos |
| CU03 | Explorar categorías | Árbol general |
| CU04 | Consultar mejores ritmos | Min-Heap |
| CU05 | Comparar resultados nuevos | Registro de entrenamientos y Min-Heap |

## 5. Diagrama de casos de uso

```mermaid
flowchart LR
    A["Corredor/a"]

    subgraph S["MY RUNNING"]
        CU1(["CU01: Registrar entrenamiento"])
        CU2(["CU02: Consultar recorridos"])
        CU3(["CU03: Explorar categorías"])
        CU4(["CU04: Consultar mejores ritmos"])
        CU5(["CU05: Comparar resultados nuevos"])
    end

    A --- CU1
    A --- CU2
    A --- CU3
    A --- CU4
    A --- CU5

El actor principal es el corredor o corredora, que interactúa con las funcionalidades disponibles en My Running.

El diagrama representa las cinco situaciones descritas anteriormente.

## 6. Conclusión

Los casos de uso nos ayudaron a relacionar las funciones del programa con situaciones que pueden presentarse durante los entrenamientos.

También nos permitieron comprobar que las estructuras de datos incorporadas tienen una finalidad concreta dentro de My Running.

El árbol general facilita la exploración de recorridos y el Min-Heap permite consultar los mejores ritmos sin tener que ordenar manualmente todos los entrenamientos.
