import math

def primes(N):
    """Finds all primes in range (2, N), returns as list"""
    n = int(-(-math.sqrt(N) // 2) - 1)
    l = int(-(-N // 2) - 1)
    gen = [True] * l
    
    for x in range(n):
        if gen[x]:
            X = x * 2 + 3
            for y in range(x + X, l, X):
                gen[y] = False
                
    primes = [2] + [z * 2 + 3 for z in range(l) if gen[z]]
    
    return primes

print(primes(10000))