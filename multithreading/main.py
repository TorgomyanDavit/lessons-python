import os
import time
import threading
current_dir = os.path.dirname(__file__)

print(current_dir)
def genderFilter(file_name,start_line,end_line):

    # delete file
    with open("male.txt", "w") as maleFile:
        pass  

    # delete file
    with open("female.txt", "w") as femaleFile:
        pass

    with open(os.path.join(current_dir,file_name), "r") as myFile:
        for line in myFile.readlines()[start_line:end_line]:
            info = line.strip().split(",")  
            if info[3] == "male" :  
                with open("male.txt","a") as myFile:
                    myFile.write(line)
            else:
                with open(os.path.join(current_dir,"female.txt"),"a") as myFile:
                    myFile.write(line)
            time.sleep(0.1)

start_time = time.time()

# genderFilter("users.txt",1,50)
# genderFilter("users.txt",50,100)

# Define two threads, each targeting the genderFilter function with different arguments
thread1 = threading.Thread(target=genderFilter,args=("users.txt",1,50))
thread2 = threading.Thread(target=genderFilter,args=("users.txt",50,100))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish execution
thread1.join()
thread2.join()


print("Completeed Time",time.time() - start_time)

