
file=open("demo3.txt","r")
cont=file.read()
print(cont)
file.close()


file=open("demo3.txt","w")
file.write("this is python file write project ")
file.close()

file=open("demo3.txt","a")
file.write("append mode")
file.close()