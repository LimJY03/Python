import random

def roll(num):
    '''
    This function returns a random integer between 1 and the user input.

    >>> roll(3):
    2
    '''

    outcome = random.randint(1, num)
    return outcome