---
title: "Guía de términos CAD Tuberculosis"
authors: "Santiago Correa Marulanda, Sara Galván Ortega"
tutors: "Maria Bernarda Salazar, Luis Felipe Buitrago Castro"
bibliography: references.bib
csl: ieee.csl
---


# Diccionario

Como parte de la documentación del CAD se incluye este diccionario que explica el significado de las características (features) extraídas de las imágenes a analizar. 

Como se puede ver en el README dichas imágenes son un conjunto de radiografías de tórax.

## Extracción de características

    Es el proceso mediante el cual se transforma información compleja, como una imagen, en un conjunto de variables numéricas que contienen propiedades consideradas relevantes para el problema.

La extracción de características es una fase crucial en la clasificación de enfermedades respiratorias, ya que permite identificar patrones y rasgos asociados a afecciones específicas. Consiste en obtener información de alto nivel a partir de imágenes, como el color, la forma y la textura, asegurando que solo se consideren las áreas relevantes para el análisis [@tonni2025framework].

Acontinuación se explican las caracteríticas de manera agrupada 

### Gray-Level Co-Occurrence Matrix (GLCM) features

El GLCM es un modelo estadístico que considera las conexiones espaciales entre píxeles, capturando información textural significativa sobre la distribución espacial de las intensidades de los píxeles y permitiendo la caracterización de los patrones de los tejidos. [@tonni2025framework;@prince2025interpretable]

Las enfermedades respiratorias presentan patrones de textura distintivos y complejos, y el uso de descriptores de características de textura como GLCM ayuda a capturar la complejidad y ambigüedad inherentes a estos patrones.

Los descriptores de características derivadas de este modelo, son las siguientes:

#### Contraste (Contrast)

Es una característica de textura que cuantifica cuánto difieren entre sí las intensidades entre los píxeles de referencia y los pixeles vecinos;  un contraste significativo indica variaciones significativas dentro de la matriz de coocurrencia de niveles de gris (GLCM), mientras que valores más altos indican anomalías en el tejido pulmonar. 

#### Disimilitud (Dissimilarity)

 Es una medida de textura que cuantifica la diferencia absoluta entre los niveles de gris de pares de píxeles. A diferencia del contraste, utiliza la diferencia absoluta en lugar de elevarla al cuadrado.

#### Homogeneidad (Homogeneity)

1. Medida que indica qué tan concentrados están los elementos de una matriz de coocurrencia alrededor de su diagonal. Una mayor homogeneidad significa que los niveles de gris de los píxeles relacionados tienden a ser similares. [@prince2025interpretable]

2. La homogeneidad en la GLCM mide la distribución de los elementos; una mayor homogeneidad resulta en un menor contraste. Los pulmones sanos muestran valores de homogeneidad y energía más altos, lo que indica uniformidad de la textura. [@tonni2025framework]
 
#### Energía (Energy)

La energía cuantifica la uniformidad local de los niveles de gris; valores más altos indican una mayor similitud entre píxeles.

#### Correlación (Correlation)

La característica de correlación indica la relación lineal entre los valores de los niveles de gris dentro de la matriz de coocurrencia.

### 

### Característica de textura (Texture feature)






