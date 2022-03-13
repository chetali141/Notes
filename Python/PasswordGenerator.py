# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:55:41 2022

@author: user
"""

"""
A program that gives you a choice to either generate a password or secure your current password.
"""

import string
import random

secure = (('and','&'),('fine','f9'),('are','r'),('you','U'),('a','@'),('o','0'),('i','1'),('I','|'),('s','$'))

def securePassword(pwd):
    for a,b in secure:
        pwd = pwd.replace(a,b)
    print("The secure password generated is: ",pwd)

def generatePassword(plen):
    s = []
    s.extend(list(string.ascii_lowercase))
    s.extend(list(string.ascii_uppercase))
    s.extend(list(string.digits))
    s.extend(list(string.punctuation))
    pwd = "".join(random.sample(s,plen))
    print("The password generated for you is: ",pwd)


while(True):
    
    print("""
-----------------------
|        Menu         |
-----------------------
|1. Generate Password |
|2. Secure Password   |
-----------------------""")
    
    choice = int(input("Choose any one option:"))

    if (choice == 1):
        plen = int(input("Enter the length of your password: "))
        if plen<=4: 
            print("\nThe length is too short for a password, it should be atleast greater than 4.\nPlease try again :(")
            continue
        else:
            generatePassword(plen)
            key = input("Press any key to exit!")
            break
    elif (choice == 2):
        pwd = input("Enter the password: ")
        securePassword(pwd)
        key = input("Press any key to exit!")
        break
    else:
        print("You entered wrong number. Please choose either 1 or 2.")
        continue


