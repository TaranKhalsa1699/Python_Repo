List = ["1", "2", "Taran"]
# newList = []
# i = 0
# while i in List:
#     newList.append()
#     i = i + 1
# print(newList)


# while i < len(List):
#     newList.append(i)
#     i += 1
# print(newList)

# for x in List:
#     if "" in x:
#      newList.append(x)
# print(newList)
newList = [x for x in List if x != "Taran"]
print(newList)
newList = [x.upper() for x in List]
print(newList)
newList = [ x if x != "Taran" else "TARAN" for x in List]
print(newList)
newList = [ x for x in List if x == "Taran"]
print(newList)
