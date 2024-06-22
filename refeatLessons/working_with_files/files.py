
""" Read file """

"""
files = open("./users.txt","r")
for line in files.readlines():
    print(line)
print(files.close())
"""


# with open("./users.txt","r") as files:
#     # for line in files.readlines()[1:]:
#     #     # print(type(line)) # type is equal str
#     #     print(line[:-1])

#     for i in range(1):
#         print(files.readline()[:-1])
    
""" Write file """

""" __apend as a__ append file"""
# # append wile write on file without delete existing context inner file
# with open("./output.txt","a") as newFile:
#     newFile.write("new line\n")

""" __new write as w__ delete and write"""
# # new write file write on file delete all existing context inner file
# with open("./output.txt","w") as newFile:
#     newFile.write("new line\n")

# create file write on file if it is not existing if exist we receive error
# try:
#     with open("./output.txt","x") as newFile:
#         newFile.write("new line\n")
# except Exception as err :
#     print(err)

# with open("./create.txt","x") as newFile:
#     newFile.write("")

# with open("./users.txt","r+") as file:
#     for line in file.readlines():
#         if "Male" in line[:-1]:
#             print(line[:-1].split(","))
#             print(line[:-1].split(",")[2])


# Write 
# listName = []
# with open("./users.txt","r+") as file:
#     for line in file.readlines()[:-1]:
#         listName.append(line[:-1].split(",")[0])


# try:
#     for line in listName:
#         with open(f"./{line.split(',')[0]}.txt","x") as file:
#             file.write(line.strip().split(',')[0])
# except Exception as error:
#     print(f"thist file can note craet again becouse it already exist {error}")

