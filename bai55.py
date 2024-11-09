# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:25:40 2024

@author: kid30
"""
#55 Viết phương thức tính chu vi và diện tích hình chữ nhật khi biết độ dài 2 
#cạnh. Sau đó vẽ hình chữ nhật ra màn hình bằng các dấu *. Phương thức 
#tính chu vi, diện tích và phương thức vẽ hình chữ nhật phải độc lập nhau.

def chuvi(a,b):
    return 2*(a+b)
def dt(a,b):
    return a*b 
def vehinh(a,b):
    for _ in range(b):
        print ('*'*a)
if __name__=="__main__":
    print (chuvi(5,4 ))
    print(dt(5,4)) 
    print (vehinh(5,4 )) 



    
     