""" The Game of Hangman """

from hangman_dict import hangmen
from random_words import RandomWords


user_letter_bank = []


# TODO
# evaluate guessed letter to each letter in random word
# if wrong guess subtract attempts
# evaluate at end of attempts or no more underscores in word


# get random word
def get_random_word():

    rw = RandomWords()
    word = rw.random_word()
    if len(word) <= 10:
        return word
    else:
        return get_random_word()


# random word into underscores for user display
def get_underscr(ran_word):

    under_scr = ['_' for letter in ran_word]
    return under_scr


# get user guessed letter
def get_user_selection():
    while True:
        try:
            user_letter = input("Choose a letter: ").lower()
            valid_input(user_letter)
            return user_letter
        except:
            break


# asses valid user input
def valid_input(word):

    if not word.isalpha():
        print('No')
    elif len(word) > 1:
        print("Only one letter please.")
    elif word in user_letter_bank:
        print("Letter already guessed")
    else:
        user_letter_bank.append(word)

    print(user_letter_bank)


def game_start():

    random_word = get_random_word()
    print(random_word)
    underscr_bank = get_underscr(random_word)
    print(' '.join(underscr_bank))

    while True:
        letter = get_user_selection()
        if letter in random_word:
            print("yes")
            continue
        else:
            break


if __name__ == "__main__":
    game_start()

