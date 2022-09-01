
# Name    : Suhail M
# Project : Additional_Question_6

a=(1,2,3,"one","two","three")
print(a)
print(type(a))
b=list(a)

b.append("four")
print(b)

b.insert(3,4)
print(b)

print(b.index("three"))
print(b[-2])
