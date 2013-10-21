import math

def even_numbers_only(thelist):
    '''
    Returns a list of even numbers in thelist
    '''
    return [x for x in thelist if x%2 == 0]

def is_perfect_square(x):
    '''
    Returns True if x is a perfect square, False otherwise
    '''
    thesqrt = int(math.sqrt(x))
    return thesqrt * thesqrt == x
