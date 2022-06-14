"""
Practice with generator functions, using wordnet.sorted.txt as a bank of categorized words.
"""
__author__ = "A student in CS 12P, someone@jeff.cis.cabrillo.edu"

import re  # for tokenizing words
from collections.abc import Generator, Iterable  # for type hints
from itertools import permutations

# Consider adding variables here containing info from the WordNet dataset that will be of use in the
# functions below. Use appropriate objects to optimize the speed of your code.

set_dict = set()
word_only = set()
for line in open("C:/datasets/wordnet.sorted.txt").readlines():
    segments = line.split("\t")
    words2 = segments[0].split(";")
    for word1 in words2:
        word_only.add(word1.lower())
        set_dict.add(word1.lower() + " " + segments[1].lower())


def prep_dock(text: Iterable[str]):
    merged_words = "".join(text)
    for match in re.finditer(re.compile(r"[a-z']+"), merged_words.strip("\n").lower()):
        yield match[0]


def adjectives(text: Iterable[str]) -> Generator[str]:
    """Yields all adjectives present in the text, in the order encountered."""
    user_file = prep_dock(text)
    for word in user_file:
        x = word, "adj"
        try:
            if " ".join(x) in set_dict:
                yield word
        except KeyError:
            pass


def adverbs(text: Iterable[str]) -> Generator[str]:
    """Yields all adverbs present in the text, in the order encountered."""
    user_file = prep_dock(text)
    for word in user_file:
        x = word, "adv"
        try:
            if " ".join(x) in set_dict:
                yield word
        except KeyError:
            pass


def nouns(text: Iterable[str]) -> Generator[str]:
    """Yields all nouns present in the text, in the order encountered."""
    user_file = prep_dock(text)
    for word in user_file:
        x = word, "noun"
        try:
            if " ".join(x) in set_dict:
                yield word
        except KeyError:
            pass


def verbs(text: Iterable[str]) -> Generator[str]:
    """Yields all verbs present in the text, in the order encountered."""
    user_file = prep_dock(text)
    for word in user_file:
        x = word, "verb"
        try:
            if " ".join(x) in set_dict:
                yield word
        except KeyError:
            pass


def anagrams(words: str) -> Generator[str]:
    """Yields all unique arrangements of the characters in `word` that are words, in any order."""
    for word in permutations(words):
        if "".join(word) in word_only:
            yield "".join(word)


if __name__ == "__main__":
    # Some quick tests:

    sentences = [
        "the sun did not shine.",
        "it was too wet to play.",
        "so we sat in the house all that cold, cold, wet day.",
    ]

    assert list(adjectives(sentences)) == ["wet", "in", "all", "cold", "cold", "wet"]
    assert list(adverbs(sentences)) == ["not", "too", "so", "in", "all"]
    assert list(nouns(sentences)) == [
        "sun",
        "shine",
        "it",
        "wet",
        "play",
        "so",
        "sat",
        "in",
        "house",
        "cold",
        "cold",
        "wet",
        "day",
    ]
    assert list(verbs(sentences)) == ["sun", "shine", "wet", "play", "house", "wet"]

    test_file = "C:/datasets/cat-in-the-hat.txt"
    assert list(adjectives(open(test_file)))[0] == "wet"
    assert len(set(adjectives(open(test_file)))) == 58
    assert list(adverbs(open(test_file)))[0] == "not"
    assert len(set(adverbs(open(test_file)))) == 42
    assert list(nouns(open(test_file)))[0] == "sun"
    assert len(set(nouns(open(test_file)))) == 150
    assert list(verbs(open(test_file)))[0] == "sun"
    assert len(set(verbs(open(test_file)))) == 106
    assert sorted(anagrams("least")) == [
        "lates",
        "least",
        "slate",
        "stael",
        "stale",
        "steal",
        "stela",
        "tesla",
    ]