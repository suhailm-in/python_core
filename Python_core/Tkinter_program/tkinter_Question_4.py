from tkinter import *
root=Tk()

def file1():
    print("This is New")
def file2():
    print("This is Open")
def file3():
    print("This is Save")
def file4():
    print("This is Save As")
def file5():
    print("This is Print")

def edit1():
    print("This is Undo")
def edit2():
    print("This is Redo")
def edit3():
    print("This is Cut")
def edit4():
    print("This is Copy")
def edit5():
    print("This is Past")
def edit6():
    print("This is Delete")

def View1():
    print("This is Zoom in")
def View2():
    print("This is Zoom Out")
def View3():
    print("This is Find")
def View4():
    print("This is Run")
def View5():
    print("This is Debug")
def View6():
    print("This is Appearance")

def Tool1():
    print("This is Task & Contexts")
def Tool2():
    print("This is Code With Me")
def Tool3():
    print("This is IDE Scripting")
def Tool4():
    print("This is XML Action")
def Tool5():
    print("This is Markdown Converter")
def Tool6():
    print("This is Creat setup.py")

def Help1():
    print("This is Find Actions")
def Help2():
    print("This is Learn IDE Features")
def Help3():
    print("This is Contact Support")
def Help4():
    print("This is Submit Bug Report")
def Help5():
    print("This is Submit FeedBackr")
def Help6():
    print("This is About")


mainMenu=Menu(root)
root.config(menu=mainMenu)

submenu1=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="New",command=file1)
submenu1.add_command(label="Open",command=file2)
submenu1.add_separator()
submenu1.add_command(label="Save",command=file3)
submenu1.add_command(label="Save As",command=file4)
submenu1.add_separator()
submenu1.add_command(label="Print",command=file5)
submenu1.add_separator()
submenu1.add_command(label="Exit",command=quit)

submenu2=Menu(mainMenu)
mainMenu.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="Undo",command=edit1)
submenu2.add_command(label="Redo",command=edit2)
submenu2.add_separator()
submenu2.add_command(label="Cut",command=edit3)
submenu2.add_command(label="Copy",command=edit4)
submenu2.add_separator()
submenu2.add_command(label="Past",command=edit5)
submenu2.add_command(label="Delete",command=edit6)

submenu3=Menu(mainMenu)
mainMenu.add_cascade(label="View",menu=submenu3)
submenu3.add_command(label="Zoom in",command=View1)
submenu3.add_command(label="Zoom out",command=View2)
submenu3.add_separator()
submenu3.add_command(label="Find",command=View3)
submenu3.add_command(label="Run",command=View4)
submenu3.add_command(label="Debug",command=View5)
submenu3.add_separator()
submenu3.add_command(label="Appearance",command=View6)

submenu3=Menu(mainMenu)
mainMenu.add_cascade(label="Tools",menu=submenu3)
submenu3.add_command(label="Task & Contexts",command=Tool1)
submenu3.add_command(label="Code With Me",command=Tool2)
submenu3.add_separator()
submenu3.add_command(label="IDE Scripting",command=Tool3)
submenu3.add_separator()
submenu3.add_command(label="XML Action",command=Tool4)
submenu3.add_command(label="Markdown Converter",command=Tool5)
submenu3.add_command(label="Creat setup.py",command=Tool6)

submenu4=Menu(mainMenu)
mainMenu.add_cascade(label="Help",menu=submenu4)
submenu4.add_command(label="Find Actions",command=Help1)
submenu4.add_separator()
submenu4.add_command(label="Learn IDE Features",command=Help2)
submenu4.add_separator()
submenu4.add_command(label="Contact Support",command=Help3)
submenu4.add_command(label="Submit Bug Report",command=Help4)
submenu4.add_command(label="Submit FeedBack",command=Help5)
submenu4.add_separator()
submenu4.add_command(label="About",command=Help6)

root.mainloop()
