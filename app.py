from typing import List, Dict, Tuple
from benchmarking import Benchmarking
from sort_methods import SortMethods
import random

class App:

    def __init__(self):
        self.tamanos: List[int] = [5000, 10000, 30000,50000,100000]
        self.max_tamano: int = max(self.tamanos)
        self.arreglo_base: List[int] = self.build_arreglo(self.max_tamano)
        
        self.benchmark = Benchmarking()
        self.sorter = SortMethods()  
        
        self.algoritmos: Dict[str, callable] = {
            "bubble": self.sorter.sort_bubble,
            "bubbleMejorado": self.sorter.sort_bubble_optimized,
            "seleccion": self.sorter.sort_selection,
            "insercion": self.sorter.sort_insertion,
            "shell": self.sorter.sort_shell
        }

        self.resultados: List[Tuple[int, str, float]] = []

    def build_arreglo(self, tamano: int) -> List[int]:
        return [random.randint(1, 1000) for _ in range(tamano)]

    def main(self):
        for tam in self.tamanos:
            arreglo = self.arreglo_base[:tam]
            for nombre, metodo in self.algoritmos.items():
                tiempo = self.benchmark.medir_tiempo(metodo, arreglo)
                self.resultados.append((tam, nombre, tiempo))
                print(f"Tamano: {tam}, Algoritmo: {nombre}, Tiempo: {tiempo:.4f} segundos")
