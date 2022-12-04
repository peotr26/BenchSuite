# This program was parttialy written by ChatGPT

import threading
from multiprocessing import cpu_count

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end, prime_numbers):
    for n in range(start, end):
        if is_prime(n):
            prime_numbers.append(n)

prime_numbers = []

# Determine the number of threads to use
num_threads = cpu_count()

# Split the range of numbers to check into equal-sized chunks
chunk_size = (2000000 - 2) // num_threads
ranges = [(i * chunk_size + 2, (i + 1) * chunk_size + 2) for i in range(num_threads)]

# Launch one thread per chunk of numbers
threads = []
for start, end in ranges:
    thread = threading.Thread(target=find_primes, args=(start, end, prime_numbers))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()