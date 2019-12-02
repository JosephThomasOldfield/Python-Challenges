'''
Write a function that takes two numbers as parameters
and returns a random number between them.
'''
import random

def random_number_2_par (n1, n2):
    print(random.randint(n1, n2))

random_number_2_par(5, 10)
