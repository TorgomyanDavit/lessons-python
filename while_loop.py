

# people = {
#     "julia":11,
#     "arman":152,
#     "gevor":17,
#     "vardan":18,
# }

# keys = list(people.keys())


'''
count = -1
while count < 10:
    count+=1
    if count == 5 :
        continue
    print(str(count) + "Hello world")  
'''

while True :
    print("1. Settings")
    print("2. Home")
    print("3. Profile")
    print("4. Exit")
    print("Enter menu Id")
    comand = input()
    print("=============")

    if int(comand) == 1 :
        print("home Page")
    elif int(comand) == 2 :
        print("settings Page")
    elif int(comand) == 3 :
        print("Profile Page")      
    elif int(comand) == 4 :
        print("Exit Page")
        break



    

