
s = {10,20,3}
print(s)

print(s.add(4))
print(s)

print(s.remove(20)) # if element not found , it will raise an error
print(s)

print(s.discard(10)) # safe way , if element not found , it will not raise an error
print(s)

s.pop() # remove random element
print(s)

s.clear()
print(s)


s2 = {1,"maruf",2.3}
#frozen set are immutable version of a set. cannot be changed. but can perform operations like union , intersection etc (normal set can do that too , like union , diff , intersect but normal set is mutable so cannt be hashed. Frozenset can be hashed as a result can be used as a dictionary key or as elements of another set)

fs = frozenset(s2)
print(fs)

fs2 = {"maruf",1,3,4.3}

print(fs.intersection(fs2))


#subset check
s1 = {1,2,3,4}
s2 = {1,2,3,4,5,6,7,8,9}

print(s1 <= s2) #  checks if s1 is a subset of s2

s1 = {1,77,73,4}
s2 = {1,2,3,4,5,6,7,8,9}

print(s1 <= s2) #  checks if s1 is a subset of s2

#ops
print(s1 | s2) #union
print(s1 & s2) #intersection
print(s1-s2) # difference
print(s1^s2) #symmetric difference (elements in s1 or s2 but not both)
