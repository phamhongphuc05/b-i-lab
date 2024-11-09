# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:17:25 2024

@author: kid30
"""
import math 
#a 
def cb (x,n):
    if n>0:
      return n**(1/x) 
print (cb(2,9 ))
#b
def nd(n):
    return 1/n
print(nd(9))
#c
def cp(n): 
    return  math.sqrt(n)==int(math.sqrt(n)) and n!=1 
print("n phải số nguyên tố không:",cp(1))
#d
def nguyento(n) :
    if n<2:
        return " không phải số nguyên tố."
    for i in range (2,int(n**0.5) + 1):
        if n % i ==0:
            return "không là sô nguyên tố"
    return "là số nguyên tố"
print(nguyento(9)) 
#e) Phương thức tính tích các chữ số lẻ.


def tichsole(n):
    S=1 
    for i in range(1,n+1):
        i=int(i) 
        if i%2!=0 :
          S*=i
    return S
print (tichsole(7)) 
#f Phương thức tính tổng các số nguyên tố nhỏ hơn n
def nto(n):
    S=0 
    for i in range(2,n):
        for y in range(2 ,int(i**0.5)+1 ):
           if i%y!=0:
             S+=i 
    return S
print(nto( 6  )) 
#g) Phương thức tính tổng các số chính phương nhỏ hơn n.

def cphuongnho(n):
    S=0
    for i in range(2,n): #số 1 không phải số chính phương dương  
       if math.sqrt(i)==int(math.sqrt(i)):
           S+=i 
    return S
print("tổng số chính phương nhỏ hơn n", cphuongnho(5 ))
        
#h) Phương thức tính tổng các ước số dương của n.
def tonguocso(n):
    S=0
    for i in range(1,n+1):
        if n%i==0:
            S+=i
    return S
print(" tổng các ước số của n là",tonguocso(2))



# từ 2 hàm trở lên phải đưa pritn xuống câu if name 
            
      
    
            
          
      


    
    