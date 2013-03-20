'''
Created on 2013-3-21

@author: duanhong
'''
# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    D = {}  
    q = 2  
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

my_gen = gen_primes()      
sum = 0  
for i in my_gen:
    if(i<2000000):
        sum += i
    else:
        break
print(sum)