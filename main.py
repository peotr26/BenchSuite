def ex_time(binary:str, args:str)->float:
    import time
    import subprocess
    start = time.time()
    subprocess.call([binary, args])
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