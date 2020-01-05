from random import randrange
numberdrawn= randrange(100)
a=1
print('Guess a number from 0 to 100 \n')
while (a == 1):
    while True:
        try:
            n = int(input('Enter your number: '))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    if numberdrawn > n:
        print('The number entered is smaller than the drawn number')
    elif numberdrawn < n:
        print('The number entered is larger than the drawn number')
    else:
        print('You got the number right, CONGRATULATIONS')
        break
    print('Do you want to keep trying?')
    a = int(input('Yes (1) or No (0): '))


