

# Name    : Suhail M
# Project : Coding Challenge 9

def addition(a,b):
    return a-(a*b/100)
def square(c):
    return c-(c*5/100 )
x=int(input("Enter Your Amount : "))
y=10
result=addition(x,y)
reguler=square(addition(x,y))
print("Student Discount Price : ",result)
print("Reguler Discount Price : ",reguler)
