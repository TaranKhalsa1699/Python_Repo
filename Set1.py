# Set = {1, 2, 3, 4, 5}
# Set1 = { "Taran", "Ajay", "Mango"}
# Set3 = { "Taran", "Ajay", "Mango", 44, 33}
# Set4 = { "Taran", "Ajay", "Mango", 34, 56, 39}
# List = [1, 8, 6, 9]
# tuple = ("hello", "World", 12, 50, 30)

# Set2 = Set.union(Set1)
# print (Set2)
# Set2 = Set | Set1
# print(Set2)
# Set2 = Set.union(Set1, Set3, Set4)
# print(Set2)
# Set2 = Set | Set1 | Set3 | Set4
# print(Set2)

# z = Set.union(List)
# print(z)

# z = Set.union(tuple)
# print(z)
# Set = {1, 2, 3, 4, 5}
# Set1 = { "Taran", "Ajay", "Mango"}
# Set3 = { "Taran", "Ajay", "Mango", 34, 33}
# Set4 = { "Taran", "Ajay", "Mango", 34, 56, 39}
# List = [1, 8, 6, 9]
# tuple = ("hello", "World", 12, 50, 30)

# Set.update(List)
# print(Set)
# Set.update(Set1)
# print(Set)

# Set1.intersection(Set3)
# Set = Set1 & Set3
# print(Set)
# Set3.intersection_update(Set4)
# print(Set3)
# Set3.difference(Set4)
# print(Set3)
# Set3.difference_update(Set4)
# print(Set3)


Set = {1, 2, 3, 4, 5}
Set1 = { "Taran", "Ajay", "Mango"}
Set3 = { "Taran", "Ajay", "Mango", 34, 33}
Set4 = { "Taran", "Ajay", "Mango", 34, 56, 39}
List = [1, 8, 6, 9]
tuple = ("hello", "World", 12, 50, 30)

Set0 = Set3.symmetric_difference(Set4)
print(Set0)
# or it can be with 
Set0 = Set3 ^ Set4
print(Set0)
