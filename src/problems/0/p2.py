'''
Created on 2013-3-21

@author: duanhong
'''

def problem2():
    MAX_NUM = 4000000
    sum_of_even = 2
    first = 1
    second = 2
    while(1):
        if(first + second > MAX_NUM):
            break
        if((first + second)%2==0):
            sum_of_even += first + second
        first, second = second, first + second
    print(sum_of_even)
    
problem2()