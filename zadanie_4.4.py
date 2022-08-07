import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

choose_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie / 2 Odejmowanie / 3 Mnożenie / 4 Dzielenie:")

def add(x,y):
    return x + y

def substraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

    

if choose_operation in ('1', '2', '3', '4'):
    number1 = float(input("Podaj składnik 1:"))
    logging.info(f"Podano argument {number1}")
    
    number2 = float(input("Podaj składnik 2:"))
    logging.info(f"Podano argument {number2}")
    
    if choose_operation == '1':
        logging.info(f"Wybrano operację dodawania")
        print(f"Dodaję {number1} i {number2}")
        result = add(number1, number2)
        print(f"Wynik to: {result}")  

    if choose_operation == '2':
        print(f"Odejmuję {number1} i {number2}")
        result = substraction(number1, number2)
        print(f"Wynik to: {result}")   

    if choose_operation == '3':
        print(f"Mnożę {number1} i {number2}")
        result = multiplication(number1, number2)
        print(f"Wynik to: {result}")    

    if choose_operation == '4':
        print(f"Dzielę {number1} i {number2}")
        result = division(number1, number2)
        print(f"Wynik to: {result}")    

else:
    print ("Nie ma takiej operacji")
    exit

if __name__ == "__main__":
    choose_operation =(sys.argv[1:])
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')    
    



