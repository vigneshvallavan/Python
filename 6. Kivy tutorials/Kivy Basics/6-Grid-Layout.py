from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size = (360,600)

class MainApp(App):
    def build(self):
        layout = GridLayout(cols = 2, spacing = 10, padding = 40)

        b1 = Button( text = 'Button 1', size_hint = (None,None), width = 100, height = 40 )
        b2 = Button( text = 'Button 2', size_hint = (None,None), width = 100, height = 40 )
        b3 = Button( text = 'Button 3', size_hint = (None,None), width = 100, height = 40 )
        b4 = Button( text = 'Button 4', size_hint = (None,None), width = 100, height = 40 )
        b5 = Button( text = 'Button 5', size_hint = (None,None), width = 100, height = 40 )
   
        layout.add_widget(b1)
        layout.add_widget(b2)
        layout.add_widget(b3)
        layout.add_widget(b4)
        layout.add_widget(b5)
        return layout

MainApp().run()

