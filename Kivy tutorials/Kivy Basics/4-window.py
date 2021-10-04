from kivy.app import App
from kivy.uix.label import Label        # For Inserting Label
from kivy.core.window import Window  

#Window.clearcolor = (1,0,0,0) # Background - Red color
#Window.clearcolor = (0,1,0,0) # Background - Green color
#Window.clearcolor = (0,0,1,0) # Background - Blue color
#Window.clearcolor = (0,0,0,1) # Background - Black color
#Window.clearcolor = (1,1,1,1) # Background - White color

Window.clearcolor = (0,1,1,0)

Window.size = (360,600)

class MainApp(App):
    def build(self):
        label = Label(  text = "Hi! Welcome to KIVY",
                        font_size = 24,
                        bold = True,
                        italic = True,
                        color = (1,0,0,1) )
        return label
        
MainApp().run()

