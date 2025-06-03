"""pairwise exame course 1"""
import sys

def max_pairwise_product(arr, n):
    # Sort the array 
    arr.sort() 
    num1 = num2 = 0
  
    # Calculate product of two smallest numbers 
    sum1 = arr[0] * arr[1] 
  
    # Calculate product of two largest numbers 
    sum2 = arr[n - 1] * arr[n - 2] 
  
    # Print the pairs whose product is greater 
    if (sum1 > sum2): 
        num1 = arr[0] 
        num2 = arr[1] 
    else: 
        num1 = arr[n - 2] 
        num2 = arr[n - 1] 

    return num1 * num2

if __name__ == "__main__":

    #get an integer from the first input line
    _ = int(input())
    numbers = list(map(int, input().split()))

    result = max_pairwise_product(numbers, len(numbers))
    print(result)
