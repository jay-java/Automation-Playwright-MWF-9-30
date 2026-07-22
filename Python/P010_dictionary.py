dict1 ={
    1:"c",
    2:"c++",
    "java":3,
    34.34:"php",
}

print(dict1)
dict1[5] = "kotlin"
print(dict1)

dict1[1] = "python"
print(dict1)

students = {
    "s1" : {
        "id":1,
        "name":"python",
        "contact":1234566798,
        "address":"ahmedabad"
        },
    "s2" : {
       "id":1,
       "name":"python",
       "contact":1234566798,
       "address":"ahmedabad"
        },
}
print(students)
print(students["s1"]["name"])

#values from dictionary
for i in students.values():
    print(i)
    
#key value from dictionary
for i in students.items():
    print(i)
    
for i,j in students.items():
    print('key ',i,' : values ',j)
