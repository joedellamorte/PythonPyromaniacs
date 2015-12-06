# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:12:22 2015

@author: June Hua 
"""
###############################################################################
###############################################################################
""" This program accounts for typos in the User's entries. The database of 
course attributes will be searched to find the closest course to the course
the User entered """
###############################################################################
###############################################################################

import numpy as np
import math

def distance(course,inpt):
    distance = 0
    alpha = {}
    count = 0
    beta = 'abcdefghijklmnopqrstuvwxyz0123456789'

    matrixcour = np.empty(26)
    matrixinp = np.empty(26)
    
    for i in range(26):
        distance += (inpt.count(beta[i])-course.count(beta[i]))**2

        return distance


print(distance("linear algebra","linear algebra"))
    
    





"-----------------------------------------------------------------------------"
#dataBase = ["course","title","prof","section"] #checks all of database
#inpt = ["course","title","profe","section"] #what user inputs
#alpha = {}
#distance = 0 
#entered = 8 #number of components user enters
################################################################################
#""" Places alphabet in dict, with value of corresponding num 0 - 25 """
################################################################################
#count = 0
#for x in 'abcdefghijklmnopqrstuvwxyz':
#    alpha[x] = count
#    count += 1
################################################################################
#""" matrixAlpha: empty matrix will record the # of each letter A - Z
#    matrixNum: empty matrix will record # of numbers from 0 - 9 """
################################################################################    
#matrixAlpha = np.empty((9,26))
#matrixNum = np.empty((9,10))
################################################################################
#"""Sets the row 0 of matrixAlpha and matrixNum to 0 - 26 and 0 - 9 respectively"""
################################################################################
#for x in range(26):
#    matrixAlpha[0][x] = x
#for x in range(10):
#    matrixAlpha[0][x] = x  
################################################################################    
#""" Counts the number of letters and numbers in each variable in dataBase"""
################################################################################
#for word in dataBase:
#    for z in range(1, entered,2):
#        for letter in word:
#            found = False
#            for key in alpha:
#                if key==letter:
#                    matrixAlpha[z][alpha[key]] += 1
#                    found = True
#            if found == False:
#                for num in range(10):
#                    if matrixNum[1] == letter:
#                        matrixNum[z][num] += 1
################################################################################
#"""Counts the number of letters and numbers in each variable in inpt"""
################################################################################
#for word in inpt:
#    for z in range(2, entered,2):
#        for letter in word:
#            found = False
#            for key in alpha:
#                if key==letter:
#                    matrixAlpha[z][alpha[key]] += 1
#                    found = True
#            if found == False:
#                for num in range(10):
#                    if matrixNum[1] == letter:
#                        matrixNum[z][num] += 1
################################################################################
#"""Subtracts numbers in matrix rows (database - input), squares them and adds them,
#   then calculates the square root = distance formula"""
################################################################################                
#for ct in range(1,8,2):
#    for x,y in zip(matrixAlpha[ct][:],matrixAlpha[ct+1][:]):
#        distance += (x-y)**2
#    for x,y in zip(matrixNum[ct][:],matrixNum[ct+1][:]):
#        distance += (x-y)**2
#print(distance)
#distance = math.sqrt(distance)
#
####################### 
#"""TEST"""
#
#print(matrixAlpha)                

#------------------------------------------------------------------------------

