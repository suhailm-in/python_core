
# Name    : Suhail M
# Project : Generating Audio From Text Data

from gtts import gTTS
import os
text = "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs "
output = gTTS(text=text, lang="en", slow=False)
output.save('output.mp3')
os.system('start output.mp3') #windows="start", mac="afplay"
