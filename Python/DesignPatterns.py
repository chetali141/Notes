# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:01:21 2022

@author: user
"""

#Ques: Print the following designs using loops. 

"""
A.
  *
 * *
* * *
"""
print("\n Equilateral Triangle \n")

i = 1
n = 20

while i<=n:
    space = n-i
    print(" "*space,"* "*i)
    i = i + 1
