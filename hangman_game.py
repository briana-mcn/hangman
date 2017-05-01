""" The Game of Hangman """

from hangman_dict import hangmen
from random_words import RandomWords


user_letter_bank = []


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
            valid_letter = valid_input(user_letter)
            if valid_letter == False:
                continue
            else:
                print(user_letter_bank)
                return user_letter
        except:
            break


# asses valid user input
def valid_input(word):

    if not word.isalpha():
        print('Please select a letter')
        return False
    elif len(word) > 1:
        print("Only one letter please.")
        return False
    elif word in user_letter_bank:
        print("Letter already guessed")
        return False
    else:
        user_letter_bank.append(word)
        return True


def game_start():

    # start game header

    print("*********************")
    print("Let's Play Hangman!")
    print("*********************")

    # counter for attempts
    attempts = len(hangmen) - 1

    # counter for printed hangman
    hangmen_count = 1
    print(hangmen[hangmen_count])

    random_word = get_random_word()

    underscr_bank = get_underscr(random_word)
    print(' '.join(underscr_bank))

    # end game header

    # iterate until win or lose
    while '_' in underscr_bank and attempts > 0:

        letter = get_user_selection()
        print("Letter chosen: {}".format(letter))

        # evaluate letter to random word
        if letter not in random_word:
            print('{} not in word!'.format(letter))
            attempts -= 1
            hangmen_count += 1
            print(hangmen[hangmen_count])
        else:
            for i, v in enumerate(random_word):
                if letter in v:
                    print('{} in word!'.format(letter))
                    underscr_bank[i] = letter

            print(hangmen[hangmen_count])

        print(' '.join(underscr_bank))
        print("Attempts Left: {}".format(attempts))

    # evaluate winner or loser
    if attempts == 0:
        print('You lose! The word was: {}'.format(random_word))

    if '_' not in underscr_bank:
        print('You win! The word was: {}'.format(random_word))


if __name__ == "__main__":
    game_start()

