
# Name    : Suhail M
# Project : Coding Challenge 5

# 2. Open the file, read the contents and display them as output.
file=open("demo.txt","r")
cont=file.read()
print(cont)
file.close()

# 1. Write Python code to open a file named demo.txt and write some random data into it.
file=open("demo.txt","w")
file.write("Hi, Hello World ")
file.close()

# 3. Write python code to add additional text to the existing file on a new line without deleting the previous contents
file=open("demo.txt","a")
file.write(" \nThis is additional text")
file.close()