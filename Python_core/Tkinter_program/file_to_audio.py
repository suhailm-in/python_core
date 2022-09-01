
# Name    : Suhail M
# Project : Converting File Data To Audio

from gtts import gTTS
import os
text=open('audio.txt','r',encoding="utf-8").read()
language="hi"
output=gTTS(text=text,lang=language,slow=False)
output.save('fileoutput.mp3')
os.system("start fileoutput.mp3")