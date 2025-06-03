def get_fibonacci_mod(n, m):
    pisano_period = 60
    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    return current

def last_digit_sum_squares_fibonacci(n):
    fn = get_fibonacci_mod(n, 10)
    fn1 = get_fibonacci_mod(n + 1, 10)
    return (fn * fn1) % 10

if __name__ == "__main__":
    n = int(input())
    print(last_digit_sum_squares_fibonacci(n))
