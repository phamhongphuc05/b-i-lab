# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:05:10 2024

@author: kid30
"""


def ngto(n):
    if n<= 1 : 
        return False 
    for i in range(2 ,int(n**0.5) + 1):
        if n%i==0 : 
            return False 
    return True 
def tongnguyen2 (n):
    S=0 
    for i in range(2,n):
       if ngto(i):
           S+=i
    return S
print(tongnguyen2(5)) 