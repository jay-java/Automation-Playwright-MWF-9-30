#encapsulation : wrapping data into single unit is called
class Studnet:
    def __init__(self,id,name,contact):
        self.__id = id
        self.__name = name
        self.__contact = contact
        print('id = ',id,' name = ',name,' contact = ',contact)

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def __str__(self):
        return  f'id = {self.__id}, name = {self.__name}, contact = {self.__contact}'

s1 = Studnet(1,'user1',9876543521)
s2 = Studnet(2,'user2',9876543521)

id = s1.getId()
print(id)
name = s1.getName()
print(name) 
print(s1)