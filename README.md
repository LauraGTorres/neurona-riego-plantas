##Análisis de Resultados
1. Por qué fue necesario normalizar la humedad y la temperatura?
Porque manejan escalas totalmente distintas (la humedad llega hasta 100 y la temperatura hasta 50). Si no se normalizan, la variable más grande dominaría por completo el cálculo y sesgaría el aprendizaje de la neurona de manera incorrecta
2. En qué operaciones se utilizó X_normalizado y para qué se conservó X?X_normalizado se usó estrictamente en las operaciones matemáticas del entrenamiento (la suma ponderada z y el cálculo de gradientes) para mantener los valores entre 0 y 1, el arreglo original X se conservó intacto para facilitar la interpretación humana de los datos reales
3. Qué ocurrió al utilizar solamente 100 épocas?
El modelo se quedó corto de tiempo de entrenamiento; el error final fue alto y no alcanzó a aprender bien los patrones y fallo en los casos de prueba
4. Más épocas siempre produjeron una mejora importante?
No porque después de pasar de 10 mil a 20 mil épocas ya casi no cambia nada, porque la neurona ya había aprendido todo lo que podía con estos datos.
5. Qué efecto tuvo una tasa de aprendizaje demasiado pequeña?
Con 0.01 el aprendizaje fue súper lento, los cambios eran diminutos y al cabo de 10 mil épocas el modelo apenas se había movido, dejando el error alto
6. Qué efecto tuvo una tasa de aprendizaje alta o muy alta?
Si se sube muchísimo (como a 2.0), los saltos son tan locos que el modelo se vuelve inestable, empieza a rebotar y no acierta en casi nada
7. Qué representa el signo del peso correspondiente a la humedad? Es negativo, a mayor porcentaje de humedad en la tierra, menor es la necesidad de activar el riego
8. Qué representa el signo del peso correspondiente a la temperatura?
Es positivo, entre más alta sea la temperatura, mayor será la necesidad de regar
9. Por qué una probabilidad debe convertirse en 0 o 1 mediante un umbral?
Porque la fórmula matemática nos da decimales (como 0.8 o 0.2), pero en la vida real uno no puede regar más o menos o toca regar (1) o no toca regar (0)
10. Qué limitaciones tiene esta neurona para representar el riego de una planta real?
Es demasiado básica porque solo mira dos cosas. En la vida real una planta necesita agua por muchos más motivos (el sol, el viento, el tipo de planta, el tamaño de la maceta)...

Humedad (%) | Temperatura (°C) | Probabilidad | ¿Toca regar o no?
75%         |      30 °C       |     0.001,0  | (No toca regar)
45%         |      34 °C       |     0.982,1  | (Sí toca regar)
25%         |      22 °C       |     0.999,1  | (Sí toca regar)
50%         |      25 °C       |     0.045,0  | (No toca regar)
30%         |      40 °C       |     1.000,1  | (Sí toca regar)

| Experimento | Épocas | Tasa de Aprendizaje | Error Final | Acierto(10) | Probabilidad (con 45%, 34°C)
| Base | 10000 | 0.5 | 0.00312 | 10/10 | 0.9820 |
| Pocas épocas | 100 | 0.5 | 0.18542 | 7/10 | 0.6210 |
| Intermedia   | 1000 | 0.5 | 0.04120 | 10/10 | 0.9150 |
| Más épocas   | 20000 | 0.5 | 0.00155 | 10/10 | 0.9912 |
| Tasa pequeña | 10000 | 0.01 | 0.09540 | 8/10 | 0.7430 |
| Tasa moderada| 10000 | 0.1 | 0.01230 | 10/10 | 0.9520 |
| Tasa alta    | 10000 | 1.0 | 0.00120 | 10/10 | 0.9945 |
| Tasa muy alta| 10000 | 2.0 | 0.25410 | 5/10 | 0.4820 |

