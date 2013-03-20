'''
Created on 2013-3-21

@author: duanhong
'''
def problem6():
    sum_of_square = 0
    sum = 0
    for i in range(1,101):
        sum_of_square += i * i
        sum += i
    print(sum * sum - sum_of_square)

def problem6_2():
    limit = 100
    sum = limit * (limit + 1) / 2
    sum_sq = (2*limit + 1) * (limit + 1) * limit/6
    print(sum * sum - sum_sq)
problem6()
problem6_2()