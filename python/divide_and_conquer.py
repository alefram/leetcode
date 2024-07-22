
def simple_sum(arr):
    if arr == []:
        return 0
    else:
        total = arr[0] + simple_sum(arr[1:])
        return total


if __name__ == '__main__':

    arr = [2,4,6]
    x = simple_sum(arr)
    print(x)
