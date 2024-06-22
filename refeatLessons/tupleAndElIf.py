
month = "junyar","febuari","march"
monthDat = 1,2,3,4,5,6,7,8,9,10,11,12

comand = input()
login = False
if comand == "1":
    print("open Home Page")
elif comand == "2" and not login:
    print("open Settings Page")
elif comand == "8" or comand == "9":
    print("comand is " + comand)
else:
    print("Ends") 