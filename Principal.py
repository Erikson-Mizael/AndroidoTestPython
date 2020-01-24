import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class GerenciadorDeTelas(ScreenManager):
    pass
class MenuInicial(Screen):
    pass
class TelaPersonal(Screen):
    pass
class Estudo(Screen):
    def soma(self, a, b):
        return a + b
p1 = Estudo()
print('Resultado ', p1.soma(3013, 120010))


class Construtor(App):
    def build(self):
        return GerenciadorDeTelas()
if __name__ == '__main__':
    Construtor().run()