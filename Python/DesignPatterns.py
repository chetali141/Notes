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

"""
B. 
* * * 
*   *
* * *
"""
print("\n Rectangle \n")

i = 1
n = 10

while i<=n :
    if(i==1):
        print(" *"*n)
    elif(i==n):
        print (" *"*n)
    else:
        print(" *"," "*(2*(n-3))," *")
    i = i + 1
    
