from tkinter import *
from tkinter import messagebox
root=Tk()

messagebox.showinfo("info Box","Helloo World")
messagebox.showwarning("Warning Box","Thare is some problem !")
messagebox.showerror("Error Box","404 error")

messagebox.askquestion("Question Box","are you ok to countinu ?")
messagebox.askokcancel("ok or cancel","do you want to countinu ")
messagebox.askyesno("yes or no","delet all file")
messagebox.askretrycancel("retry or cancle","try again?")
messagebox.askyesnocancel("yes , no or cancel","are you rady to play")

root.mainloop()