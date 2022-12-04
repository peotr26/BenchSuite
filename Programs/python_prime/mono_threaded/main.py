# This program was written by ChatGPT

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for n in range(2, 200000):
    if is_prime(n):
        prime_numbers.append(n)