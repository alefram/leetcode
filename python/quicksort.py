def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        #el elemento pivotante
        pivot = arr[0]

        #tomar el arreglo con los numeros menores que el pivotante
        less = [i for i in arr[1:] if i <= pivot]
        
        #tomar el arreglo con los elementos mayores al pivotante
        greater = [i for i in arr[1:] if i > pivot]

        #devolver la recursividad
        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    x = [10,5,2,3]
    print(quicksort(x))
