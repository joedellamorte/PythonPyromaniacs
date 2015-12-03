# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:12:22 2015

@author: June
"""

#import 
#
#alpha = [][][][][]
#for x in 'abcdefghijklmnopqrstuvwxyz'
#        alpha[x]= [][][][][]
#alpha = {'a':[][],'b':[][],'c':[][],'d':[][],'e':[][],'f':[][],'g':[][],\
#'h':[][],'i':[][],'j':[][],'k':[][],'l':[][],'m':[][],'n':[][],'}

import numpy as np
import math

course = "LinearAlgebra"
inpt = "LinarAbebra"
distance = 0
#def distance(course,inpt):
alpha = {}
count = 0
for x in 'abcdefghijklmnopqrstuvwxyz':
    alpha[x] = count
    count += 1

matrix = np.empty((3,26))

for x in range(26):
    matrix[0][x] = x
    
for letter in course:
    for key in alpha:
        if key==letter:
            matrix[1][alpha[key]] += 1
for letter in inpt:
    for key in alpha:
        if key==letter:
            matrix[2][alpha[key]] += 1
for x,y in zip(matrix[1][:],matrix[2][:]):
    distance += (x-y)**2
distance = math.sqrt(distance)
print(distance)                      
print(matrix)
            
    
    