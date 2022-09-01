
# Name    : Suhail M
# Project : Coding Challenge 10

class desktop:
    def __init__(self,Dweight,Dmonitor,Dpower,Dsoftwer):
        self.Dweight=Dweight
        self.Dmonitor=Dmonitor
        self.Dpower=Dpower
        self.Dsoftwer=Dsoftwer
    def desktopGetspecs(self):
        self.Dweight=("Weight is 10 kg\n")
        self.Dmonitor=("External Monitor\n")
        self.Dpower=("Power Supply\n")
        self.Dsoftwer=("OS & Softwer user choice""\n")
    def desktopDisplayspecs(self):
        print("Desktop Details :-")
        print(self.Dweight,self.Dmonitor,self.Dpower,self.Dsoftwer)

class laptop:
    def __init__(self,Lweight,Lmonitor,Lpower,Lsoftwer):
        self.Lweight=Lweight
        self.Lmonitor=Lmonitor
        self.Lpower=Lpower
        self.Lsoftwer=Lsoftwer
    def laptopGetspecs(self):
        self.Lweight=("Weight is 2 kg\n")
        self.Lmonitor=("Built in Monitor\n")
        self.Lpower=("Battery\n")
        self.Lsoftwer=("OS & Softwer user choice\n")
    def laptopDesplayspecs(self):
        print("Laptop Details :-")
        print(self.Lweight,self.Lmonitor,self.Lpower,self.Lsoftwer)

class computer(desktop,laptop):
    def computerDesplayspecs(self):
        print("Available Devices Desktop and Laptop")


"""-- computer --"""
obj=computer("","","","")
obj.desktopGetspecs()
obj.desktopDisplayspecs()
obj.laptopGetspecs()
obj.laptopDesplayspecs()
obj.computerDesplayspecs()
