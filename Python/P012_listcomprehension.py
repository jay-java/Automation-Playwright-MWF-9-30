#list = [data]
#list_name= [expression for item in list(iterable)]
#expression -> operation applied to each item
#item -> variable representing exist list
#iterable -> source(list)

num = [1,2,3,4,5]
sq = []
for i in num:
    sq.append(i ** 2)
print(sq)

#com
square = [i ** 2 for i in num]
print(square)
 

even = [n for n in range(20) if n % 2 == 0]
print(even)


state = ['even' if n % 2 == 0 else 'odd' for n in range(7)]
print(state)



