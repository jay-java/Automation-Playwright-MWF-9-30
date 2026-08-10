#inheritance - to access property of one class to another class
#1.single
# 2.Multilevel
# 3.Multiple
# 4.Hierarchical
# 5.Hybrid
# to make our code reusable

#single
class Animal:#parent
    def canWalk(self):
        print('animal can walk')

    def canSleep(self):
        print('animal can sleep')

class Dog(Animal): #child
    def canBark(self):
        print('dog can bark')
class Cat(Animal):
    def canMeww(self):
        print('cat can meww')


#multilevel
class Puppy(Dog):
    def functiona(self):
        print('puppy functions')

dog = Dog()
dog.canWalk()
dog.canSleep()
dog.canBark()

p = Puppy()
p.functiona()
p.canBark()
p.canSleep()
p.canWalk()



    