#!/usr/bin/env python3
"""
Functions implementing readability tests.
See: https://en.wikipedia.org/wiki/Readability#Popular_readability_formulas
"""

__author__ = 'Teo Schnell, taschnell@jeff.cis.cabrillo.edu'

__name__ = '__main__'

from cmath import sqrt
import math

syllables = open("C:\datasets\syllables.txt")

def filtered_words(data):
  allowed = "abcdefghijklmnopqrstuvwxyz'-"
  filterdata = []
  filterword = ''
  data_1 = data.lower()
  data_2 = data_1.replace('\n',' ').split()
  for word in data_2:
    filterword = ''
    for letter in word:
        if allowed.find(letter.lower()) != -1:
            filterword += (letter.lower())
        
    filterdata.append(filterword)

  x = ''

  for word in filterdata:
      x += word + ' '
  y = x[:-1]
  
  return y


def word_count(data):
  filterdata = filtered_words(data)
    
  word_count = len(filterdata.split())
  return word_count

def character_count(data):
  filterdata = filtered_words(data)
  character_count = len(filterdata.replace(' ',''))
  return character_count

def sentance_count(data):
  data_sentance = data.replace('\n',' ').replace("'",'').replace('"','')

  test = data_sentance.split()
  
  sentance_count = 0

  for sentance in test:
    if sentance.endswith('.'):
      sentance_count += 1
    elif sentance.endswith('?'):
      sentance_count += 1
    elif sentance.endswith('!'):
      sentance_count += 1
  
  return sentance_count

def syllables_count(data):
  
  complex_words = 0
  dict_syllables = dict()
  for line in syllables:
    dict_syllables.update( {line.replace(';','').replace('\n','') : line.replace('\n','')} )
  filterdata = filtered_words(data)
  syllables_count = 0
  for word in filterdata.split():
    try:
      x = dict_syllables[word].split(';')
      
      syllables_count += len(x)
      if len(x) > 3 or len(x) == 3:
        complex_words += 1
    except:
      x = (len(word) / 4)
      syllables_count += math.ceil(x)
      if x > 3 or x == 3:
        complex_words +=1 
    # print(x,word)
  return syllables_count

def complex_word(data):
  
  complex_words = 0
  dict_syllables = dict()
  for line in syllables:
    dict_syllables.update( {line.replace(';','').replace('\n','') : line.replace('\n','')} )
  filterdata = filtered_words(data)
  syllables_count = 0
  for word in filterdata.split():
    try:
      x = dict_syllables[word].split(';')
      syllables_count += len(x)
      if len(x) > 3 or len(x) == 3:
        complex_words += 1
    except:
      x = (len(word) / 4)
      syllables_count += math.ceil(x)
      
      if math.ceil(x) > 3 or math.ceil(x) == 3:
        complex_words +=1 

  return complex_words


def automated_readability_index(intake) -> float:
  """
  See: https://en.wikipedia.org/wiki/Automated_readability_index
  """
  x = word_count(intake)
  y = sentance_count(intake)
  z = character_count(intake)
  
  # print(z,x,y)
  try:
    output = 4.71 * (z/x) + 0.5 * (x/y) - 21.43
    output_format = format(output,'.2f')
  except ZeroDivisionError:
    output_format = None
  return float(output_format)


def coleman_liau_index(intake) -> float:
  x = word_count(intake)
  y = sentance_count(intake)
  z = character_count(intake)
  # print(x,y)
  L = z/x * 100
  S = y/x * 100
  try:
    output = 0.0588 * L - 0.296 * S - 15.8
    formated_ouput = format(output,'.2f')
  except ZeroDivisionError:
    formated_ouput = None

  return float(formated_ouput)



def dale_chall_readability_score(text: str) -> float:
  """
  See: https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula
  The list of familiar words is available at /srv/datasets/dale-chall_familiar_words.txt
  """
  pass  # TODO


def flesch_kincaid_grade_level(data) -> float:
  """
  See: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
  Syllable counts for many words are available in file /srv/datasets/syllables.txt
  """

  words = word_count(data)
  sentances = sentance_count(data)
  syl = syllables_count(data)
  try:
    x =  0.39 * (words/sentances) + 11.8 * (syl/words) - 15.59 
    y = format(x,'.2f')
    output = float(y)
  except ZeroDivisionError:
      output = None

  return output


def gunning_fog_index(data) -> float:
  """
  See: https://en.wikipedia.org/wiki/Gunning_fog_index
  Syllable counts for many words are available in file /srv/datasets/syllables.txt
  """
  x = word_count(data)
  y = sentance_count(data)
  z = complex_word(data)

  try:
    answer = 0.4 * ((x/y) + 100 * (z/x))
  # print(x,y,z)
    output = format(answer,'.2f')
    foutput = float(output)
  except ZeroDivisionError:
      foutput = None
  
  return foutput

def smog_grade(data) -> float:
  """
  See: https://en.wikipedia.org/wiki/SMOG
  Syllable counts for many words are available in file /srv/datasets/syllables.txt
  """
  x = complex_word(data)
  y = sentance_count(data)

  try:
    grade = 1.0430 * sqrt(x * 30 / y) + 3.1291
    output = format(grade, '.2f')
    x = float(output[:-6])
  except ZeroDivisionError:
    x = None
  return x

if __name__ == '__main__':
  # Here you might consider adding some tests for your functions, so that you can run this module
  # as a script and de"C:\datasets\communist-manifesto.txt"termine whether things are working appropriately, e.g.:
  sample_text = open("C:\datasets\communist-manifesto.txt").read()
  print(
    automated_readability_index(sample_text)
  )
