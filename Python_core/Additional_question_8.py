
# Name    : Suhail M
# Project : Additional_Question_8

class Hospital:
    def __init__(self,admin,doctor,sister,department):
        self.admin=admin
        self.doctor=doctor
        self.sister=sister
        self.department=department
    def getdetails(self):
        self.admin=("admin is joker\n")
        self.doctor=("doctor is Abraham\n")
        self.sister=("sister is bruslee\n")
        self.department=("depatment is Alex\n")

class Department(Hospital):
    def display(self):
        print("Department Class :-")
        print(self.admin,self.doctor,self.sister,self.department)

class patient_Ward:
    def __init__(self,name,age,phone,gender):
        self.name=name
        self.age=age
        self.phone=phone
        self.gender=gender
    def getdetails_patient(self):
        self.name=input("Enter Name: ")
        self.age=int(input("Enter Age: "))
        self.phone=int(input("Enter phone: "))
        self.gender=input("Mail Or Femail: ")
    def putdetails_petient(self):
        print(self.name,self.age,self.phone,self.gender)


"""-- Department --"""
obj=Department("","","","")
obj.getdetails()
obj.display()

"""-- patient_Ward --"""
obj=patient_Ward("","","","")
obj.getdetails_patient()
obj.putdetails_petient()