class Parent1:
    def parent1function(self):
        print('parent 1 function')

    def call(self):
        print('call in parent 1')

class Parent2:
    def parent2function(self):
        print('parent 2 function')

    def call(self):
        print('call in parent 2')

class Child(Parent2,Parent1):
    def childfunction(self):
        print('child function')

c = Child()
c.parent1function()
c.parent2function()
c.childfunction()
c.call()