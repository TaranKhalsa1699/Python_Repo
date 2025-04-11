# dict1 = { "Name" :  "Taran", "Age" : 21, "Class" : 12, "Address" : "Ropar"},
# dict2 = { "Name" :  "Karan", "Age" : 20, "Class" : 10, "Address" : "Chandigarh"},
# dict3 = { "Name" :  "Charan", "Age" : 22, "Class" : 11, "Address" : "Mohali"}

My_family = {
    "child1" : { 
    "Name" :  "Taran", 
    "Age" : 21,
    "Class" : 12,
    "Address" : "Ropar"
    },
    "child2" : { 
    "Name" :  "Taran", 
    "Age" : 21,
    "Class" : 12,
    "Address" : "Ropar"
    },
    "child3" :{ 
    "Name" :  "Taran", 
    "Age" : 21,
    "Class" : 12,
    "Address" : "Ropar"
    }
   } 
print(My_family)

for x , obj in My_family.items()
    print(x)

    for y in obj:
        print( ':' + y , obj[y])