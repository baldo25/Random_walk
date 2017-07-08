# Project- Random Walk Test
# Pycharm Project
# Python 3.6.1
# Author- @sahil
# This is the main file in which main code will be executed

import variables            # Importing variables
import random
print(variables.test)       # Testing statement will be removed further


def data_gen():
    dataset =[]
    for key in range(200):
        dataset.append(random.choice([-1,0,1]))

    return dataset


print(data_gen())