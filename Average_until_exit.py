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
counter=0 # the counter counts the number of numbers given
total=0 # total is the summation of all numbers given
while True:  #creates an infinite loop until it breaks
    x=input('enter:')
    if x=='quit' or x=='Quit' or x=='Exit' or x=='exit': #if user enters any of these, the loop breaks
        break
    x=int(x) #if a number is given, this turns it into an int
    counter+=1 #a new number has been given, so counter has to go up one digit
    total+=x # the new number has been added to the summation
try:  # the following line will be tried until it encounters errors
    print(total/counter)
except ZeroDivisionError: # if the user enters 'exit' or 'quit', there are no given numbers, therefore the sum is divided by zero
    print('You have exited the program')
except ValueError: #if the user enters sth irrelevent, like an unknown character
    print('Invalid request')
