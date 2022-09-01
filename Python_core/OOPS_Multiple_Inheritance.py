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

class teacher:
    def desplay(self):
        print("I am the teacher")

class admin(student,teacher):
    def admindesplay(self):
        print("I am the admin")

# # Student class
# obj=student("","","")
# obj.getdetails()
# obj.putdetails()

# # teacher class
# obj=teacher("","","")
# obj.desplay()

# # admin class
obj=admin("","","")
obj.getdetails()
obj.putdetails()
obj.desplay()
obj.admindesplay()
