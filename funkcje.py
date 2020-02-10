import time


#for liczba in range(0,30):
#    a,b = b,a+b
#    print(a,b)
def fibonacci(a,b=3):
    while True:
        a,b = b, a + b
        print(b)
        time.sleep(1)