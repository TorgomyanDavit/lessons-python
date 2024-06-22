names = ["John","Smith","Andrew","July"]

ages = [18,28,38,50,65,8]

mixedLists = [18,28,"Andrew",True]

nestedLists = [
    ["John","Smith","Andrew","July"],
    [18,28,38,50,65]
]

# print(names)
# print(ages)
# print(mixedLists)
# names[1] = "David"
# names.append("Ben")
# lastElement = names.pop()
# print(lastElement)


sumeOfLists = nestedLists[0] + nestedLists[1]
# print(sumeOfLists) 

multipleLists = nestedLists[1] * 2
# print(multipleLists)


fromToList = ages[:2]
print(len(ages))
print(fromToList)
