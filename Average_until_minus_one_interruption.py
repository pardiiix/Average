# -*- coding: utf-8 -*-
"""
Created on August 4th, 2017

@author: Pardis Ranjbar
E-mail: pardis.ranjbar@gmail.com
#==============================================================================
# This code gets numbers from user and gives the average, until user enters '-1'.
#==============================================================================
"""
x=0
counter=0
total=0
while x!=-1:
    try:
        x=input('enter a number:')
        x=int(x)
    except ValueError: #if user does not enter an integer, the code asks them to try again
        print('Please enter an integer')
        x=input('enter a number:')
    x=int(x)
    counter+=1
    total+=x
    print('The average for now is:', total/counter, '\n')
try:
    print((total+1)/(counter-1))
except ZeroDivisionError:
    print('You entered -1')
