import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog
import playsound
import multiprocessing


if __name__ == '__main__':

    root = tk.Tk()
    root.title("Music Player")

    # Setting Geometry of Tk window
    root.geometry("565x400")
    root.configure(background="#0ABDE3")

    # create a music icon lable
    img = Image.open("C:\\Users\\US\\Desktop\\Python Programming\\files\\music--icon.png")
    img = ImageTk.PhotoImage(img)
    
    music_icon_label = tk.Label(root,image = img , bg = "#0ABDE3", fg ="black")
    music_icon_label.place(relx = 0.2,rely = 0.0)

    # create a music lable
    music_label = tk.Label(root, text = "Music Player", bg = "#0ABDE3", fg ="black")
    music_label.place(relx = 0.3,rely = 0.05)
    music_label.configure(font = ('Bernard MT Condensed',20))

    # file name
    file = tk.Label(root, text = 'File Path: ', bg = "#0ABDE3", fg ="black")
    file.place(relx = 0.0,rely = 0.3)
    file.configure(font = ('Algerian',16))

    # create a Playing lable
    playing_label = tk.Label(root, text = "", bg = "#0ABDE3", fg ="black")
    playing_label.place(relx = 0.25,rely = 0.85)   
    playing_label.configure(font = ('Forte',16)) 

    global a
    a = 1

    def open_file():
        global audio_file 
                
        audio_file =  filedialog.askopenfilename(filetypes=(("Audio Files", ".mp3"),   ("All Files", "*.*")))
        print("\nAudio File Added")
        file_response = tk.Label(root,text = audio_file, bg = "gray", fg ="black")
        file_response.place(relx = 0.3, rely = 0.3)
        file_response.configure(font = ('Georgia',14))        

        # create a Play lable
        play_label = tk.Label(root, text = "Click Play button to play this audio", bg = "#0ABDE3", fg ="black")
        play_label.place(relx = 0.15,rely = 0.5)
        play_label.configure(font = ('Forte',16)) 

    def play_fn():
        global p
        global a

        if a == 1:     
            p = multiprocessing.Process(target=playsound.playsound, args = (audio_file, ) )  #args takes two arguments :> ("audio1.mp3", )
            print("playing")
            p.start() 

            playing_label['text'] = 'Audio - Playing'
            a+=1

        else:
            playing_label['text'] = 'Audio - Playing...Click stop and then play...'

    def stop_fn():
        global a
        print("Stopped")
        p.terminate()
        playing_label['text'] = 'Audio - Stopped'
        a = 1
       
    def exit_fn():
        p.terminate()
        root.destroy()

    # Create a open button 
    open_button = tk.Button(root, text = 'Open', bg = "gray", fg ="black", command = lambda:open_file() )
    open_button.place(relx = 0.2,rely = 0.3)
    

    # Create a play button 
    play_button = tk.Button( root, text = 'Play', bg = "green", fg ="yellow", command = lambda:play_fn())
    play_button.place(relx = 0.15,rely = 0.7)
    play_button.configure(font = ('Algerian',16))

    # Create a stop button 
    stop_button = tk.Button( root, text = 'Stop', bg = "red", fg ="black", command = lambda:stop_fn())
    stop_button.place(relx = 0.3,rely = 0.7)
    stop_button.configure(font = ('Algerian',16))

    # Create a Exit button 
    exit_button = tk.Button( root, text = 'Exit', bg = "red", fg ="white", command = lambda:exit_fn())
    exit_button.place(relx = 0.45,rely = 0.7)
    exit_button.configure(font = ('Algerian',16))

    tk.mainloop()


