'''
Created on 2013-3-21

@author: duanhong
'''
from math import log
from math import sqrt

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes(upperlimit):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        if(q > upperlimit):
            break
        q += 1
        

def problem5(upperlimit):
    '''1.0 duanhong169'''
    result = 1
    while(1):
        for i in range(upperlimit, 1, -1):
            if(result % i != 0):
                result += i - result % i
                break
            if(i == 2):
                return result

#print(problem5(10))

def problem5_2(upperlimit):
    '''2.0 projecteuler'''
    p = [i for i in gen_primes(upperlimit)]
    p.append(upperlimit + 1)
    a = [1 for i in gen_primes(upperlimit)]
    N = 1
    i = 0
    check = True
    limit = sqrt(upperlimit)
    while(p[i] <= upperlimit):
        if(check):
            if(p[i] <= limit):
                a[i] = int(log(upperlimit)/log(p[i]))
            else:
                check = False
        N = N * p[i] ** a[i]
        i = i + 1
    return N
    
print(problem5_2(20))