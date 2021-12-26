import math

def math_helper():
    print('Welcome to the simple math helper.')
    print('What would you like to calculate?')
    print('1. Sqrt')
    print('2. Log')
    print('3. Factorial')
    
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("This is not a valid choice. Try again ...")
        else:
            if 1 <= choice <= 3:
                break
            else:
                print("This is not a valid choice. Try again ...")
        
    if choice == 1:
        number = float(input('Enter the number to sqrt: '))
        print(math.sqrt(number))
    elif choice == 2:
        number = float(input('Enter the number to log: '))
        print(math.log(number))
    elif choice == 3:
        number = int(input('Enter the number to factorial: '))
        print(math.factorial(number))

if __name__ == '__main__':
    math_helper()
