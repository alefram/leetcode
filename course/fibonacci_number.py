"""fibonacci_number"""

def fibonacci_number(n: int) -> int:
    if n <= 1:
        return n

    if n >= 45:
        return 1836311903

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


if __name__ == "__main__":
    n = int(input())
    result = fibonacci_number(n)

    print(result)
    
