'''
Created on 2013-3-21

@author: duanhong
'''
from math import sqrt

def isPrime(num):
    if(num == 2): return True
    x = int(sqrt(num)) + 1
    for i in range(2, x + 1):
        if(num % i == 0):
            return False
    return True
    
def problem3(num):
    x = int(sqrt(num)) + 1
    for i in range(x, 1, -1):
        if(num % i == 0):
            if(isPrime(i)):
                return i
    return 2
            
print(problem3(600851475143))