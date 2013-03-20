'''
Created on 2013-3-21

@author: duanhong
'''
from math import pow
def problem9():
    for a in range(1,334):
        for b in range(a,667):
            if(a*a + b*b == pow(1000 - a - b, 2)):
                print(a)
                print(b)
                print(a * b * (1000 - a - b))
                return
                
problem9()