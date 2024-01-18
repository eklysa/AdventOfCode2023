# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 09:23:20 2024

@author: sylke
"""

import pandas as pd
import numpy as np
import re

import os
working_directory = os.getcwd()

df = pd.read_excel(working_directory + '/input.xlsx', index_col=0)

Possibilities = pd.DataFrame(index=df.index) 

#make tuples of the colors in the sets
def process_sets(value): 
    if pd.notna(value): 
        return [(int(item.split()[0]), item.split()[1]) for item in value.split(', ')]

# check if sets are possible with total number of stones
# red: 12 , green: 13, blue: 14
#if not, return none
Total = 12 + 13 + 14

def checkTotal(value): 
    if value != None: 
        if len(value) == 3:
            if (value[0][0] + value[1][0] + value[2][0]) <= Total: 
                return value
        if len(value) == 2: 
            if (value[0][0] + value[1][0]) <= Total: 
                return value
        if len(value) == 1: 
            if (value[0][0] <= Total): 
                return value
        else: 
            return 'Not Possible'

# check if the sets have a possible red value
# red: 12
# if not: return not possible
def checkRed(value): 
    if value != None: 
        if value != 'Not Possible': 
            for item in value:
                if any(item[1] == 'red' for item in value):
                    if item[1] == 'red': 
                        if item[0] <= 12: 
                            return value
                        else:
                            print(value)
                            return 'Not Possible'
                else: 
                    return value
        else: 
            return value
def checkGreen(value): 
    if value != None: 
        if value != 'Not Possible': 
            for item in value:
                if any(item[1] == 'green' for item in value):
                    if item[1] == 'green': 
                        if item[0] <= 13: 
                            return value
                        else:
                            print(value)
                            return 'Not Possible'
                else: 
                    return value
        else: 
            return value
def checkBlue(value): 
    if value != None: 
        if value != 'Not Possible': 
            for item in value:
                if any(item[1] == 'blue' for item in value):
                    if item[1] == 'blue': 
                        if item[0] <= 14: 
                            return value
                        else:
                            print(value)
                            return 'Not Possible'
                else: 
                    return value
        else: 
            return value
def main(): 
    for i in range(1,7):
        set_column = 'set_{}'.format(i)
        df[set_column] = df[set_column].apply(process_sets)
        df[set_column] = df[set_column].apply(checkTotal)
        df[set_column] = df[set_column].apply(checkRed)
        df[set_column] = df[set_column].apply(checkGreen)
        df[set_column] = df[set_column].apply(checkBlue)
        
main()
#%%
#drop the rows that contain not possible
df = df[df.set_1 != 'Not Possible']
df = df[df.set_2 != 'Not Possible']
df = df[df.set_3 != 'Not Possible']
df = df[df.set_4 != 'Not Possible']
df = df[df.set_5 != 'Not Possible']
df = df[df.set_6 != 'Not Possible']

game_list = list(df.index.values)

game_numbers = [int(re.search(r'\d+', item).group()) for item in game_list]

print(sum(game_numbers))

