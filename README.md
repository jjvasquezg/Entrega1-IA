## 1.1 Descripción

### Primera parte
Este proyecto en su primera parte implementa un sistema de planificación de rutas para un agente autónomo en un entorno bidimensional, inspirado en un escenario de exploración planetaria.  
El objetivo principal es encontrar el camino óptimo entre un punto inicial y un punto objetivo, minimizando el costo total de desplazamiento, el cual depende de la naturaleza del terreno.  
Se utilizan algoritmos de búsqueda informada, específicamente A*, para garantizar la optimalidad de la solución cuando la heurística es admisible y consistente.

### Segunda parte

En la segunda parte del proyecto se implementa un sistema que consiste en planificar una rutina semanal de 7 días que combine correr (R), gimnasio (G) y descanso (D) de manera equilibrada. Se deben cumplir varias restricciones: no entrenar más de tres días seguidos, incluir al menos dos sesiones de correr y dos de gimnasio, y limitar los descansos a un máximo de tres por semana. Además, se busca que los descansos se distribuyan estratégicamente tras bloques de 2–3 días de entrenamiento, favoreciendo tanto la recuperación como la continuidad del progreso físico.


---

## 1.2 Tecnologías

- **Lenguaje de programación:** Python 3.x
- **Librerías:**
  - `heapq` para la gestión de la cola de prioridad en A*.
  - `time` para la medición de tiempos de ejecución.
  - `os` para manejar archivos y directorios del sistema.
  - `json` y `csv` para crear y manipular archivos .json y .csv respectivamente
  - `random` para generar números aleatorios.
- **Control de versiones:** Git y GitHub (Wiki y repositorio principal).
- **Formato de documentación:** Markdown para la wiki.

---

## 1.3 Integrantes

- Juan Jose Vasquez Gomez
- Santiago Alvarez Peña