import random

def computerguess(low,high):
    feedback = ''
    
    while feedback != 'c':
        guess = random.randint(low,high)
        print(guess)
        feedback = input('high, low lub correct')

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print('dobra liczba')

            
computerguess(1,1000)


