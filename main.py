# General functions:

def exec(binary:str, args:str):
    import subprocess
    subprocess.call([binary, args])

def data(file_name:str):
    with open(file_name, 'r') as f:
        data = first_line = f.readline()
    return data

# Functions for CPU benchmarks:

def ex_time(binary:str, args:str)->float:
    import time
    import subprocess
    exec(binary, args)
    end = time.time()
    time = end - start
    score = 1/time
    return score

def rust_time(n:int)->float:
    result = []
    for i in range(0,n):
        time = ex_time('Programs/rust_prime/main', '')
        result.append(time)
    score = sum(result)/len(result)
    score *= 100000
    return score

def python_prime_mono(n:int)->float:
    result = []
    for i in range(0,n):
        time = ex_time('/bin/python', 'Programs/python_prime/mono_threaded/main.py')
        result.append(time)
    score = sum(result)/len(result)
    score *= 10000
    return score

def python_prime_multi(n:int)->float:
    result = []
    for i in range(0,n):
        time = ex_time('/bin/python', 'Programs/python_prime/multi_threaded/main.py')
        result.append(time)
    score = sum(result)/len(result)
    score *= 1000000
    return score

def pi_calc(n:int)->float:
    result = []
    for i in range(0,n):
        time = ex_time('Programs/pi_calc/main', '')
        result.append(time)
    score = sum(result)/len(result)
    score *= 100000
    return score

# Functions for the GPU benchmark:

def vkmark(n:int)->int:
    result = []
    for i in range(0,n):
        exec('/bin/dash', 'Programs/vkmark/main.sh')
        result.append(data('Programs/vkmark/result.txt'))
    score = sum(result)/len(result)
    score *= 100000
    return score

def glmark2(n:int)->int:
    result = []
    for i in range(0,n):
        exec('/bin/dash', 'Programs/glmark2/main.sh')
        result.append(data('Programs/glmark2/result.txt'))
    score = sum(result)/len(result)
    score *= 100000
    return score