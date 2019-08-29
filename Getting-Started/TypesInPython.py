
# Type Hinting
def add_numbers(a, b):
    print (a + b)

# just telling IDE to warning you.
def add_numbers2(a:int, b:int) -> int:
    print (a + b)

# Integers Floats
def LearnIntegersAndFloats():
    answer = 42 # int
    pi = 3.14 # floats

    print (answer + pi) # answer + pi = 45.314. No need to worry about conversion.
    
    # convert
    print(int(pi)) # == 3
    print(float(answer)) # == 42

# String
# Python3 >> Unicode, Python2 >> ACSII
# """<Comments>"""
def LearnString():
    print('hello'.capitalize()) # Hello
    print('hello'.replace('e', 'a')) #hallo
    print('hello'.isalpha()) # true
    print('hello'.isdigit()) # false
    print('some,csv,values'.split(',')) # ['some','csv','values']

    name = 'solarseed'
    machine = 'devbox'
    print('nice to meet you {0}, I am {1}'.format(name, machine))

    # Only In Python 3
    print(f'nice to meet you {name}. I am {machine}')

# Some other type:
    #complex
    #long # only in python 2
    #bytes and bytearray
    #tuple
    #set
    #frozenset


# Run def
LearnString()