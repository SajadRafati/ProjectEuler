# -*- coding: utf-8 -*-
"""
Created on sun Jul  6 00:04:13 2022

@author: SajadRafati
"""
# projecteuler 16
# Power digit sum
# What is the sum of the digits of the number 2**1000?
# answer is: "1366"
x = []
y = []
for i in range(1, 101):
    i **= 2
    x.append(i)
    z = sum(x)
    b = int(z)
for j in range(1, 101):
    y.append(j)
    v = sum(y)
    v **= 2 
    
print(v - b)