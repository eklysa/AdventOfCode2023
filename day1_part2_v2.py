# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 18:02:40 2024

@author: sylke
"""

import pandas as pd
import re
import numpy as np

import os
working_directory = os.getcwd()

url = working_directory + '/input_day1.csv'

day1_input = pd.read_csv(url, names=['value'], header=None)
day1_input['value'] = day1_input['value'].astype('string')

example1 = pd.DataFrame(['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet'], columns=['value'])
example = pd.DataFrame(['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four',
                        '4nineeightseven2', 'zoneight234', '7pqrstsixteen'], columns=['value'])

replacements = { 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9',
                 '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9' : '9'}
length = []
for i in range(len(day1_input)): 
    length.append(len(day1_input['value'][i]))
maxLength = max(length)
print('max-length: ', max(length))
#%%
def findIntegers(row):
    myRow = row['value']
    integers = []
    for start in range(len(myRow)): 
        for end in range(start + 1, min(start + 6, len(myRow) + 1)):
            substring = myRow[start:end]
            for key, value in replacements.items(): 
                if key == substring: 
                    integers.append(value)                    
    # integers = re.findall('\d', row['value'])
    integers = list(map(str, integers))
    integers = ''.join(integers)
    return integers

def selectFirst(row): 
    first = row['integers'][0]
    return first

def selectLast(row): 
    last = row['integers'][-1]
    return last

def calibrationValue(row): 
    return int(row['first'] + row['last'])

def main(): 
    # example['integers']= example.apply(findIntegers, axis=1)
    # example['first'] = example.apply(selectFirst, axis=1)
    # example['last'] = example.apply(selectLast, axis=1)
    # example['sum'] = example.apply(calibrationValue, axis=1)
    day1_input['integers']= day1_input.apply(findIntegers, axis=1)
    day1_input['first'] = day1_input.apply(selectFirst, axis=1)
    day1_input['last'] = day1_input.apply(selectLast, axis=1)
    day1_input['sum'] = day1_input.apply(calibrationValue, axis=1)

main()

print(np.sum(day1_input['sum']))