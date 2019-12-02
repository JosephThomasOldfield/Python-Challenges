'''Create a variable called password.
Check how many letters are in the password,
 if there are less than 8 log to the console 
 that the password is too short. Otherwise log 
 the password to the console.'''


password = "password"


def passwordChecker(passCheck):
    if len(passCheck) >= 8:
        print(passCheck)
    else:
        print("Password is too short")


passwordChecker(password)