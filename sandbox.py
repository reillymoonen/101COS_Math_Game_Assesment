def generate_primes():
    primes = []
    yield 2  # 2 is the first prime number
    candidate = 3

    while True:
        is_prime = all(candidate % prime != 0 for prime in primes)
        if is_prime:
            primes.append(candidate)
            yield candidate

        candidate += 2  # Skip even numbers (except for 2)

# Example: Generate the first 10 prime numbers
limit = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
prime_generator = generate_primes()

for _ in range(limit):
    print(next(prime_generator))

