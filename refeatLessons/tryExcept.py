


# try :
#     print(name)
# except Exception as error:
#     print(error)
# name = "Davit"
# try:
#     print(name)
# except Exception as error:
#     print(error)
# else:
#     print(f"Else {name}")
# finally:
    # print("Continue ...")



myString = "helo world"

def changeString():
    try:
        myString += " from Davit"
        return myString
    except Exception as error:
        print("Error occurred:", error)
    finally:
        print("Finally ...")


print(changeString())