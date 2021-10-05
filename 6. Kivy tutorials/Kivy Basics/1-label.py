from kivy.app import App
from kivy.uix.label import Label        # For Inserting Label

class MainApp(App):
    def build(self):
        label = Label(  text = "Hi! Welcome to KIVY",
                        font_size = 30,
                        bold = True,
                        italic = True,
                        color = (1,0,0,1) )
        return label
        
MainApp().run()


