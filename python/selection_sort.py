def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1,len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


# selection sort algorithm

def selection_sort(array):
    newArray = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        newArray.append(array.pop(smallest))
    return newArray

print(selection_sort([5,6,2,10]))

