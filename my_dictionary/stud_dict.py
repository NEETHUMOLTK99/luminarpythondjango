#value stored in key:value pairs
students={"roll no":100,"name":"ajay","course":"mca"}

#acess name
print(students["name"])
#course
print(students["course"])
#updating total with value150
students["total"]=150
#adding new key value pairs
#checking for a key in dict
print("gender" in students)
print("name" in students)

#adding a new key valuepairs
students["gender"]="male"
print(students)