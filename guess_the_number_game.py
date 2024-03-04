import random
import math

def generateNumber():
    randomNumber = random.randint(0,10)
    return randomNumber

def main():
    theNumber = generateNumber()

    while True:
        print("Guess the number")
        print(theNumber)

        point = input()
        try:
            point = int(point)
        except Exception as error :
            print("exception error =>",error)
            continue

        if point == theNumber:
            print(f"you win guess number is {point}")
            break
        elif point > theNumber:
            print("number must be less than {} and {}".format(str(point),str(point)))
        elif point < theNumber :
            print(f"number must be greater than {point}")

main()