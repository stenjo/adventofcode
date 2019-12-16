from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def primes(n):
    divisors = [ d for d in range(2,n//2+1) if n % d == 0 ]
    return [ d for d in divisors if \
             all( d % od != 0 for od in divisors if od != d ) ]

def pickfactors(f,n):
    f = list(f)
    f.sort()
    print(f)
    factors = [0]
    fp = 1
    for fn in f:
        while fp < n:
            factors.append(fn)
            fp = reduce(lambda x, y: x*y, factors)

    return factors


# for n in [3084599, 1026085, 194633, 7661300]:
allprimes = []
for n in [924, 617, 2772, 924]:
    fac = factors(n)
    print(n, fac, pickfactors(fac, n))
    prims = primes(n)
    if len(prims):
        print(n, prims, reduce(lambda x, y: x*y, prims))
        allprimes += list(prims)

print(set(allprimes))
