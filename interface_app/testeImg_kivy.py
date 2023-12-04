"""
from kivy.app import App
from kivy.uix.image import AsyncImage


class MainApp(App):
    def build(self):
        img = AsyncImage(
            source='https://supermariorun.com/assets/img/stage/mario03.png',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return img


if __name__ == '__main__':
    app = MainApp()
    app.run()

"""

from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        # Use o caminho absoluto da imagem no seu disco rígido
        img = Image(source=r'C:\Users\ander\Pictures\tigre.jpg',
                    size_hint=(1, .5),
                    pos_hint={'center_x': .5, 'center_y': .5})
        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()
