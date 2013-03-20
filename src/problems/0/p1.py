'''
Created on 2013-3-21

@author: duanhong
'''
def problem1(max_num):
    answer = 0
    for x in range(3, max_num):
        if(x%3 == 0 or x%5 == 0):
            answer = answer + x
    print(answer)
    
problem1(1000)