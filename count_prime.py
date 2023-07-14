import numpy as np

import time


def countPrimes(n):
    if n<3:
        return 1
    Primes = np.ones(n) * n
    Primes[0] = 2
    compt = 1
    for k in range(3, n, 2):
        is_prime=True
        list_Primes = Primes[Primes<np.sqrt(k)+1]
        if 0 in k%list_Primes:
            is_prime=False
            continue
        Primes[compt] = k
        compt += 1

    return np.count_nonzero(Primes!=n)

def countPrimes2(n):
    if n<3:
        return 1
    Primes = np.array([2])
    for k in range(3, n, 2):
        list_Primes = Primes[Primes<np.sqrt(k)+1]
        if 0 in k%list_Primes:
            continue
        Primes = np.append(Primes, k)

    return len(Primes)

def countPrimes3(n):
        if n < 3:
            return 1

        numbers = set([i for i in range(4,n,2)])
        for p in range(3, int(np.sqrt(n)) + 1, 2):
            if p not in numbers:
                for multiple in range(p*p, n, p):
                    numbers.add(multiple)

        return n - len(numbers) - 2

t1 = time.time()
print(countPrimes(100000))
t2 = time.time()
print(countPrimes2(100000))
t3 = time.time()
print(countPrimes3(100000))
t4 = time.time()



print("first function time : ", t2-t1)
print("second function time : ", t3-t2)
print("third function time : ", t4-t3)








