# Project- Random Walk Test
# Pycharm Project
# Python 3.6.1
# Author- @sahil, @bal
# This is the main file in which main code will be executed

import variables  # Importing variables
import random
import csv


# This is the data generating segment
def data():
    # Function to generate random numbers
    dataset = []
    for key in range(200):
        dataset.append(random.choice([-1, 0, 1]))

    return dataset


def new_data():
    """Function to write the generated numbers to a csv file
    Each time the numbers generated will be random and gets updated"""
    with open('dataset.csv', 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data())


new_data()
