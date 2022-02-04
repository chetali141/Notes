# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:09:35 2022

@author: user
"""

import math

# the variable disk has the number of disk
disk = int(input("Number of disks = "))

#the recursive function to solve the problem
def TowerOfHanoi(disk, source, destination, auxiliary):
    if disk == 1:
        print("Moving disk 1 from ",source," to ",destination)
        return
    TowerOfHanoi(disk-1,source,auxiliary,destination)
    print("Moving disk ",disk," from ",source," to ",destination)
    TowerOfHanoi(disk-1,auxiliary,destination,source)
    

#calculating the total number of moves required.
moves = int(math.pow(disk, 2) - 1)
print("\nTotal number of moves required to move ",disk," disks are: ",moves,"\n")

# calling the recursive function for three rods: A,B,C where the Rod A is the source and Rod C is the destination
TowerOfHanoi(disk, 'Rod A','Rod C','Rod B')    
