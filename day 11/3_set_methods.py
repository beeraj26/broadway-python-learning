#add()
s = {1, 2, 3}
result = s.add(4)
print(result) #None; because add() method returns nothing
print(s) #={1, 2, 3, 4}

#update()
s= {1, 2, 3}
s.update([4, 5, 6, 7, 8])
print(s) # {1, 2, 3, 4, 5, 6, 7, 8}

# discard()
s = {1, 2, 3, 4}
s.discard(3)
print(s) # {1, 2, 4}

#remove()
s = {1, 2, 3, 4}
s.remove(2)
print(s) #{1, 3, 4}
s.remove(5) #It raises error

#clear()
s = {1, 2, 3, 4}
s.clear()
#print(s) ={}

#pop()
s = {1, 2, 3, 4}
print(s.pop()) #It reandomly pops out any one value of the last 

#diffrence
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.difference(b)
#print(result) =#{1, 2}

#intersection()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b)) #{3, 4}
print(a & b) # & operator is used for set intersection

#union()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b)) #{1, 2, 3, 4, 5, 6}
print(a | b) #| operator is used for set union

# isdisjoint()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.isdisjoint(b)) #false


#issubset()
a = {1, 2, 3, 4, 5, 6}
b = {2, 3}
print(b.issubset(a)) #True
print(a.issuperset(b)) #True

###symmetric difference()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.symmetric_difference(b)
print(result) #{1, 2, 5, 6}
print(a ^ b) # ^ cap operator is used for symetric diffrence

#symmetric diffrence update()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.symmetric_difference_update(b)
print(result) #none
#print(a) = {1, 2, 5 ,6}



