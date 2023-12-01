"""from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button(text='Fala Galera!',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5},
                      on_press=self.on_press_button)

    def on_press_button(self, instance):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
"""

'''O Kivy também fornece uma linguagem de design chamada KV, que você pode usar com seus aplicativos Kivy. A linguagem KV permite separar o design da interface e a lógica do aplicativo.

Isso segue o princípio da separação de interesses e faz parte do padrão de arquitetura Model-View-Controller.

Você pode atualizar o exemplo anterior para usar a linguagem KV. Confira! '''

from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()

