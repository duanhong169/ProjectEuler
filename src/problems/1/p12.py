# -*- coding:utf-8 -*-
'''
Created on 2013-3-21

@author: duanhong
'''
from math import sqrt

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

def gen_triangle_numbers():
    q = 0
    n = 1
    while True:
        q = q + n
        yield q
        n += 1

my_triangle_numbers_gen = gen_triangle_numbers()

for i in my_triangle_numbers_gen:
    num_divisors = 2
    for x in range(2, int(sqrt(i))):
        if(i%x == 0):
            num_divisors += 2
        if(i == x*x):
            num_divisors -= 1 
    if(num_divisors > 500):
        print(i)
        break