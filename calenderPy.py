# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 03:57:50 2018

@author: leone
"""

days = ["S", "M", "T","W", "Th", "F", "S"]
for d in days:
    print ("{0:4s}".format(d.rjust(4)), end ="")
print ("")
    
daysInMonth = 31
numberOfWeeks = int(daysInMonth / 7)

currentDay = 1
for w in range(numberOfWeeks):
     for cw in range(0, 7):
         print ('{0:4d}' .format(currentDay), end = "")
         currentDay += 1
         
     print ("")
     
for d in range(currentDay, daysInMonth + 1):
        print ('{0:4d}' .format(d), end = "")
print ("")
         