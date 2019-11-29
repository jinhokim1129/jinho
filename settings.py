"""Settings for the hangman game."""


#  test this game. .

# WORD is the word we will be using for hangman
WORD = 'jinho'
# type in whatever word.

# If the user makes more than MAX_NUM_ERRORS number of incorrect guesses, they
# lose the game.
MAX_NUM_ERRORS = 5

# basic rules for input users
assert WORD.isalpha() 
assert WORD.islower()
assert MAX_NUM_ERRORS >= 1  # Making sure its positive