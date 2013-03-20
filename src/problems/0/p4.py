'''
Created on 2013-3-21

@author: duanhong
'''
def isPalindromic(s):
    x = reversed(str(s))
    rev = ""
    for i in x:
        rev += i
    if rev == str(s):
        return True
    return False

def problem4():
    result = 0
    for i in range(999, 99, -1):
        for j in range(999, i-1, -1):
            if(i * j < result):    # inspired by PDF, this decrease the time consuming
                break
            if(isPalindromic(i * j)):
                result = i * j
    return result

print(problem4())