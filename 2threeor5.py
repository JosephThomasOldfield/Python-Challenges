'''
Create a variable called num.
Check if the variable is divisible by 3 or 5.
If it is log “This number is divisible by 3 or 5”
to the console. Otherwise log “This number is not
divisible by 3 or 5”.
'''

num = 15

def divthreeorfive(numbervalue):
    if numbervalue % 5 == 0 and numbervalue % 3 == 0:
        print("Number divides by three and five.")
    else:
        print("Does not divide by three and five.")


divthreeorfive(num)
