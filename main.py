# Project- Random Walk Test
# Pycharm Project
# Python 3.6.1
# Author- @sahil, @bal
# This is the main file in which main code will be executed

import variables as var  # Importing variables
import random
import csv



# Data Generating segment
dataset = []
def data():
    # Function to generate random numbers

    for key in range(200):
        dataset.append(random.choice([-1, 0, 1]))

    return dataset





def new_data():
    """Function to write the generated numbers to a csv file
    Each time the numbers generated will be random and gets updated"""
    with open('dataset.csv', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data())


# new_data()             # to be called only to genrate new dataset








# taking values here when we get exit positions
var.p = float(input('Enter value of P'))
var.N = int(input("Enter the Value of N"))
var.position = 0
var.l = int(input('Enter the loop number L'))
# Will join the dataset here





# loop condition here
'''i = 0
while i < var.l:
    i = i + 1'''



# If conditions          #correct defination of var.p should be appended in the following conditions
if var.p == var.pp1:
    print('sell a%')
    var.p = var.p + var.p * var.a  # This is incorrect BD to correct.
    print(var.p)
elif var.p == var.pp2:
    print('sell b%')
    var.p = var.p + var.p * var.b
    print(var.p)
elif var.p == var.pp3:
    print('sell c%')
    var.p = var.p + var.p * var.c
    print(var.p)
elif var.p == var.pp4:
    print('sell d%')
    var.p = var.p + var.p * var.d
    print(var.p)
    var.p = int(input('Enter value of P'))
    var.N = int(input("Enter the Value of N"))
    var.position=0                     # exit position take input again
elif var.p == var.ps1:
    print('sell g%')
    var.p = var.p - var.p * var.g
    print(var.p)
elif var.p == var.ps2:
    print('sell h%')
    var.p = var.p + var.p * var.h
    print(var.p)
    var.p = int(input('Enter value of P'))
    var.N = int(input("Enter the Value of N"))
    var.position = 0                          # exit position take input again
elif var.p == var.pe and var.position < var.N:  # This condition is not same as others
    var.N = int(input("Enter the Value of N"))
