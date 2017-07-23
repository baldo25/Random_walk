'''
This is junk file any new code developed, should be developed here and then implemented here
This file should not be imported to other files
It includes all the test methods
'''

import random
import variables as var
import csv

dataset = []
for key in range(200):
    dataset.append(random.choice([-1, 0, 1]))


def csvcreate():
    with open('dataset.csv', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dataset)


# csvcreate()
var.p = int(input("Enter the value of Price P"))

if var.p == var.pp1:
    print('sell a%')
    var.p = var.p + var.p * var.a
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
    # make loop                   #have to make a new function so that it can jump back
elif var.p == var.ps1:
    print('sell g%')
    var.p = var.p - var.p * var.g
    print(var.p)
elif var.p == var.ps2:
    print('sell h%')
    var.p = var.p + var.p * var.h
    print(var.p)
    # call loop again


# inputs
# @staticmethod
def input(self):
    return
