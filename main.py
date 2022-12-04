def rust_time()->float():
    import time
    import subprocess
    binary = 'Programs/rust_prime/main'
    start = time.time()
    subprocess.call([binary])
    end = time.time()
    time = end - start
    score = 1/time
    return score

def rust_time_score(n:int)->float():
    result = []
    for i in range(0,n):
        result.append(rust_time())
    score = sum(result)/len(result)
    return score