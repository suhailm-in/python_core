from  tkinter import *
root=Tk()

canvas=Canvas(root,width=100,height=200)
canvas.pack()
line1=canvas.create_line(0,0,10,20)
line2=canvas.create_line(10,50,30,10)
line3=canvas.create_oval(70,0,30,40)
line4=canvas.create_rectangle(10,40,90,60)

root.mainloop()