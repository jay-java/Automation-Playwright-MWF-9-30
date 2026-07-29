#function - is block of code to execute specified task

#2 TYpes 
#1. pre define
print('hello python')
#2.user define

# ther are 4 categories
#1.without return type without parameter

def functionName():
    print('without return type without parameter')
    
#2.without return type with parameter
def funName(a):
    print('without return type with parameter',a)
    for i in a:
        print(i)
        
#3.with return type without parameter
def fun():
    print('with return type without parameter')
    return '123'
#4.with return type with parameter
def getSquare(num):
    print('num is coming from paramater',num)
    return num*num

functionName()
funName([1,2,3,4])
a = fun()
print(a)

num = int(input('enter num'))
sq = getSquare(num)
print('square of',num,'is',sq)