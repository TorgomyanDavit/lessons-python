print("======= Working with files  =======")

'''
if not use with , must be close file it important
myFile = open("users.txt","r")
print(myFile.readline())
print(myFile.readline())
myFile.close()

'''

'''
read all line
with open("users.txt","r") as myFile:
    for line in range(10):
        print(myFile.readlines())

'''
'''

The open() function returns a file object, which has a read() method for reading the content of the file:
with open("users.txt","r") as myFile:
        print(myFile.read())
        
'''

'''
read alll line
with open("users.txt","r") as myFile:
    for line in myFile.readlines()[1:]:
        print(line[:-1])
'''

'''
Append - will create a file if the specified file does not exist
with open("output.txt","a") as myFile:
    myFile.write("\nour new line")

'''
'''
# Write - will create a file if the specified file does not exist and dellete all write new all
with open("output.txt","w") as myFile:
    myFile.write("our new line")

'''

'''
try :
    with open("outputs.txt","x") as myFile:
        myFile.write("our new line")
except Exception as error:
    print("error",error)
    
'''

def write_file(dest,text) :
    with open(f"{dest}.txt","a") as myFile :
        myFile.write(text)

with open("users.txt","r") as myFile :
    for line in myFile.readlines() :
        info = line[:-1].split(",")
        if info[3].strip() == "Male":
            write_file("Male",info[3]+"\n")   
        elif info[3].strip() == "Female" :
            write_file("Female",info[3]+"\n")   
        else :
            print("Unknown")
            
            
            

    



