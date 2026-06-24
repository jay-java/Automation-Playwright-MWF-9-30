#1.if else
a = 100
b = 20
if(a > b):
    print('a is greater than b')
else:
    print('b is greater than a')
    
#2.nested if
age = 39
if(age > 18):
    if(age < 55):
        print('You are eligible')
    else:
        print('age is greater than 18 but not less than 55')
else:
    print('age is less than 18')
    

#3.elif
per = 76
if(per < 35):
    print('fail')
elif(per >= 35 and per <= 60):
    print('pass class')
elif(per >= 61 and per <= 70):
    print('C grade')
elif(per >= 71 and per <= 80):
    print('B grade')
elif(per >= 81 and per <= 90):
    print('A grade')
elif(per >= 91 and per <= 100):
    print('A+ grade')
else:
    print('invalid input')
    

#4.match
choice = 2
match choice:
    case 1:
        print('you selected english')
    case 2:
        print('you selected hindi')
    case 3:
        print('you selected gujarati')
     
