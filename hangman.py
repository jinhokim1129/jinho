"""Some functions useful for the hangman game. Organized functions
Jinho Kim 1001360261
"""


def unclear_word(word, past_guesses):
    """ Replaces word with '_' for guessed letters.

    What I want:
        word: a str representing the word in question
        past_guesses: a list consisting of guessed letters

    What I want return:
        a str identical to word but where the characters which have
        been guessed are unmodified and the non-guessed characters have
        been replaced with underscores.

    >>>example of the word: obfuscated_word('headphones', ['e', 'd'])
    '_e_d____e_'
    """
    revealed = ""
    for each_char in word:
        # if each_char is found in past_guesses, then just add
        # otherwise, add an underscore
        if each_char in past_guesses:
            revealed = revealed + each_char
        else:
            revealed = revealed + "_"
    return revealed


def get_guess(past_guesses):
    """ Asks a user what to guess.

    Asks a letter from the user as input in a lowercase which
    letter must be one alphabetic char and has not be guessed.
    Otherwise, it prompts the user repeatedly.

    What I want:
        past_guesses: a list consisting of guessed letters.

    What I want return:
        A valid guess letter from a user
    """
    to_ask = 'Guess a letter: '
    user_input = input(to_ask)
    user_input = user_input.lower()

    # Keep asking the user if the input is not 1 alphabetic long OR
    # it is already one of guessed letters
    while not (len(user_input) == 1 and user_input.isalpha()) \
            or user_input in past_guesses:
        print("You need to enter one alphabetic character " +
              "which you haven\'t already guessed. Try again")
        user_input = input(to_ask)
        user_input = user_input.lower()

    # Append the guess
    past_guesses.append(user_input)

    return user_input


def format_guesses(past_guesses):
    """ Converts each of guess letters to a single string.

    Formats each letters in past_guesses to a single string
    consisting of past_guesses with a space between them.

    What I want:
        past_guesses: a list consisting of guessed letters.

    What I want return:
        The formatted single string

    >>> format_guesses(['a', 'b', 'c'])
    'a b c'
    """
    string = ""
    count = 0
    for each_char in past_guesses:
        # if first time, do not add a space
        if count == 0:
            string = each_char
        # not first time, then append a space and each char
        else:
            string = string + " " + each_char

        count = count + 1

    return string


def is_guess_good(word, guess):
    """ is guess good?

    Checks if guess is part of word.

    What I want:
        word: a str representing the word in question.
        guess: a single str which was most recently guessed by the user.

    What I want return:
        If the guess is in the word, returns True, else False.

    >>> is_guess_good('toe', 'e')
    True
    >>> is_guess_good('toe', 'a')
    False
    """
    guess_found = False

    # is the guess in the word?
    if guess in word:
        guess_found = True
    else:
        guess_found = False

    return guess_found


def is_word_guessed(word, past_guesses):
    """ Is word fully guessed?

    Checks if word is fully guessed using past_guesses.

    What I want:
        word: a str representing the word in question.
        past_guesses: a list consisting of guessed letters.

    What I want return:
        if word is fully guessed, return True. Otherwise, False.

    >>> is_word_guessed('toe', ['e', 't', 'a', 'o',])
    True
    >>> is_word_guessed('toe', ['e', 't', 'a'])
    False
    """

    revealed = unclear_word(word, past_guesses)
    is_fully_guessed = True

    # if there is any understore, it means it is not fully guessed
    if '_' in revealed:
        is_fully_guessed = False
    else:
        is_fully_guessed = True

    return is_fully_guessed
