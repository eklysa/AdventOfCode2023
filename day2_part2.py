# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 09:18:36 2024

@author: sylke
"""

import pandas as pd
import numpy as np
import re

import os
working_directory = os.getcwd()

df = pd.read_excel(working_directory + '/input.xlsx', index_col=0)

MinimumRed = pd.DataFrame(index=df.index) 
MinimumGreen = pd.DataFrame(index=df.index) 
MinimumBlue = pd.DataFrame(index=df.index) 
Red = []
Green = []
Blue = []

#make tuples of the colors in the sets
def process_sets(value): 
    if pd.notna(value): 
        return [(int(item.split()[0]), item.split()[1]) for item in value.split(', ')]

#there are no impossible games
#in each game, find the highest number for each color
#multiply the minimum required number of cubes for each color
# add these powers together
def findMinimumRed(value): 
    if value != None: 
        for item in value: 
            if any(item[1] == 'red' for item in value):
                if item[1] == 'red':
                    return item[0]
def findMinimumGreen(value): 
    if value != None: 
        for item in value: 
            if any(item[1] == 'green' for item in value): 
                if item[1] == 'green': 
                    return item[0]
def findMinimumBlue(value):
    if value != None: 
        for item in value: 
            if any(item[1] == 'blue' for item in value): 
                if item[1] == 'blue': 
                    return item[0]

def FindNoOfCubesRed(value): 
    Red.append(int(value.max()))
def FindNoOfCubesGreen(value):
    Green.append(int(value.max()))
def FindNoOfCubesBlue(value): 
    Blue.append(int(value.max()))
    
def main(): 
    for i in range(1,7): 
        set_column = 'set_{}'.format(i)
        df[set_column] = df[set_column].apply(process_sets)
        MinimumRed[set_column] = df[set_column].apply(findMinimumRed)
        MinimumGreen[set_column] = df[set_column].apply(findMinimumGreen)
        MinimumBlue[set_column] = df[set_column].apply(findMinimumBlue)
    MinimumRed.apply(FindNoOfCubesRed, axis=1)
    MinimumGreen.apply(FindNoOfCubesGreen, axis=1) 
    MinimumBlue.apply(FindNoOfCubesBlue, axis=1)
    
main()
#%%
print(Red[0], Green[0], Blue[0])
print(Red[0] * Green[0] * Blue[0])

Powers = np.array(Red) * np.array(Green) * np.array(Blue)

print(sum(Powers))