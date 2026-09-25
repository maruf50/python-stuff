print("hello")

a = 8
b = 7
color = "Cyan"

x,y,z = 1,2.5,"maruf"
print(x,y,z)

print(type(x))

a,b = b,a
print(a,b)

print("\n")

word = "skibidisigma"
length = len(word)
print("length of the word is: ", length)
print(word[0:3] + word[5:9]) #manipulating words

print("\n")

# arithmatic ops

a,b = 10,3

print("addition : ",a+b)
print("sub : ",a-b)
print("multiplication : ",a*b)
print("div : ",a/b)
print("mod : ",a%b)
print("exp : ",a**b) # ** works as ^ , like 5^2 = 25

print("\n")
# comparison ops
print(a>b)
print(a<=b)


print("\n")
# logical ops
a = 1
b = 0
print(a and b)
print(a or b)
print(not a) # look how "not a = False" , you might expect it to result 0
print(not b)

print("\n")
#bitwise ops

p = 50
q = 4
print(p&q)
print(p|q)
print(p^q) # XOR operation (0 for maching bits , 1 for non matching bits)
print(~p) # ~p = -p-1
print(p >> 2) # right shift 2
print(p << 2) # left shift 2

print("\n")
#assignment ops

p = p+1
print(p)
p -= 1
print(p)

p *=q
print(p)

p <<= q
print(p)

print("\n")
#membership ops


x = 22
y = 20

list = [10,20,30,40,50]

if(x not in list):
    print("x is not a member of list")
else:
    print("x is a member of list")


if(y in list):
    print("y is a member of list")
else:
    print("y is not a member of list")

print("\n")
#ternary operations

a,b = 10,2
min = a if(a<b) else b
print("the minimum val is: ",min)





