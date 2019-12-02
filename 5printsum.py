'''
Create a function that takes two numbers
and an operator as parameters.
It should return a print out of the sum
e.g. “1 + 2 = 3” or “4 x 6 = 24”.
'''

num1 = 10
num2 = 15

def printsum(value1, value2):
    valuesum = value1 + value2
    valuetimes = value1 * value2
    
    print(" ",value1," x ",value2," = ",valuetimes," ")
    print(" ",value1," + ",value2," = ",valuesum," ")


printsum(num1, num2)

    
