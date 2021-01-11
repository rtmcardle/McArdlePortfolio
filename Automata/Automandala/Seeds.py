###############################################################
####	Automandala Seeds
####	Ryan McArdle
####	Original: Dec.  2018
####	Refresh: Dec.  2020
####	
####	Fuctions defined to seed the initial grid for the 
####    Automandala class.
####
###############################################################


import matplotlib.pyplot as plt
import numpy as np


def seed25(matrix,mandala):
    base=mandala.center[0]-2
    print(f'base:{base}')
    for y in range(5):
        for x in range(5):
            if matrix[x][y]==1:
                mandala.grid[base+x,base+y]=mandala.on
                print(f'on:{mandala.grid[base+x,base+y]}')
    print("Seed: ")
    for z in range(len(matrix)):
        print(matrix[z])

def seed9(matrix,mandala):
    base=mandala.center[0]-1
    for y in range(3):
        for x in range(3):
            if matrix[x][y]==1:
                mandala.grid[base+x,base+y]=mandala.on
    print("Seed: ")
    for z in range(len(matrix)):
        print(matrix[z])


def cent():
    matrix=[[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    return matrix
def root():
    matrix=[[0,0,0,0,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,0,0,0,0]]
    return matrix
def x():
    matrix=[[1,0,0,0,1],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,1,0,1,0],
            [1,0,0,0,1]]
    return matrix
def cross():
    matrix=[[0,0,1,0,0],
            [0,0,1,0,0],
            [1,1,1,1,1],
            [0,0,1,0,0],
            [0,0,1,0,0]]
    return matrix
def numseed9(number):
    string=format(number, '09b')
    matrix=[[int(string[0]),int(string[1]),int(string[2])],
            [int(string[3]),int(string[4]),int(string[5])],
            [int(string[6]),int(string[7]),int(string[8])]]
    return matrix
def numseed25(number):
    string=format(number, '025b')
    matrix=[[int(string[0]),int(string[1]),int(string[2]),int(string[3]),int(string[4])],
            [int(string[5]),int(string[6]),int(string[7]),int(string[8]),int(string[9])],
            [int(string[10]),int(string[11]),int(string[12]),int(string[13]),int(string[14])],
            [int(string[15]),int(string[16]),int(string[17]),int(string[18]),int(string[19])],
            [int(string[20]),int(string[21]),int(string[22]),int(string[23]),int(string[24])]]
    return matrix
def randseed():
    #enter num btw 0-33554431
    random=np.random.randint(0,33554432)
    print(random)
    string=format(random, '025b')
    matrix=[[int(string[0]),int(string[1]),int(string[2]),int(string[3]),int(string[4])],
            [int(string[5]),int(string[6]),int(string[7]),int(string[8]),int(string[9])],
            [int(string[10]),int(string[11]),int(string[12]),int(string[13]),int(string[14])],
            [int(string[15]),int(string[16]),int(string[17]),int(string[18]),int(string[19])],
            [int(string[20]),int(string[21]),int(string[22]),int(string[23]),int(string[24])]]
    return matrix
def manual():
    matrix=[[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    return matrix
