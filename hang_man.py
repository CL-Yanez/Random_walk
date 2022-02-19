import random
import string
from getwords import get_word


def random_valid_word(list_of_words):
    '''Takes a function which return a list of word and then validate it'''

    word = random.choice(list_of_words()) #Radomly choses a word

    while 'ñ' in word:
        word = random.choice(get_word())

    return word.upper()

palabra = random_valid_word(get_word)
print(palabra)

