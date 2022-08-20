import random
from words import words
import string

#computer has to pick a word for us to guess 

#in our list of words we got online we see that there are words that have dashes or spaces so we first want to create a function that will choose a random word that doesnt include one of those features
def get_word(words):
    word = random.choice(words) #here the function will choose a random word from the list
    while '-' in word or ' ' in word: # this while loop will allow the computer to continue choosing a random word if a dash or space is present in the currently random chosen word
        word = random.choice(words)
    return word.upper() #to eliminate issues with using capital or lowercase letters we will return the word using only uppercase letters


def hangman():
    word = get_word(words)
    word_letters = set(word) # these are the letters that are in the word that was chosen
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # these are the letters that the user have guessed so far
    user_letter = input('Guess a letter').upper()
    
    #get user input
    while len(word_letters) > 0:
        print('You have used these letters:', ' '.join(used_letters))
        
        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper() 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print(' you have already used that character. please try again.')
        else:
            print('invalid character. please try again.')


user_input = input('Type something: ')
print(user_input)