import  random
import string



def generatePassword(length):
    print("Enter the Password length")

    asciiNumber = string.ascii_letters
    digits = string.digits
    totalChars = asciiNumber + digits
    password = ""

    # groupings = [for char in totalChars]
    # print(groupings,"groupings")

    for char in range(length):
        # ranomNum = random.randint(0,len(totalChars) -1)
        # password += totalChars[ranomNum]
        password += random.choice(totalChars)


    print(password,"password")




def main():
    while True :
        print("Enter the Password length")
        theLength = input()

        try:
            theLength = int(theLength)
        except Exception as err:
            print(err)
            continue

        thePassword = generatePassword(theLength)
        print(f"the password this {thePassword}" )
        break
main()