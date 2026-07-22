set1 = {1,3,2,4,5}
print(set1)
set1.add(7)
print(set1)

set2 ={"java","python","php","kotlin","dart"}
print(set2)
print("dasfb" in set2)

for i in set2:
    print(i)

set2.pop()
print(set2)

s1 = {1,2,3}
s2 = {3,4,5,6}
s3 = s1.difference(s2)
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)

s1.discard(1)
print(s1)


s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = s1.intersection(s2)
print(s3)
s1.intersection_update(s2)
print(s1)

print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s2)
s2.pop()
print(s2)

s3 =s1.union(s2)
print(s3)





