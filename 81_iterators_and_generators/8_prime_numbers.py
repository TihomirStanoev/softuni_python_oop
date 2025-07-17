def is_prime(n):
    if n <= 1:
        return 0
    for d in range(2, n):
        if n % d == 0:
            return 0
    else:
        return n


def get_primes(nums):
    for n in nums:
        if is_prime(n):
            yield n







print(list(get_primes(range(0,100))))