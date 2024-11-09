# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:12:37 2024

@author: kid30
"""

def kt (x):
    if x<0 and x%2!=0:
        return -1
    elif x>0 and x%2==0:
        return 1
    return 0
if __name__=="__main__":
    print(kt(6 ))
    
    