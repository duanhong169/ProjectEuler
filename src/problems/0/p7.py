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
    serial_num = 0
    while True:
        if q not in D:
            #yield q
            serial_num += 1
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        if(serial_num == 10001):
            print(q)
            break
        q += 1
        
gen_primes()