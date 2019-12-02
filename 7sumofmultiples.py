'''
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
firstmultiple = 3
secondmultiple = 5
bellownumber = 1000

def sumofmultiples(multiple1, multiple2, bellow):
    print(sum(i for i in range(bellow) if i % multiple1 == 0 or i % multiple2 == 0))

sumofmultiples(firstmultiple, secondmultiple, bellownumber)