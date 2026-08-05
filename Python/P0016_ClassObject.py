class User:
    __id = 0
    __name = ''
    __contact = 0

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setContact(self,contact):
        self.__contact = contact

    def getContact(self):
        return self.__contact


u1 = User()
u1.setId(12)
print(u1.getId())