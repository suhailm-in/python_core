
# Name    : Suhail M
# Project : Calculator_Project

import parser
from tkinter import *
root=Tk()

# calculator display
root.title("Calculator")
display=Entry(root,width=30,bd=10)
display.grid(row=1,columnspan=6,pady=5)

# input number display calculater
i=0
def get_veriable(num):
    global i
    display.insert(i,num)
    i+=1

# AC button clear all
def all_clear():
    display.delete(0,END)

# AC button clear back
def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        all_clear()
        display.insert(0,new_string)
    else:
        all_clear()
        display.insert(0,"Error")

# opreters button
def get_operater(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculater():
    entitre_string=display.get()
    try:
        a=parser.expr(entitre_string).compile()
        result=eval(a)
        all_clear()
        display.insert(0,result)
    except Exception:
        all_clear()
        display.insert(0,"Error")

# calculator buttons 0 to 9
Button(root,text="9",width=5,command=lambda :get_veriable(9)).grid(row="3",column="2")
Button(root,text="8",width=5,command=lambda :get_veriable(8)).grid(row="3",column="1")
Button(root,text="7",width=5,command=lambda :get_veriable(7)).grid(row="3",column="0")
Button(root,text="6",width=5,command=lambda :get_veriable(6)).grid(row="4",column="2")
Button(root,text="5",width=5,command=lambda :get_veriable(5)).grid(row="4",column="1")
Button(root,text="4",width=5,command=lambda :get_veriable(4)).grid(row="4",column="0")
Button(root,text="3",width=5,command=lambda :get_veriable(3)).grid(row="5",column="2")
Button(root,text="2",width=5,command=lambda :get_veriable(2)).grid(row="5",column="1")
Button(root,text="1",width=5,command=lambda :get_veriable(1)).grid(row="5",column="0")
Button(root,text="0",width=5,command=lambda :get_veriable(0)).grid(row="6",column="1")

# calculator buttons "Exit" and "."
Button(root,text="Exit",width=5,command=quit).grid(row="6",column="0")
Button(root,text=".",width=5,command=lambda :get_operater(".")).grid(row="6",column="2")

# calculator buttons  " = + - x "
Button(root,text="x",width=5,command=lambda :get_operater("*")).grid(row="3",column="3")
Button(root,text="-",width=5,command=lambda :get_operater("-")).grid(row="4",column="3")
Button(root,text="+",width=5,command=lambda :get_operater("+")).grid(row="5",column="3")
Button(root,text="=",width=5,command=lambda :calculater()).grid(row="6",column="3")

# calculator buttons " AC C ÷ % "
Button(root,text="AC",width=5,command=lambda :all_clear()).grid(row="2",column="0")
Button(root,text="C",width=5,command=lambda :undo()).grid(row="2",column="1")
Button(root,text="÷",width=5,command=lambda :get_operater("/")).grid(row="2",column="2")
Button(root,text="%",width=5,command=lambda :get_operater("%")).grid(row="2",column="3")




root.mainloop()