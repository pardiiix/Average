# -*- coding: utf-8 -*-
"""
Created on August 10th, 2017

@author: Pardis Ranjbar
E-mail: pardis.ranjbar@gmail.com
#==============================================================================
# This code gets numbers from user and gives the average, until user enters 'quit' or 'Exit'.
#==============================================================================
"""
x=0
counter=0
total=0
while True:  #creates an infinite loop until it breaks
    x=input('enter:')
    if x=='quit' or x=='Quit' or x=='Exit' or x=='exit':
        break
    x=int(x)
    counter+=1
    total+=x
try:
    print(total/counter)
except ZeroDivisionError:
    print('You have exited the program')
except ValueError:
    print('Invalid request')
