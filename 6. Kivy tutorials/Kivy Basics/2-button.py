from kivy.app import App
from kivy.uix.button import Button        # For Inserting Button
from kivy.uix.label import Label        # For Inserting Label

class MainApp(App):
    def build(self):
        button = Button( text = "PRINT", font_size = 20, bold = True, color = (1,0,0,1),
                         size_hint = (0.2,0.2), pos_hint = { 'center_x': 0.5, 'center_y': 0.2 },   
                         on_press = self.printpress,
                         on_release = self.printrelease
                       )

        return button
        
    def printpress(self, obj): 
        print ("PRINT Button has been pressed")

    def printrelease(self, obj):
        print ("PRINT Button has been released")

MainApp().run()
