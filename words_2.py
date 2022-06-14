
"""
Practice with generator functions, using wordnet.sorted.txt as a bank of categorized words.
"""
__author__ = 'A student in CS 12P, someone@jeff.cis.cabrillo.edu'

from itertools import permutations
import re  # for tokenizing words
from collections.abc import Generator, Iterable
from tabnanny import check  # for type hints

# Consider adding variables here containing info from the WordNet dataset that will be of use in the
# functions below. Use appropriate objects to optimize the speed of your code.

# Building the Dictionary

index = 0
final_dict = {}
set_dict = set()
word_only = set()
for line in open("C:/datasets/wordnet.sorted.txt").readlines():
  segments = line.split('\t')
  words = segments[0].split(';')
  for word in words:
    set_dict.add(word.lower() + ' ' + segments[1].lower())
    word_only.add(word.lower())


def prep_doc(file):
  try:
    y = file.read()
  except:
    y = ' '.join(file)
  finder = re.compile(r"[a-z']+")
  prepared_words = [match[0] for match in re.finditer(finder, y)]
  for word in prepared_words:
    yield word

def adjectives(file) -> Generator[str]:
  """Yields all adjectives present in the text, in the order encountered."""
  user_file = prep_doc(file)
  for word in user_file: 
    x = word, 'adj'
    try:
      if ' '.join(x) in set_dict:
        yield word
    except KeyError:
      print('missed', word)
      pass



def adverbs(file) -> Generator[str]:
  """Yields all adverbs present in the text, in the order encountered."""
  user_file = prep_doc(file)
  for word in user_file: 
    x = word, 'adv'
    try:
      if ' '.join(x) in set_dict:
        yield word
    except KeyError:
      print('missed', word)
      pass

def nouns(file) -> Generator[str]:
  """Yields all nouns present in the text, in the order encountered."""
  user_file = prep_doc(file)
  for word in user_file: 
    x = word, 'noun'
    try:
      if ' '.join(x) in set_dict:
        yield word
    except KeyError:
      pass
  
  

def verbs(file) -> Generator[str]:
  """Yields all verbs present in the text, in the order encountered."""
  user_file = prep_doc(file)
  for word in user_file: 
    x = word, 'verb'
    try:
      if ' '.join(x) in set_dict:
        yield word
    except KeyError:
      print('missed', word)
      pass


def anagrams(word) -> Generator[str]:
  """Yields all arrangements of the characters in `word` that are also words, in any order."""
  x = permutations(word)
  for word in x:
    x = ''.join(word)
    if x in word_only:
      yield x
    
  


if __name__ == '__main__':
  # Some quick tests:
  
  sentences = [
      'the sun did not shine.', 'it was too wet to play.',
      'so we sat in the house all that cold, cold, wet day.'
  ]
  assert list(adjectives(sentences)) == ['wet', 'in', 'all', 'cold', 'cold', 'wet']
  assert list(adverbs(sentences)) == ['not', 'too', 'so', 'in', 'all']
  assert list(nouns(sentences)) == [
      'sun', 'shine', 'it', 'wet', 'play', 'so', 'sat', 'in', 'house', 'cold', 'cold', 'wet', 'day'
  ]
  assert list(verbs(sentences)) == ['sun', 'shine', 'wet', 'play', 'house', 'wet']
  
  
  
  test_file = 'C:/datasets/cat-in-the-hat.txt'
  assert list(adjectives(open(test_file)))[0] == 'wet'
  '''
  print(
    len(set(adverbs(open(test_file))))
  )
  print(
    len(set(verbs(open(test_file))))
  )
  print(
    sorted(anagrams('test'))
  )
  '''
  assert len(set(adjectives(open(test_file)))) == 58
  assert list(adverbs(open(test_file)))[0] == 'not'
  assert len(set(adverbs(open(test_file)))) == 42
  assert list(nouns(open(test_file)))[0] == 'sun'
  assert len(set(nouns(open(test_file)))) == 150
  assert list(verbs(open(test_file)))[0] == 'sun'
  assert len(set(verbs(open(test_file)))) == 106
  assert sorted(anagrams('least')) == [
      'lates', 'least', 'slate', 'stael', 'stale', 'steal', 'stela', 'tesla'
  ]
