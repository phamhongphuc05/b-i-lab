# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:47:11 2024

@author: kid30
"""

def fib(n):
    a,b=0,1 
    while a<n:
        print(a,end=" ")
        a,b = b, a+b 
    return ()
print(fib(1000 ))