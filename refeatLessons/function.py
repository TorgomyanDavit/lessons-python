
import os
from datetime import datetime

# def PrintHello(fromHo,To):
#     print("hello from" + fromHo + " to " + To)

# PrintHello("Davit","Vardan")


# def sum(numberOne,numberTwo) :
#     print(numberOne + numberTwo)

# sum(5,4)

# myVar = "someText"
# myVarTwo = "155"

# print(type(myVar))
# print(type(myVarTwo))
# print(type(str(myVarTwo)))
# print(type(int(myVarTwo)))



# os Funtion

# ditPath = os.getcwd()
# print(ditPath)

# print(datetime.today())



# def sum(num):
#     print(num)
# sum(5)


# def double(num):
#     if(num < 2) :
#         return num
    
#     num += 1
#     return num

# doubleValue = double(5)
# print(doubleValue)

myString = "helo world"
def changeString():
    global myString
    myString += " from Davit"
    return myString
print(changeString())

