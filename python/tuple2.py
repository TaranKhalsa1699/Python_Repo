tup = (1, 2, 3, "Taran")
# (apple, *mango, banana) = tup
# print(apple)
# print(mango)
# print(banana)
# for i in range(len(tup)):
#     print(tup[i])
# for i in tup:
#     print(i)
# i = 0
# while i < len(tup):
#     print(tup[i])
#     i += 1
# for x in tup:
#     print(x)
tup1 = tup + tup
print(tup1)

tup2 = tup * 2
print(tup2)
x = tup.count("Taran")
print (x)
x = tup.index("Taran")
print (x)

