#membership operators

a = "hello"
b = "hello world"

if (a in b):
    print("true")

if (a not in b):
    print("true")

#identity operators

p = [20,10,30,40]
q = [20,30]
r = p

print(r not in p)
print(q in p)

#bitwise operators

a = 5
b = 3
print ("The bitwise left shift  a << 1 :",a << 1)
print ("The bitwise left shift  b << 1 :",b << 1)

print ("The bitwise left shift  a >> 1 :",a >> 1)