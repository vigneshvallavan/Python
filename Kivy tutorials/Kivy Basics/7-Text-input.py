from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size = (360,600)

class MainApp(App):
    def build(self):
        layout = GridLayout(cols = 2, spacing = 10, padding = 40)

        self.weight = TextInput(text = 'Enter Weight here...', size_hint = (None,None), width = 150, height = 60)
        self.height = TextInput(text = 'Enter Height here...', size_hint = (None,None), width = 150, height = 60)

        submit = Button( text = 'Submit', size_hint = (None,None), width = 100, height = 40,
                         pos_hint = {'center_x': 0.5},
                         on_press = self.submitfn )
           
        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)

        return layout

    def submitfn(self,obj):
        print("Weigth : ",self.weight.text)
        print("Heigth : ",self.height.text)

MainApp().run()

