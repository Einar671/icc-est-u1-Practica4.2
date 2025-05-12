# Práctica de Algoritmos de Ordenamiento

## 📌 Información General

- **Título:** Teoria de la complejidad
- **Asignatura:** Estructura de Datos  
- **Carrera:** Computación  
- **Estudiantes:** Einar Kaalhus, Israel Orellana 
- **Fecha:** 10 de mayo del 2025  
- **Profesor:** Ing. Pablo Torres  

---

## 🛠️ Descripción

Este proyecto implementa y compara diferentes algoritmos de ordenamiento en **Python**, incluyendo:

- Método Burbuja  
- Método Burbuja Mejorado  
- Método Selección  
- Método Inserción  
- Método Shell  

El objetivo es medir y graficar el tiempo de ejecución de cada uno de estos métodos con arreglos de diferentes tamaños. El sistema:

- Genera arreglos aleatorios automáticamente.  
- Ejecuta cada algoritmo con copias del mismo arreglo.  
- Registra y grafica los tiempos de ejecución.  
- Guarda el gráfico como imagen `.png`.  

---

## 🚀 Ejecución

Para ejecutar el proyecto:

1. Asegúrate de tener Python y las dependencias necesarias (como `matplotlib`).
2. Ejecuta el archivo principal:

```bash
python app.py
```

El programa mostrará el gráfico de comparación y guardará la imagen como `comparativa_metodos_ordenacion.png`.

---

## 🧪 Ejemplo de Salida por Consola

```plaintext
Iniciando evaluación de algoritmos de ordenación...
Tamaño: 5000, Método: burbuja, Tiempo: 1.531265 segundos
Tamaño: 5000, Método: bubbleMejorado, Tiempo: 1.320884 segundos
Tamaño: 5000, Método: seleccion, Tiempo: 1.114242 segundos
...
Proceso completado. Se ha mostrado el gráfico comparativo y se ha guardado como 'comparativa_metodos_ordenacion.png'
```

---

## 📈 Gráfico Generado

![Comparativa de Métodos de Ordenación](comparativa_metodos_ordenacion.png)

---

## ✅ Conclusiones

La comparación de los métodos de ordenamiento muestra que, en términos de notación Big-O, los algoritmos como **Shell Sort** tienen un mejor rendimiento promedio con una complejidad de \( O(n \log^2 n) \), mientras que algoritmos clásicos como **Burbuja**, **Inserción** y **Selección** presentan una complejidad de \( O(n^2) \). Por lo tanto, **Shell Sort** es significativamente más rápido en la mayoría de los casos, especialmente para arreglos de gran tamaño. Los métodos cuadráticos son adecuados solo para conjuntos de datos pequeños o con listas casi ordenadas.

---
