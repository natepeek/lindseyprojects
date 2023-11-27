"""Gullible, by Al Sweigart al@inventwithpython.com
How to keep a gullible person busy for hour. (This is a joke program.)
View the code on their website
Tags: tiny, beginner, humor"""

print('Gullible, by Al Sweigart al@inventwithpython.com')

while True: # Main program loop.
    print('Do you want to know how to keep a gullible person busy for hours? Y/N')
    response = input('> ') # Get the user's response
    if response.lower() == 'no' or response.lower() == 'n':
        break
    if response.lower() == 'yes' or response.lower() == 'y':
        continue
        print('"{}"is not a vaild yes/no response.' format(response))

print('Thank you. have a nice day!')