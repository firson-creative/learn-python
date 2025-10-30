import math
#from learntools.core import binder
#binder.bind(globals())
#from learntools.intro_to_programming.ex2 import *

def get_expected_cost(beds, baths):
    value = 80000 + (beds * 30000) + (baths * 10000)
    return value

option_one = get_expected_cost(beds = 2, baths = 3)
option_two = get_expected_cost(beds = 3, baths = 2)
option_three = get_expected_cost(beds = 3, baths = 3)
option_four = get_expected_cost(beds = 3, baths = 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

