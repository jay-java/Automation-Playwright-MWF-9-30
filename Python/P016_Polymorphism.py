class Calculate:
    # def addition(self,a,b):
    #     print(a+b)

    def addition(self,a,b,c):
        print('addition in parent',(a+b+c))

    def fun(self):
        print('fun in parent')


class Calc(Calculate):
    def addition(self,a,b,c):
        super().addition(4,5,6)
        print('addition in child',(a+b+c))

c = Calc()
c.addition(1,2,3)
c.fun()


