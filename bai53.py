# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:25:22 2024

@author: kid30
"""

#a) S = 1 + 2 + 3 +......+ n
def suma(n):
    return n*(n+1)//2 
#b) S = 1^2 +2^2 +3^2 +......+n^2
def sumb(n):
    return sum(i**2 for i in range(1,n+1))

#c) S = 1 + 1/2 + 1/3 +......+ 1/n
def sumc(n):
    return sum(1/i for i in range(1,n+1))

#d) S = 1! + 2! + 3! +......+ n!
import math 
def sumd(n):
    return sum(math.factorial(i) for i in range(1,n+1))
#d cách 2
def gthua(n):
    S=0
    gthua=1
    for i in range(1,n+1):
        gthua*=i
        S+=gthua 
    return S
print (gthua(4))

#e) S = 1 * 2 * 3 *......* n
def sume(n):
    S=1
    for i in range(1,n+1):
        S*=i
    return S
if __name__=="__main__":
    print("S = 1 + 2 + 3 +......+ n",suma(9))
    print("S = 1^2 +2^2 +3^2 +......+n^2",sumb(9))
    print("S = 1 + 1/2 + 1/3 +......+ 1/n",sumc(9))
    print("S = 1! + 2! + 3! +......+ n!",sumd(9))
    print("S = 1 * 2 * 3 *......* n",sume(9))
    
    