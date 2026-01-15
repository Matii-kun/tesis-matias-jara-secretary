Código correspondiente al Capítulo 4 para el caso de rango general k.

En esta carpeta se implementa y analiza el programa dinámico asociado
al problema **Todo o nada** para un matroide uniforme de rango k,
junto con sus verificaciones computacionales y comparaciones con
resultados teóricos.

Estructura del código:

1. programa_dinamico/
   Implementación del programa dinámico para rango general k.
   Incluye el cálculo del valor óptimo y de los tiempos r_i.

2. prueba_pd/
   Pruebas computacionales del programa dinámico.
   Se verifican valores y tiempos para distintos pares (N, k),
   incluyendo casos borde.

3. lehtinen_vs_pd/
   Comparación entre el programa dinámico y los valores límite
   obtenidos por Lehtinen.
   Contiene el código que genera las figuras presentadas en el Capítulo 4.
