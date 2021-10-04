import gtts
import pyttsx3

text_input = "Hi vignesh, Welcome to Python Programming. Now we perform a snippet of 'text to speech'."

language = 'en'

speech = gtts.gTTS(text = text_input, lang = language, slow = False)

speech.save('text-to-speech.mp3')


# Play the text in console window

s = pyttsx3.init()

print("\nNow you hear a speech as Default rate")
s.say(text_input)                   # say() method - passed the text as an argument, It is used to add a word to speak to the queue,
s.runAndWait()                      # runAndWait() method runs the real event loop until all commands queued up

rate = s.getProperty("rate")  
print("\nDefault speech speed = ",rate)

print("\nNow you hear a speech as rate is 300")
s.setProperty("rate", 300)  
s.say(text_input)  
s.runAndWait()  

print("\nNow you hear a speech as rate is 100")
s.setProperty("rate", 100)  
s.say(text_input)  
s.runAndWait()  