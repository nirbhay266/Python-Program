def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

n = 190
prime_numbers = generate_primes(n)

print(f"The first {n} prime numbers are:")
for i, prime in enumerate(prime_numbers, start=1):
    print(f"{i}. {prime}")
