from tkinter import Button
from kivy.app import App
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy')    
        return label


app = MainApp()
app.run()