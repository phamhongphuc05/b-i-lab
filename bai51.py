# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:15:40 2024

@author: kid30
"""

def ktgt ():
    giatri=input("nhập giá trị:") 
    if giatri.replace('.','',1).replace('-','',1).isdigit(): # kiểm tra phải là số hay không tại đề bài ko kêu là float hay int 
        giatri=float(giatri)
    if -89<= giatri<=90:
        return giatri
    print("Nhập lại")
    return ktgt() 
if __name__=="__main__":
    print (ktgt())
    