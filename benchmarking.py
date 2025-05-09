import time
from typing import Callable, List

class Benchmarking:

    def medir_tiempo(self, func: Callable[[List[int]], List[int]], array: List[int]) -> float:
        inicio = time.perf_counter()
        func(array)
        fin = time.perf_counter()
        return fin - inicio
