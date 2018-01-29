#!/usr/bin/env python3
__author__ = "Matthew Ng"
__date__ = "1/17/18"
from matplotlib import pyplot as plt

def int_or_float(s):
   '''
   Function from John Machin on stackoverflow
   https://stackoverflow.com/questions/5608702/how-can-i-convert-a-string-to-either-int-or-float-with-priority-on-int
   @param s string that is either a float or int
   @return the number in float or int form depending on what it is
   '''
   try:
      return int(s)
   except ValueError:
      return float(s)

def is_number(s):
   '''
   Function from Daniel Goldberg on stackoverflow
   https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
   @param s string to determine if that string is a number
   @return T/F depending on if that string is a number
   '''
   try:
      float(s)
      return True
   except ValueError:
      return False


with open("eric.csv") as file:
   lines = [line.partition('#')[0].rstrip() for line in file]# Removes comments
   lines = [line.split(",")[:2] for line in lines] #splits up string and returns first 2 elem
   lines = [[x.strip() for x in line] for line in lines if len(line) > 1] #removes less than 2 elem
   plt.xlabel(lines[0][0]) #x label on plot
   plt.ylabel(lines[0][1]) #y label on plot
   lines = [x for x in lines if is_number(x[0]) and is_number(x[1])] #keeps if both elem are #'s

   #splitting up the list into X and Y
   lines_x = [int_or_float(line[0]) for line in lines[1:]]
   lines_y = [int_or_float(line[1]) for line in lines[1:]]

   plt.title('Homework 1 - Matthew Ng') #title
   plt.plot(lines_x, lines_y) #plot values
   plt.show() #show graph
