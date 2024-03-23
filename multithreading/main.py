

def genderFilter(file_name):

    # delete file
    with open("male.txt", "w") as maleFile:
        pass  

    # delete file
    with open("female.txt", "w") as femaleFile:
        pass

    with open(f"{file_name}.txt", "r") as myFile:
        for line in myFile.readlines()[1:]:
            info = line.strip().split(",")  
            if info[3] == "male" :  
                with open("male.txt","a") as myFile:
                    myFile.write(f"\n{info[2]}")
            else:
                with open("female.txt","a") as myFile:
                    myFile.write(f"\n{info[2]}")

genderFilter("users")
