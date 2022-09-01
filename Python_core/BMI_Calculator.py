
# Name    : Suhail M
# Project : Body Mass Index Calculator (BMI)

def bm_index(y,z):
    print("Your Body Mass Index is ", y / (z**2))
h = int(input("Enter Your Height in centi metre (cm) "))
w = int(input("Enter Your Weight in Kilo Gram   (kg) "))
d = h / 100.0
bm_index(w,d)
