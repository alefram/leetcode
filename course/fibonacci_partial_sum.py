def get_fibonacci_mod(n, m):
    pisano_period = 60
    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    return current

def last_digit_partial_sum_fibonacci(from_, to):
    last_digit_to = get_fibonacci_mod(to + 2, 10)
    last_digit_from = get_fibonacci_mod(from_ + 1, 10)
    result = (last_digit_to - last_digit_from) % 10
    return result

if __name__ == "__main__":
    from_, to = map(int, input().split())
    print(last_digit_partial_sum_fibonacci(from_, to))
