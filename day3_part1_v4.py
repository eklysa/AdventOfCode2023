# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:38:03 2024

@author: sylke
"""
import pandas as pd
import numpy as np
import os
working_directory = os.getcwd()

with open(working_directory + '/input.txt', 'r') as file: 
    schematic = file.readlines()
example = ['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', 
           '......755.', '...$.*....', '.664.598..']

#%%
matrix = schematic
#symbol if it is not a digit and not a numeric character
symbolLocations = []
digitLocations = []
def findSymbolsAndDigits(A): 
    for i, string in enumerate(A):
        symbols_in_string = []
        digits_in_string = []
        for j, char in enumerate(string): 
            if char.isnumeric() == False and char != '.' and char != '\n': 
                symbols_in_string.append([i,j])
            if char.isnumeric(): 
                digits_in_string.append([i,j])
        symbolLocations.append(symbols_in_string)
        digitLocations.append(digits_in_string)

                          
findSymbolsAndDigits(matrix)
adjacent_digits = []
for symbolRow in symbolLocations: 
    for symbol in symbolRow:
        x = symbol[0]
        y = symbol[1]
        adjacent = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y -1], [x, y + 1], [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]
        for digitRow in digitLocations:
            for digit in digitRow:
                digit_x = digit[0]
                digit_y = digit[1]
                left = [digit_x, digit_y - 1]
                left_left = [digit_x, digit_y -2]
                right = [digit_x, digit_y + 1]
                right_right = [digit_x, digit_y + 2]
                number = []
                if digit in adjacent:
                    if left in digitRow and left_left in digitRow:
                        if [left_left, left, digit] not in adjacent_digits:
                            number = [left_left, left, digit]
                    elif right in digitRow and right_right in digitRow: 
                        if [digit, right, right_right] not in adjacent_digits:
                            number = [digit, right, right_right]
                    elif left in digitRow and right in digitRow: 
                        if [left, digit, right] not in adjacent_digits:
                            number = [left, digit, right]
                    elif left in digitRow and left_left not in digitRow:
                        if [left, digit] not in adjacent_digits:
                            number = [left, digit]
                    elif right in digitRow and right_right not in digitRow: 
                        if [digit, right] not in adjacent_digits:
                            number = [digit, right]
                    elif left not in digitRow and right not in digitRow: 
                        if [digit] not in adjacent_digits:
                            number = [digit]
                    adjacent_digits.append(number)

sum_digits = []
for number in adjacent_digits: 
    digits = []
    for location in number: 
        digit = matrix[location[0]][location[1]]
        digits.append(digit)
    sum_digits.append(digits)

# number_list = [[int(x) for x in sublist] for sublist in sum_digits]
number_list = [int(''.join(sublist)) for sublist in sum_digits if sublist]

        
print(np.sum(number_list))  

        
