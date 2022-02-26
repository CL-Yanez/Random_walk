import random
import string
from getwords import get_word


def random_valid_word(list_of_words):
    '''Takes a function which return a list of word and then validate it'''

    word = random.choice(list_of_words()) #Radomly choses a word

    while 'ñ' in word:
        word = random.choice(get_word())

    return word.upper()


# print(palabra)

def hangman():
    palabra = random_valid_word(get_word)
    word_check = set(palabra) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lifes = 6 # max number of attempts allowed
    
    while len(word_check) > 0 and lifes > 0:
        
        print(f'YOU HAVE {lifes} TURNS LEFT\nUsed letters: ',' '.join(used_letters))
        print('----------------------------------------------------------')
        
        guessin_progress = [letters if letters in used_letters else '-' for letters in palabra] # a loop which validate every single single letter in the hidden word and return just the letters that we guessed right.
        print('current progress: ', ' '.join(guessin_progress))

        user_letter = input('Guess letter ----> ').upper() #user input guess
        print('\n')
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_check:
                word_check.remove(user_letter)
            else:
                lifes -= 1 # subtract one attempt until there is nothing left.
                print(f'{user_letter} is not in the word, try hard!')
        
        elif user_letter in used_letters:
            print(f'\t\t\t\tYou have already used this one: "{user_letter}". Try a different one!!!')
        else:
            print('invalid character')
    
    if lifes != 0:
        guessin_progress = [letters if letters in used_letters else '-' for letters in palabra]
        print('\n\t\t\t\tYOU WIN Congratulations!!! You got the word: ', ' '.join(guessin_progress))
    else:
        print('\n\t\t\t\tYOU LOSE :( the word was: ', palabra)
        
play = hangman()
  

