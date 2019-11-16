Ejercicio 14 parte 2

1) Si lamda es 1, se obtiene una ecuación diferencial lineal de segundo orden.

2) Las soluciones son funciones seno y coseno ya que son las unicas cuya segunda derivada es igual a la función.

3) Programa adjunto en el repositorio.

4) Al graficar y(0) en función del tiempo se ve una funcion senoidal que siempre tiene la misma amplitud ya que no es amortiguada, este osiclador va a osiclar infinitamente.

5) Ambas implementaciones tanto la de Euler como la rk4, permiten ver el comportamiento del sistema del oscilador armónico, sin embargo como se observa en la imagen superior derecha del ejercicio, se observan unas leves diferencias, donde el método de Euler no es del todo exacta, el método RK4 se aproxima mejor a la solución.

6) Al graficar y(0) vs y(1), se observa una especie de elipse, esto es porque se esta graficando una señal senoidal vs una señal cosenoidal las cuales al graficarlas juntas forma una elipse ya que las amplitudes son distintas.

7) Al añadir el termino de la fricción el sistema converge a un valor en el tiempo, el cual es la posición cero en ambos ejes, y por lo tanto la elipse uniforme que antes se tenia ahora va reduciendo en amplitud y converge al punto (0,0)

8) Al aumentar el valor de lamda, no es posible graficar las soluciones de la ecuacion diferencial porque se convierte en no lineal y estos métodos no brinda una solución para este sistema de forma
correcta y salen como lienas rectas.
