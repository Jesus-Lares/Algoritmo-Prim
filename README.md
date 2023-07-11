# Algoritmo-Prim

## Descripción

El algoritmo de Prim, dado un grafo conexo, no dirigido y ponderado, encuentra un árbol de expansión mínima. Es decir, es capaz de encontrar un subconjunto de las aristas que formen un árbol que incluya todos los vértices del grafo inicial, donde el peso total de las aristas del árbol es el mínimo posible.

### Funcionamiento del algoritmo de Prim

- Se marca un vértice cualquiera. Será el vértice de partida.
- Se selecciona la arista de menor peso incidente en el vértice seleccionado anteriormente y se selecciona el otro vértice en el que incide dicha arista.
- Repetir el paso 2 siempre que la arista elegida enlace un vértice seleccionado y otro que no lo esté. Es decir, siempre que la arista elegida no cree ningún ciclo.
- El árbol de expansión mínima será encontrado cuando hayan sido seleccionados todos los vértices del grafo.

**Grafo utilizado**

![Imagen Grafo](https://github.com/Jesus-Lares/Algoritmo-Prim/blob/main/grafo.png)

## Author

**JesusLares**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-jesusLares-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/jesusLares)
<br />
[![Web](https://img.shields.io/badge/jesuslares.com-5865F2?style=for-the-badge&logo=dev.to&logoColor=white&labelColor=101010)](https://jesuslares.com)
<br />
[![Github](https://img.shields.io/badge/jesuslares-238636?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/JesusLares)
<br />

## Ejemplo

En este grafo, las interacciones necesarias para recorrer todos los puntos con el menor peso posible son (iniciando por a):

```
('a', 'f')
('a', 'b')
('b', 'c')
('c', 'z')
('b', 'd')
('c', 'e')
('f', 'g')
```

Dando como consecuencia que se fueran todando los puntos en este orden ` ['a', 'f', 'b', 'c', 'z', 'd', 'e', 'g']`

## Instalacion

Este projecto requiere tener `python`. Posterior a esto, simplemente abre la carpeta en la terminal y corre el comando `python metodoPrim.py`

## Contacto

Si quieres contactarme puedes escribirme a contacto@jesuslares.com para consultas

## Licencia

MIT Public License v3.0 No puede usarse comercialmente
