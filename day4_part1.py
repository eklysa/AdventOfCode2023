# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 20:05:13 2024

@author: sylke
"""

import pandas as pd
import numpy as np
import os
working_directory = os.getcwd()

example = pd.read_csv(working_directory + '/example.txt', names=['input'], header=None)
example[['card No', 'No']] = example['input'].str.split(':', expand = True)
example[['Winning No', 'My No']] = example['No'].str.split('|', expand = True)
example.drop(columns={'input', 'No'}, inplace=True)

df = pd.read_csv(working_directory + '/input.txt', names=['input'], header=None)
df[['card No', 'No']] = df['input'].str.split(':', expand = True)
df[['Winning No', 'My No']] = df['No'].str.split('|', expand = True)
df.drop(columns={'input', 'No'}, inplace=True)

winningNo = df['Winning No'].tolist()
myNo = df['My No'].tolist()

def toInt(lotList): 
    Numbers = []
    for lot in lotList: 
        lotNumbers = lot.split()
        numbers = [int(x) for x in lotNumbers]
        Numbers.append(numbers)
    return Numbers
    
def main():
    global winningNumbers
    global myNumbers
    winningNumbers = toInt(winningNo)
    myNumbers = toInt(myNo)
main()

winning = []
for i, row in enumerate(winningNumbers): 
    card = winningNumbers[i]
    mycard = myNumbers[i]
    winninglots = []
    for item in card: 
        if item in mycard: 
            winninglots.append(item)
    winning.append(winninglots)

myPoints = []
for card in winning: 
    x = len(card)
    if x > 1: 
        points = (2**(x-1)) * 1
    if x == 1: 
        points = 1
    if x == 0: 
        points = 0
    myPoints.append(points)

print(np.sum(myPoints))