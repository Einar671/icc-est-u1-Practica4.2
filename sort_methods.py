class SortMethods:

    def sort_bubble(self, array):
        arreglo = array.copy()
        for i in range(len(arreglo)):
            for j in range(i+1,len(arreglo)):
                if arreglo[i]>arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo
    
    def sort_bubble_optimized(self, array):
        arreglo = array.copy()
        for i in range(len(arreglo)-1):
            for j in range(0,j<n-1-i):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[i]
    
    def sort_insertion_(self, array):
        arreglo = array.copy()
        for i in range(len(arreglo)-1):
            aux = arreglo[i]
            j = i-1

            for j in range(0,i>=0 and arreglo[i]> aux,-1):
                arreglo[j+1] = arreglo[j]
            arreglo[i+1] = aux
        return arreglo
    
    def sort_selection(self, array):
        arreglo=array.copy()
        n= len(arreglo)
        for i in range(0,n,1):
            maxIdx = i
            for j in range(i+1,n,1):
                if arreglo[maxIdx]> arreglo[j]:
                    maxIdx = j
            if maxIdx!=i:
                arreglo[maxIdx], arreglo[i] = arreglo[i], arreglo[maxIdx]
        return arreglo
    
    def sort_shell(self,array):
        arreglo = array.copy()
        for gap in range(len(arreglo)/2,gap>0,gap/2):
            for i in range(gap,i<len(arreglo)):
                aux = arreglo[i]
                j=i
                while(j>=gap and aux > arreglo[j-gap]):
                    arreglo[j] = arreglo[j-gap]
                    j-=gap
                
                arreglo[j]=aux
        return arreglo