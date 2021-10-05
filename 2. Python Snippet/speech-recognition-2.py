import speech_recognition as sr

filename = "speech-to-text.txt"
f = open(filename, "w")

r = sr.Recognizer()

print("\n Make sure are you connected a microphone for recognizing\n ")

mic_list = sr.Microphone.list_microphone_names()

for i in range(len(mic_list)):
    print(mic_list[i])

with sr.Microphone() as source:

    r.adjust_for_ambient_noise(source)

    print("\nRecognizing...\n")

    audio = r.listen(source)

    print("Time Over, thanks!\n")

    try:
        recognized_text = r.recognize_google(audio)
        print("Text (English) : "+recognized_text)                      # print output (speech to text)

        f.write(recognized_text)                                        # store english text in to text file

        print("\nSpeech to text completed---> see the text (speech-to-text.txt) file\n")
    
    except:
        print("Sorry, I did not get that")