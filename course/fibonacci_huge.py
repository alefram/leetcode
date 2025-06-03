def pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_huge(n, m):
    pisano = pisano_period(m)
    n = n % pisano

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
