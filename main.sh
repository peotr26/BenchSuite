#! /bin/bash

TIMEFORMAT=%R

# Setting variables for execution mono_threaded CPU benchmarks
rust_prime=$(time ./Programs/rust_prime/main)
python_prime_mono=$(time python Programs/python_prime/mono_threaded/main.py)
python_prime_multi=$(time python Programs/python_prime/multi-threaded/main.py)

$rust_prime
$python_prime_mono
$python_prime_multi