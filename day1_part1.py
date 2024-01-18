# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:59:18 2024

@author: sylke
"""

import pandas as pd
import re

import os
working_directory = os.getcwd()

url = working_directory + '/input_day1.csv'

day1_input = pd.read_csv(url, names=['value'], header=None)
day1_input['value'] = day1_input['value'].astype('string')

def find_first_integer(row):
    # print(len(row['value']))
    integers = re.findall('\d', row['value'])
    print(integers)
    return integers[0]

def find_last_integer(row):
    # print(len(row['value']))
    integers = re.findall('\d', row['value'])
    print(integers)
    return integers[-1]

def sum_integers(row): 
    return int(row['first'] + row['last'])

def main():
    day1_input['first'] = day1_input.apply(find_first_integer, axis=1)
    day1_input['last'] = day1_input.apply(find_last_integer, axis=1)
    day1_input['sum'] = day1_input.apply(sum_integers, axis=1)
    
main()

print(sum(day1_input['sum']))