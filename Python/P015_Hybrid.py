class A:
    def classA(self):
        print('class A function')

class B(A):
    def classB(self):
        print('class B function')


class C(A):
    def classC(self):
        print('class C function')


class D(B,C):
    def classD(self):
        print('class D function')

d = D()
d.classA()
d.classB()
d.classC()
d.classD()
