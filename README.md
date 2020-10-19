# Algoritmo-Prim

El algoritmo de Prim, dado un grafo conexo, no dirigido y ponderado, encuentra un árbol de expansión mínima. Es decir, es capaz de encontrar un subconjunto de las aristas que formen un árbol que incluya todos los vértices del grafo inicial, donde el peso total de las aristas del árbol es el mínimo posible.

## Funcionamiento del algoritmo de Prim

- Se marca un vértice cualquiera. Será el vértice de partida.
- Se selecciona la arista de menor peso incidente en el vértice seleccionado anteriormente y se selecciona el otro vértice en el que incide dicha arista.
- Repetir el paso 2 siempre que la arista elegida enlace un vértice seleccionado y otro que no lo esté. Es decir, siempre que la arista elegida no cree ningún ciclo.
- El árbol de expansión mínima será encontrado cuando hayan sido seleccionados todos los vértices del grafo.

**Grafo utilizado**

![Imagen Grafo](https://github.com/Jesus-Lares/Algoritmo-Dijkstra-Python/blob/master/algoritmoDijkstra.png)
