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

i = 1
n = 3

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
print("\n")

i = 1
n = 3

while i<=n :
    if(i==2):
        print(" *     *")
    else:
        print (" * "*n)
    i = i + 1

