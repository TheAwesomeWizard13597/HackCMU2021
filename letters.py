# letters.py

import random
import copy

dictFile = open('dictionary.txt')
dictContent = dictFile.read()
dict_list = [list(x.lower()) for x in dictContent.split('\n')]

def valid_helper(input_list, word):
    input_list_ = copy.deepcopy(input_list)
    for letter in word:
        if letter in input_list_:
            # print(letter)
            # print(input_list)
            input_list_.remove(letter)
        else:
            return False
    return True

def valid_words(letters):
    """
    Input: List of letters
    Output: List of words that can be made using letters"""
    return ["".join(x) for x in dict_list if valid_helper(letters, x)]

right_side = "yhnmjuiklop"
left_side = "asdfgvtrewqcxzb"

def classify_letter(l, correct_side):
    if l in right_side and correct_side == 'r':
        return True
    elif l in left_side and correct_side == 'l':
        return True
    else:
        return False

def generate_letters(correct_side = ''):
    if correct_side == 'l':
        return(random.choice(left_side))
    elif correct_side == 'r':
        return(random.choice(right_side))
    else:
        return(random.choice(right_side + left_side))

def generate_left_letters(num):
    return [generate_letters('l') for x in range(num)]

def generate_right_letters(num):
    return [generate_letters('r') for x in range(num)]

def generate_any_letters(num):
    return [generate_letters('') for x in range(num)]

annika_left_letters = generate_left_letters(3)
central_letter = generate_any_letters(1)

# Get 3 left letters
def get_left_letters():
    return annika_left_letters

# Get a random letter
def get_central_letters():
    return central_letter














