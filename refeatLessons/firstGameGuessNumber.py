 

from random import randint

def generate_number():
    randomNumber = randint(0,10)
    return randomNumber


def main():
    theNumber = generate_number()
    triedNumber = 1
    print(f"Guess the Number {theNumber}")

    while True:
        print("Guess the Number")
        number = input()

        try:
            number = int(number)
        except Exception as error:
            print("Wrong number")
            continue
            
        if theNumber == number :
            print(f"Congradulate guess number is {theNumber} you have tried to {triedNumber} time")
            break
        elif theNumber > number:
            print(f"number is more than {number}")
        elif theNumber < number:
            print(f"number is less than {number}")

        triedNumber += 1


            
main()