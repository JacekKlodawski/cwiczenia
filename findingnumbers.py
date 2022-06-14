#dana jest lista, znajdź liczby podzielne przez 5 ale nie podzielne przez 3

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]

def find(list):
    new_list = []
    for number in list:
        if number % 5 == 0 and number % 3 != 0:
            new_list.append(number)
    print(new_list)

#znajdz liczby pierwsze w liscie

def znajdz(list):
    pierwsze = []
    niepierwsze = []
    
    for number in range(2,45):
        if i % number == 0:
            niepierwsze.append(number)
        else:
            pierwsze.append(number)

    print(pierwsze)
    print(niepierwsze)


znajdz(list)
        
