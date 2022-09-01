from tkinter import *
root=Tk()
def undo():
    print("undo clicked")
mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)

submenu.add_command(label="New")
submenu.add_command(label="Open")
submenu.add_separator()
submenu.add_command(label="save")
submenu.add_command(label="save As")
submenu.add_separator()
submenu.add_command(label="Print")
submenu.add_command(label="Print All")

newmenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)

newmenu.add_command(label="undo",command=undo)
newmenu.add_command(label="Redo")
newmenu.add_separator()
newmenu.add_command(label="Cut")
newmenu.add_command(label="Copy")
newmenu.add_command(label="Past")

viewmenu=Menu(mymenu)
mymenu.add_cascade(label="View",menu=viewmenu)

viewmenu.add_command(label="Zoom in")
viewmenu.add_command(label="Zoom out")

mymenu.add_cascade(label="Tools")
mymenu.add_cascade(label="Help")

root.mainloop()