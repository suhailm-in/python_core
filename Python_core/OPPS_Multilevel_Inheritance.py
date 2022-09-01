class student:
    def __init__(self,name,mark,rank):
        self.name=name
        self.mark=mark
        self.rank=rank
    def getdetails(self):
        self.name=input("enter name: ")
        self.mark=int(input("enter mark: "))
        self.rank=int(input("enter rank: "))
    def putdetails(self):
        print(self.name,self.mark,self.rank)

class teacher(student):
    def desplay(self):
        print("I am the teacher")

class perants(teacher):
    def perdesplay(self):
        print("I am the Perant")

class admin(perants):
    def admindesplay(self):
        print("I am the admin")

# # Student class
# obj=student("","","")
# obj.getdetails()
# obj.putdetails()

# # teacher class
# obj=teacher("","","")
# obj.getdetails()
# obj.putdetails()
# obj.desplay()

# # Parent class
# obj=perants("","","")
# obj.getdetails()
# obj.putdetails()
# obj.desplay()
# obj.perdesplay()

# # admin class
# obj=admin("","","")
# obj.getdetails()
# obj.putdetails()
# obj.desplay()
# obj.perdesplay()
# obj.admindesplay()
