import  random
import string


def generatePassword(theLength):
    """ This function generates a password of the specified length."""
    
    letters = string.ascii_letters
    digits = string.digits
    totalChars = letters + digits
    password = ""

    for index, i in enumerate(range(theLength)):
        # randomNumber = random.randint(0, len(totalChars) - 1)
        # password += totalChars[randomNumber]
        password += random.choice(totalChars)
    
    return password



def main():

    while True :
        print("Enter the password length")
        theLength = input()

        try:
            theLength = int(theLength)
        except Exception as error:
            print("Wrong password length",error)

        thePassword = generatePassword(theLength)
        print(f"the password this {thePassword}" )
        break
main()

