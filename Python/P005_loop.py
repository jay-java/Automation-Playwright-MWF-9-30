#for var in range(startPoint, endPoint+1):
for i in range(1,7):
    print(i)
    
for i in range(6):
    print(i)
    
for i in range(10,0,-1):
    print(i)
    

#while(condition)
a = 1
while(a <= 5):
    print(a)
    a = a+1

b = 5
while(b >= 1):
    print(b)
    b = b-1
    
    
for r in range(1,5): #row
    for c in range(1,6): #col
        print('* ',end='')
    print()
    

for i in range(1,6): #row
    for j in range(i): #col
        print('* ',end='')
    print()
    
    
for i in range(1,6): #row
    for j in range(1,i+1): #col
        print(j,end='')
    print()
    
for i in range(1,6): #row
    for j in range(1,i+1): #col
        print(i,end='')
    print()
    
    
for i in range(1,6): #row
    for s in range(5,i,-1):
        print(' ',end='')
    for j in range(i): #col
        print('* ',end='')
    print()
    
    
