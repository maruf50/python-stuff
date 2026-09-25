x =50
y = ["a","b","c",1,2.5,]
z = {"a","b","c",1,2.5,"a",1,1.25,2.5}
i = 2 + 5j  #complex number
word = "abcdefgh"
print(i)
print(y)
print(z) # sets are mutable and dont allow duplicate

t1 = (1,)
print(t1[0])

dict = {"a":1 , "b":2, "c":2}
for i in dict:
    print(dict[i])
    print(dict.get(dict[i]))