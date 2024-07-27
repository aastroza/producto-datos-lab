# Test Estadísticos y Big Data

Este análisis compara las distribuciones de valores de características entre diferentes períodos de tiempo utilizando la prueba estadística de Kolmogorov-Smirnov (KS). La prueba KS es una prueba no paramétrica que evalúa si dos muestras provienen de la misma distribución

## Ejemplo

Supongamos que estamos midiendo la altura media de personas en dos poblaciones diferentes. Si tenemos muestras pequeñas, solo diferencias grandes en las alturas medias serán detectadas como significativas. Pero si tenemos millones de mediciones, incluso una diferencia de milímetros podría resultar en un valor p muy pequeño, indicando una diferencia significativa desde un punto de vista estadístico, pero posiblemente irrelevante en la práctica.

## Desglose del Análisis

### Paso 1: Definir el Contexto

**Objetivo:** Comparar la altura media de personas en dos poblaciones diferentes.

- **Escenario 1:** Muestras pequeñas.
- **Escenario 2:** Muestras grandes.

### Paso 2: Entender la Prueba Estadística

**Prueba Estadística:** Supongamos que usamos una prueba ks para comparar las medias de dos poblaciones.

- **Hipótesis nula (H0):** No hay diferencia en las alturas medias entre las dos poblaciones.
- **Hipótesis alternativa (H1):** Hay una diferencia en las alturas medias entre las dos poblaciones.

### Paso 3: Escenario 1 - Muestras Pequeñas

**Características:**

- Tamaño de muestra pequeño, por ejemplo, 30 personas en cada población.
- La variabilidad dentro de cada muestra es alta en relación con el tamaño de la muestra.

**Resultado:**

- Para que la prueba t detecte una diferencia significativa (rechace H0), la diferencia en las alturas medias entre las dos poblaciones debe ser bastante grande.
- Diferencias pequeñas en las alturas medias pueden no ser detectadas como significativas debido a la alta variabilidad y el tamaño reducido de la muestra.

**Conclusión en Escenario 1:**

- Solo diferencias grandes serán estadísticamente significativas.
- Diferencias pequeñas probablemente no serán detectadas debido al tamaño de muestra pequeño.


### Paso 4: Escenario 2 - Muestras Grandes

**Características:**

- Tamaño de muestra grande, por ejemplo, 1 millón de personas en cada población.
- La variabilidad dentro de cada muestra es menor en relación con el tamaño de la muestra debido a la ley de los grandes números.

**Resultado:**

- La prueba t ahora tiene un alto poder estadístico debido al gran tamaño de la muestra.
- Incluso una diferencia muy pequeña en las alturas medias entre las dos poblaciones puede resultar en un valor p muy pequeño, indicando una diferencia estadísticamente significativa.

**Ejemplo Numérico:**

- Supongamos que las alturas medias son 170.0 cm y 170.1 cm.
- Con muestras grandes, la diferencia de 0.1 cm puede resultar en un valor p muy pequeño (e.g., 0.00001), indicando una diferencia significativa.

**Conclusión en Escenario 2:**

- Diferencias muy pequeñas en las alturas medias pueden ser detectadas como significativas debido al gran tamaño de la muestra.
- Esto puede llevar a resultados que son estadísticamente significativos pero posiblemente irrelevantes desde un punto de vista práctico.


### Paso 5: Interpretación de Resultados

**Interpretación en la Práctica:**

- **Estadísticamente Significativo:** El valor p muy pequeño indica que hay una diferencia en las alturas medias entre las dos poblaciones que es poco probable que ocurra por azar.
- **Prácticamente Significativo:** La diferencia de 0.1 cm en alturas medias es probablemente irrelevante en la práctica, a pesar de ser estadísticamente significativa.

## Resumen

En resumen, en el contexto de big data, el gran tamaño de muestra aumenta el poder de las pruebas estadísticas, lo que permite detectar diferencias muy pequeñas como significativas. Sin embargo, es importante considerar si estas diferencias tienen relevancia práctica. En el ejemplo, una diferencia de 0.1 cm en alturas medias puede ser significativa desde un punto de vista estadístico, pero no necesariamente importante o relevante en un contexto práctico.