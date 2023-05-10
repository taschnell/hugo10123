# Wordle Bot!

import requests
from colorama import Fore, Back, Style

URL = "https://jeff.cis.cabrillo.edu/util/wordle"  # Might as well keep this around
USER_ID = "0123456789abcdef0123456789abcdef01234567"  # Change this


def _load_words():
    """Returns the Wordle dictionary file as a set of strings."""
    with open("/srv/datasets/wordle_words.txt") as word_file:
        all_words = set(map(str.rstrip, word_file))
    return all_words


DICTIONARY = _load_words()


class WordlePlayer:
    """I try to win Wordle games!"""

    def __init__(self):
        """Logs into the Wordle service on jeff.cis.cabrillo.edu."""
        self._session = requests.Session()
        response = self._session.post(URL, {"user_id": USER_ID})
        self.lastguesslist = []
        self.word_info = {0: None, 1: None, 2: None, 3: None, 4: None}
        self.yellow_letters = set()
        print(response.json())

    def guess_bot(self, conditions):
        if conditions != None:
            brak1 = str(conditions).index("[")
            brak2 = str(conditions).index("]")
            sorted_condition = str(conditions)[brak1 + 1 : brak2].split(", ")
            print(sorted_condition)
            for index in range(5):
                if sorted_condition[index] == "True":
                    self.word_info.update({index: self.lastguessword[index]})
                    if self.lastguessword[index] in self.yellow_letters:
                        self.yellow_letters.remove(self.lastguessword[index])
                elif sorted_condition[index] == "False":
                    self.yellow_letters.add(self.lastguessword[index])
            print("\t", self.word_info, "\t Yellow Found:", self.yellow_letters)

        for word in DICTIONARY:
            bad_word = False
            for index in range(5):
                if self.word_info[index] == None:
                    continue
                elif self.word_info[index] == word[index]:
                    continue
                else:
                    bad_word = True

            if bad_word:
                continue
            for letter in self.yellow_letters:
                if letter in word:
                    continue
                else:
                    bad_word = True

            if bad_word:
                continue

            if word not in self.lastguesslist:
                self.lastguesslist.append(word)
                self.lastguessword = word
                print(word)
                return word
            else:
                pass

    def play(self):
        """Plays a game from start to finish, attempting to guess the word."""
        # TODO (plays but guess random words!)
        guess = self.guess_bot(None)

        response = self._session.post(URL, {"guess": guess}).json()

        while "word" not in response:
            guess = self.guess_bot(response)
            response = self._session.post(URL, {"guess": guess}).json()

        if all(response["progress"]):
            print("✅")
        else:
            print(f'🔴 ({response["word"]})')


if __name__ == "__main__":
    player = WordlePlayer()
    for index in range(100):
        player.play()
