""" The Game of Hangman """

from hangman_dict import hangmen
from random_words import RandomWords

# TODO
# random word into underscores for user display
# get user guessed letter
# store user guessed letters
# evaluate guessed letter to each letter in random word
# if wrong guess subtract attempts
# evaluate at end of attempts or no more underscores in word


# get random word
def get_random_word():
    rw = RandomWords()
    word = rw.random_word()
    if len(word) <= 10:
        return word


def game_start():
    print(get_random_word())


if __name__ == "__main__":
    game_start()

