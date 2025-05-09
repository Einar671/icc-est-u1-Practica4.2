class SortMethods:

    def sort_bubble(self, array):
        arreglo = array.copy()
        for i in range(len(arreglo)):
            for j in range(i+1, len(arreglo)):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo

    def sort_bubble_optimized(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    swapped = True
            if not swapped:
                break
        return arreglo

    def sort_insertion(self, array):
        arreglo = array.copy()
        for i in range(1, len(arreglo)):
            aux = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > aux:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = aux
        return arreglo

    def sort_selection(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_idx]:
                    min_idx = j
            if min_idx != i:
                arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
        return arreglo

    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo
