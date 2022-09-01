
#Now x is tuple
x=(9,"hi","hello",4,12.4,"wellcome")
print(type(x))
print(x[0])

# convert to "tuple to list"(x to y)
y=list(x)
print(type(y))

#Now y is list
print(y)
y.insert(2,"good morning")
print(y)

# convert to "list to tuple"(y to x)
x=tuple(y)
print(type(x))
print(x)

# anather tuple creation
a=tuple(("hi","hello","whoami","where are you"))
print(a)