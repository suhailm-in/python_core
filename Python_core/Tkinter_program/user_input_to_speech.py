

# Name    : Suhail M
# Project : Converting User Input To Speech

from gtts import gTTS
import os
from tkinter import *
root=Tk()
canvas=Canvas(root,width=200,height=300)
canvas.pack()

def texttospeach():
    text=entry.get()
    output = gTTS(text=text, lang="en", slow=False)
    output.save('fileoutput.mp3')
    os.system("start fileoutput.mp3")
entry=Entry(root)
canvas.create_window(200,180,window=entry)
button=Button(text="Start",command=texttospeach)
canvas.create_window(200,230,window=button)

root.mainloop()
