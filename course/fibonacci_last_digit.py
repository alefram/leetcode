def get_fibonacci_huge_mod(n, m):
    pisano_period = 60
    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    return current

def last_digit_of_sum_fibonacci(n):
    last_digit = get_fibonacci_huge_mod(n + 2, 10)
    result = (last_digit - 1) % 10
    return result

if __name__ == "__main__":
    n = int(input())
    print(last_digit_of_sum_fibonacci(n))
