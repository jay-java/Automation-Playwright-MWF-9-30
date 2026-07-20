#list is collection of data with ordered format and list is mutable(we can change value of list)
list = [1,2,3,4,'python',True,2345643,2346.456]
print(list)
list.append(1234)
print(list)
list1=  list.copy

print(list.count(1))
print(list[4])

list[5] = False
print(list)

list.extend([1,2,3,4])
print(list)

print(len(list))
print(list.index(1))
print(list.index(1,4,12))

list.insert(3,2346)
print(list)

list.pop()
print(list)

list.remove(1)
print(list)

list.reverse()
print(list)

for i in list:
    print(i)
    
for index,value in enumerate(list):
    print(index, value)

