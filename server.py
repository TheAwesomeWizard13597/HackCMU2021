rightSide = "yhnmjuiklop"
leftSide = "asdfgvtrewqcxzb"
import random

def classifyLetter(l, correctSide):
    if l in rightSide and correctSide == 'r':
        return True

    elif l in leftSide and correctSide == 'l':
        return True
    
    else:
        return False

def generateLetters(correctSide = ''):
    if correctSide == 'l':
        return(random.choice(leftSide))

    elif correctSide == 'r':
        return(random.choice(rightSide))

    else:
        return(random.choice(rightSide + leftSide))

