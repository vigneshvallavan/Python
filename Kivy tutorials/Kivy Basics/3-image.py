from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        #img = Image(source = 'nature.jpg')
        img = AsyncImage(source = 'https://i.pinimg.com/564x/20/8d/3c/208d3c89cb8720fcf4c931f3a1cf6006.jpg')
        return img

MainApp().run()
