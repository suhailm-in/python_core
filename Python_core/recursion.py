def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)       # 3*fact(3-1)
res=fact(int(input("Enter a value : ")))
print(res)