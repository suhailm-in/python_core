from tkinter import *
class myfun:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.pbutton=Button(frame,text="click",command=self.pmsg)
        self.pbutton.pack()

        self.qbutton=Button(frame,text="exit",command=frame.quit)
        self.qbutton.pack()

    def pmsg(self):
        print("clicked")

root=Tk()
obj=myfun(root)
root.mainloop()