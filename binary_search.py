
import math

def binary_search(list, item):
    low = 0 #posición mas baja
    high = len(list) - 1 #posición mas alta
    step = math.log(high,2)
    while (low <= high):
        mid = low + high #media del arreglo
        guess = list[mid]
        
        if (guess == item):
            return mid,step

        if (guess < item):
            low = mid + 1

        else:
            high = mid - 1
    return None

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

x,step = binary_search(my_list,10)
print("position in the array:",x)
print("steps:",step)


