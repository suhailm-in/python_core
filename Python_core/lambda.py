a=lambda a,b: a+b
print(a(2,3))

b=lambda a: a+30
print(b(5))

c=lambda x,y,z : x+12+y+z
print(c(3,5,10))

def fun(e):
    return lambda d:d+e
g=fun(2)
print(g(4))

#x*(x+5)^2

