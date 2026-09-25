x =50
y = ["a","b","c",1,2.5,] # list
z = {"a","b","c",1,2.5,"a",1,1.25,2.5} #set
i = 2 + 5j  #complex number
word = "abcdefgh"
print(i)
print(y)
print(z) # sets are mutable and dont allow duplicate

t1 = (1,)
print(t1[0])

dict = {"a":1 , "b":2, "c":5}
for i in dict:
    print(dict[i])
    print(dict.get("c"))
    print("c" in dict)


#Tuples
tuple1 = (1,3,4,"maruf","1:2:2",1.25)
print(tuple1)
print(tuple1[3])
tuple2 = (4,) #endling comma makes it a tuple 
tuple3 = (4) # without ending comma its an int
print(tuple2)
print(type(tuple2))
print(type(tuple3))

#dict with tuple and array or any other combo?
dict3 = {1:(1,"maruf",1.25),2: "two",3:[1,3,5]}

print(dict3)
print(dict3.get(2))
print(dict3.get(1)[1])



