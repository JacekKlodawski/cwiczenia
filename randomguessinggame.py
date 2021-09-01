import random

def guess(x):
    random_number = random.randint(1,x)
    i = 0
    a = 0
    no_trys = int(input('ile chcesz mieć prób:'))
    while a != random_number:
        i = i + 1
        if i > no_trys:
            print('Przykro mi, skończyły ci się próby')
            break
        else:
            a = int(input('Podaj liczbę'))
            if a < random_number:
                print('Za mało')
            elif a > random_number:
                print('za dużo')
    print('Brawo')



guess(14)

#as dadfsg