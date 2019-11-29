"""The script that runs the game of hangman"""


# Adding imports that are on same file.
from settings import *
from hangman import *


def main():
    curr_num_error = 0
    past_guesses = []
    is_user_won = False

    # Repeating until a user wins or loses
    while not is_user_won and curr_num_error <= MAX_NUM_ERRORS:
        # the current status
        print('Word: ' + unclear_word(WORD, past_guesses))
        print('Number of bad guesses: ' +
              str(curr_num_error) +
              " out of " +
              str(MAX_NUM_ERRORS))
        print('Guesses: ' + format_guesses(past_guesses))

        # Ask a guess letter
        guess = get_guess(past_guesses)

        # Is it good guess?
        if is_guess_good(WORD, guess):
            print(guess + " is in the word")
        else:
            print(guess + " is not in the word")
            curr_num_error = curr_num_error + 1

        # A user won?
        is_user_won = is_word_guessed(WORD, past_guesses)

    # A user won or lost?
    if is_user_won:
        print("Congratulations! It took you " +
              str(curr_num_error) + " incorrect guesses to guess the word")
    else:
        print("Sorry, you failed to guess the word after " +
              str(MAX_NUM_ERRORS) + " incorrect guesses")

    # the answer.
    print("The word was " + str(WORD))

if __name__ == '__main__':
    main()  # 
