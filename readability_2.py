#!/usr/bin/env python3
"""
Functions implementing readability tests.
See: https://en.wikipedia.org/wiki/Readability#Popular_readability_formulas
"""

__author__ = 'Teo Schnell, taschnell@jeff.cis.cabrillo.edu'

import string
import sys
import math
import re

data = "Testing for a number of Syllables Per Word! Such as the city of aachen. That should be two!"




def filtered_words(data):
  allowed = "abcdefghijklmnopqrstuvwxyz'- "
  filterdata = ''
  for letter in data:
    if allowed.find(letter.lower()) != -1:
      filterdata += (letter)
  return filterdata

def word_count(data):
  filterdata = filtered_words(data)
  word_count = len(filterdata.split())
  return word_count

def character_count(data):
  filterdata = filtered_words(data)
  character_count = len(filterdata.replace(' ',''))
  return character_count


def sentance_count(data):
  data_sentance = data.replace('!','.').replace('?','.')
  sentance_count = 0
  for letter in data_sentance:
    if letter == '.':
      sentance_count += 1
      return sentance_count


def syllables_count(data):
  syllables = open("C:\datasets\syllables.txt")
  dict_syllables = dict()
  for line in syllables:
    dict_syllables.update( {line.replace(';','').replace('\n','') : line.replace('\n','')} )

  filterdata = filtered_words(data)
  syllables_count = 0
  for word in filterdata.split():
    try:
      x = dict_syllables[word].split(';')
      syllables_count += len(x)
    except:
      y = (len(word) / 4)
      syllables_count += math.ceil(y)
  return syllables_count

print(
word_count('this is a test.'),
character_count('this is a test.'),
sentance_count('this is a test.'),
syllables_count('this is a test.')
)

#Old Code
'''
def sentance_count(data):
  data_1 = data.strip('"')
  data_2 = data_1.replace('!',".")
  data_3 = data_2.replace('?',".")
  sentances = data_3.split('.')
  sentance_count = len(sentances)-1
  #print(sentance_count)
  return sentance_count

def characters(data):
  data_4 = re.sub(r'[^a-zA-Z-]',' ',data)
  data_5 = data_4.replace(' ','')
  return len(data_5)

def word_count(data):
  data_4 = re.sub(r'[^a-zA-Z-]'," ",data)
  words = data_4.split()
  word_count = len(words)
  #print(word_count)
  return word_count
'''

# Consider adding several things to the module here, prior to the function definitions:
# 1. import statements for library modules (you will probably want at least the math module).
# 2. Assignment statements preparing variables that will help with syllable counts for words
#    and the list of "easy" words for the Dale-Chall readability score.
# 3. Any "helper" functions that you might find useful. Many of readability tests have several
#    aspects in common, such as needing to calculate the number of words and sentences. Instead of
#    having redundant code in several functions, consider placing that code in an additional
#    function that can be called by the others.


def automated_readability_index(intake) -> float:
  """
  See: https://en.wikipedia.org/wiki/Automated_readability_index
  """
  x = word_count(intake)
  y = sentance_count(intake)
  z = characters(intake)
  try:
    output = 4.71 * (z/x) + 0.5 * (x/y) - 21.43
    output_format = format(output,'.2f')
  except ZeroDivisionError:
    output_format = None
  return output_format


def coleman_liau_index(intake) -> float:
  x = word_count(intake)
  y = sentance_count(intake)
  z = characters(intake)

  L = z/x * 100
  S = y/x * 100

  output = 0.0588 * L - 0.296 * S - 15.8
  formated_ouput = format(output,'.2f')

  return formated_ouput



def dale_chall_readability_score(text: str) -> float:
  """
  See: https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula
  The list of familiar words is available at /srv/datasets/dale-chall_familiar_words.txt
  """
  pass  # TODO


def flesch_kincaid_grade_level(text: str) -> float:
  """
  See: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
  Syllable counts for many words are available in file /srv/datasets/syllables.txt
  """
  pass  # TODO


def gunning_fog_index(text: str) -> float:
  """
  See: https://en.wikipedia.org/wiki/Gunning_fog_index
  Syllable counts for many words are available in file /srv/datasets/syllables.txt
  """
  pass  # TODO


def smog_grade(text: str) -> float:
  """
  See: https://en.wikipedia.org/wiki/SMOG
  Syllable counts for many words are available in file /srv/datasets/syllables.txt
  """
  pass  # TODO

'''
if __name__ == '__main__':
  # Here you might consider adding some tests for your functions, so that you can run this module
  # as a script and determine whether things are working appropriately, e.g.:
  sample_text = open('/srv/datasets/communist-manifesto.txt').read()
  assert abs(coleman_liau_index(sample_text) - 13.45) < .01
'''
