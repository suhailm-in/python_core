from tkinter import *
root=Tk()

def but():
    print("Button clicked")
butt1=Button(root,text="click",bg="red",command=but)
butt1.pack()

root.mainloop()