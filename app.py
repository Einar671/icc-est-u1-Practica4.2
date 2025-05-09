from benchmarking import Benchmarking
from sort_methods import SortMethods
import matplotlib.pyplot as plt
import datetime
import random

class GraficoPersonalizado:
    def __init__(self):
        self.tamanos = [5000, 10000, 30000, 50000, 100000]
        self.benchmark = Benchmarking()
        self.sorter = SortMethods()
        
        self.metodos_dict = {
            "burbuja": self.sorter.sort_bubble,
            "bubbleMejorado": self.sorter.sort_bubble_optimized,
            "seleccion": self.sorter.sort_selection,
            "insercion": self.sorter.sort_insertion,
            "shell": self.sorter.sort_shell
        }
        
        self.colores = {
            "burbuja": "red",
            "bubbleMejorado": "orange",
            "seleccion": "green",
            "insercion": "blue",
            "shell": "purple"
        }
        
        self.resultados = []
    
    def build_arreglo(self, tamano):
        return [random.randint(1, 1000) for _ in range(tamano)]
    
    def ejecutar_pruebas(self):
        for tam in self.tamanos:
            arreglo_base = self.build_arreglo(tam)
            
            for nombre, metodo in self.metodos_dict.items():
                # Copiamos el arreglo para cada método
                arreglo_para_ordenar = arreglo_base.copy()
                tiempo = self.benchmark.medir_tiempo(metodo, arreglo_para_ordenar)
                self.resultados.append((tam, nombre, tiempo))
                print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")
    
    def generar_grafico(self):

        tiempos_por_metodo = {}
        for nombre in self.metodos_dict.keys():
            tiempos_por_metodo[nombre] = []
        
        
        for tam, nombre, tiempo in self.resultados:
            tiempos_por_metodo[nombre].append(tiempo)
        
        
        plt.figure(figsize=(10, 6), num="Algoritmos de Ordenación")
        
    
        for nombre, tiempos in tiempos_por_metodo.items():
            color = self.colores.get(nombre, None) 
            plt.plot(self.tamanos, tiempos, label=nombre, marker='o', color=color)
        
       
        plt.xlabel("Tamaño del Arreglo")
        plt.ylabel("Tiempo de Ejecución (segundos)")
        
        
        fecha_actual = datetime.datetime.now()
        fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
        titulo = f"Comparativa Métodos de Ordenación\nProyecto de Algoritmos - {fecha_formateada}"
        
        plt.title(titulo)
        plt.legend()
        plt.grid(True) 
        plt.savefig("comparativa_metodos_ordenacion.png")
        plt.show()

if __name__ == "__main__":
    print("Iniciando evaluación de algoritmos de ordenación...")
    grafico = GraficoPersonalizado()
    grafico.ejecutar_pruebas()
    grafico.generar_grafico()
    print("\nProceso completado. Se ha mostrado el gráfico comparativo y se ha guardado como 'comparativa_metodos_ordenacion.png'")
