import tkinter as tk
from tkinter.constants import END

from instaloader import Instaloader

root = tk.Tk()
root.title("Insta Profile Pic Downloader")

# Setting Geometry of Tk window
root.geometry("900x700")

tk.Label(root, text = 'Insta Profile Pic Downloader', font = 'Algerian 20 bold', fg = 'red').pack()

tk.Label(root, text = 'Insta User Name : ', font = 'Algerian 13 ', fg = 'black').place(x = 5, y = 60)

u_name = tk.Text(root, font = 'Constantia 10', height = 1.5 , width = 40)
u_name.place(x = 170, y = 60)

T = tk.Text(root,font = 'Constantia 10', height = 20 , width = 80).place(x = 170, y = 200)


def download():
    r = Instaloader()

    Insta_UserName = u_name.get(1.0, END)
    
    print(Insta_UserName)

    DP = r.download_profile(Insta_UserName, profile_pic_only = True) 


tk.Button(root, text = 'Download Profile Picture', font = 'Algerian 13 ', command = lambda:download(), pady = 8, bg = 'royal blue', fg = 'yellow').place( x= 230, y = 110)

tk.mainloop()