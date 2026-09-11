#Class -> structure in which we can have member functions and member variables
#OBjecty -> is instance of class with state(data) and behavior
#constructor-> is special member function class which is __init__() block
#have no return type and it will call automatically when object is created
class Student:
    __id = 0
    __name = ''

    def __init__(self):
        print('this is constructor')

    def call(self):
        print('call function in Student')
        
    def add(self,a,b):
        print('add in Student')
        print(a+b)


    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

obj = Student()
obj.call()
obj.add(12,12)

obj.setId(12)
print(obj.getId())

