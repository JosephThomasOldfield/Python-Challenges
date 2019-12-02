'''
Create a variable called num.
If num is divisible by 3 log “fizz” to the console,
if it’s divisible by 5 log “buzz” to the console,
if it’s divisible by both 3 and 5 log “fizz buzz”
to the console. Otherwise log num to the console.
'''

num = 15

def fizzbuzz(numberValue):
    if numberValue % 5 == 0 and numberValue % 3 == 0:
        print("FIZZ BUZZ - divides by 3 and five")
    elif numberValue % 5 == 0:
        print("BUZZ - divides by 5")
    elif numberValue % 3 == 0: 
        print("FIZZ - divides by three")
    else:
        print(numberValue)

fizzbuzz(num)