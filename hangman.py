# -*- coding: utf-8 -*-
"""
Hangman Game
Created on Sat Jul 24 13:54:24 2021

@author: RanCalifa
"""
# importing all relevant modules
import random


# declearation of all functions used by the main section

def check_win(secret_word, old_letters_guessed):
    num_of_coorect_letters = 0
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            num_of_coorect_letters += 1
    if num_of_coorect_letters == len(secret_word):
        return(True)
    else:
        return(False) 
    
    
def show_hidden_word(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter in old_letters_guessed:
            print(letter + ' ',end = '')
        else:
            print('_ ',end = '')                


def check_valid_input(letter_guessed, old_letters_guessed):
    """cheacking input letter validation
    varibles: letter_guessed (str)
    return: Ture = valid, False = notValid"""
    
    if (len(letter_guessed) == 1) and (letter_guessed.isalpha() and (letter_guessed not in old_letters_guessed) ):
        return(True)
    else:
        return(False)
        
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if (check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed += letter_guessed
        return(old_letters_guessed,True)
    else:
        print('X')
        print ('->'.join((str(x) for x in old_letters_guessed)))
        return(old_letters_guessed,False)


def choose_word(file_path, index):
    file1 = open(file_path,'r')
    file_content = file1.read()
    list_of_words = file_content.split(' ')
    num_of_words = len(set(list_of_words))
    index = int(index) % len(list_of_words) -1
    selected_word = list_of_words[index]
    file1.close()
    return(selected_word, num_of_words)

def welcome_screen():
    # Welcome 
    print ('Welcome to the game Hangman')

    # print game logo

    print(""" 
      
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/
      """)




def main():
    pass    


if __name__ == "__main__" :
    main()    
