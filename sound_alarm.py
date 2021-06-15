# pip install gTTS  
# pip install playsound  
# pip install pyttsx3

import gtts  
from playsound import playsound
from IPython.display import Audio

t1 = gtts.gTTS("M.L. code is executed. Please check, Thank You")  
sound_file = "code_executed.mp3"
t1.save(sound_file)  
Audio(sound_file, autoplay=True)
