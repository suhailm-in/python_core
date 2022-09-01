from tkinter import *
class myfun:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.plable=Label(frame,text="do you want to exit")
        self.plable.pack()

        self.pbutton=Button(frame,text="ok",command=self.pmsg)
        self.pbutton.pack()

        self.cbutton=Button(frame,text="clear",command=self.clea)
        self.cbutton.pack()

        self.qbutton=Button(frame,text="exit",command=frame.quit)
        self.qbutton.pack()

    def pmsg(self):
        print("click Them")
    def clea(self):
        print("Clear")

root=Tk()
obj=myfun(root)
root.mainloop()