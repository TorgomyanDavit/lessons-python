data = {
    "John":2800,
    "july":1500,
    "Simon":3500,
    "salary":[100,200,300,400,500]
}

friends = {
    "boys":["Gag","Armen","Vzgo","Davo"],
    "july":1500,
    "Simon":3500,
    "salary":[100,200,300,400,500]
}

# print(data)
# print(len(data))
# print(len(data["salary"]))
# print(data["salary"][2:])
# print(data["arman"]) this give error when Arman  is not defined in dictionary
# print(data.get("arman")) # this way we can avoid error when key is not defined

# Change Data
# data["John"] = 8888
# print(data.get("John"))

# friends["salary"].append(5000)
# print(friends.get("salary"))

data.update({"july":500,"John":800})
# print(data.get("John"))
keysData = data.keys()
valuesData = list(data.values())
print(valuesData[0]) #this not give error #this give error 
print(keysData[0]) #this give error 

# print(keysData)
# print(valuesData)

# print(type(valuesData))