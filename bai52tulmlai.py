# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:35:17 2024

@author: kid30
"""

#a
def cb(x,n):
    return n**1/x 
#b
def sodao(n):
        return str(n)[::-1]
#c
import math 
def ktr9p(n):
   return math.sqrt(n)==int(math.sqrt(n)) and n!=1
#d
def ngto(n):
    if n<1 : 
        return False 
    for i in range(2 ,int(n**0.5) + 1):
        if n%i==0 : 
            return False 
        return True 
#e 
def tichle(n): 
   if n<= 1 : 
       return False 
   for i in range(2 ,int(n**0.5) + 1):
       if n%i==0 : 
           return False 
   return True 
#f kì 
#def tongnguyen(n):
#   S=0 
 #   for i in range (2 ,n):
#      for y in range(2,int(i**0.5)+1):
 #           if i%y!=0: 
  #             S+=i
   # return S
# f  chạy chug ko ra 
def tongnguyen2(n):
    S=0 
    for i in range(2,n):
       if ngto(i):
           S+=i
    return S 
#g 
def tong9p(n):
    S=0 
    for i in range (2,n):
        if math.sqrt(i)==int(math.sqrt(i)):
           S+=i 
    return S
#
h
print (tong9p(5)) 
print(tongnguyen2(5 ))
print(tichle(3))
print(ngto(9))
print("n là số chính phương:",ktr9p(9))
print(sodao(2880))
print(cb(2,4))
    