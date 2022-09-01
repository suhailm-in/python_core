class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("Enter Your Name : ")
        self.mark=int(input("Enter Your Mark : "))
    def putdetails(self):
        print(self.name,self.mark)
obj=student("","")
obj.getdetails()
obj.putdetails()