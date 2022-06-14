#!/usr/bin/env python3
'''
Program which sorts throught homoglyphs and outputs possible Scrabble solutions.
'''
import sys
from collections import OrderedDict

# may need to recode homeoglyphes with homoglyph key for normlal charcater to increce speed


sorter_input = open("C:\datasets\homoglyphs_curated.txt", encoding='utf8')

sorter = {}
input = sys.stdin.read()
output = []

for line in sorter_input:
    line_1 = line.strip('\n')
    sorter.update({line_1[0] : line_1[1:]})

normal = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for letter in input:
    if normal.find(letter) != -1:
        output.append(letter)
    elif letter == ' ':
        output.append(letter)
    else:
        for valid in normal:
            if letter in sorter[valid]:
                output.append(valid)


text = (''.join(output))

words = open('C:\datasets\scrabble-hybrid').readlines()

set_sorter = set(words)

start_letter = 0
lenght = 1
final_out = []

for letter in text:
    lenght = 1
    while lenght <= 15:
        test = text[start_letter:(lenght+start_letter)].upper()
        if (test + '\n') in set_sorter:
            final_out.append(test)
        lenght += 1
    start_letter += 1


final_output = list(OrderedDict.fromkeys(final_out))

for x in final_output:
    print(x)