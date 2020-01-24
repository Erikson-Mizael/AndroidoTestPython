from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

import sys
sys.stderr = open('output.txt', 'w')
sys.stdout = sys.stderr

from kivy.logger import LoggerHistory
print('\n'.join([str(l) for l in LoggerHistory.history]))

class Gerenciador_De_Telas(ScreenManager):
    pass

class Tela_Principal(Screen):
    
    def lista_pastel(self,p):
        lista_pasteis = [('1','QUEIJO R$:10,00'),('2','QUEIJO R$:50,00'),('3','QUEIJO R$:10,0012'),('4','QUEIJO R$:10,00'),('4','QUEIJO R$:10,00'),
                         ('5','QUEIJO R$:20,00'),('6','QUEIJO R$:60,00'),('7','QUEIJO R$:10,0130'),
                         ('8','QUEIJO R$:330,00'),('9','QUEIJO R$:70,00'),('10','QUEIJO R$:1120,00'),
                         ('11','QUEIJO R$:130,00'),('12','QUEIJO R$:80,00'),('13','QUEIJO R$:130,00'),
                         ('14','QUEIJO R$:11,00'),('15','QUEIJO R$:90,00'),('16','QUEIJO R$:170,00'),
                         ('17','QUEIJO R$:144,00'),('18','QUEIJO R$:0,00'),('19','QUEIJO R$:1470,00'),
                         ('20','QUEIJO R$:110,00'),('21','QUEIJO R$:1,00'),('22','QUEIJO R$:1047,00'),
                         ('23','QUEIJO R$:120,00'),('24','QUEIJO R$:2,00'),('25','QUEIJO R$:710,00'),
                         ('26','QUEIJO R$:130,00'),('27','QUEIJO R$:3,00'),('28','QUEIJO R$:104,00'),
                         ('29','QUEIJO R$:140,00'),('30','QUEIJO R$:4,00'),('31','QUEIJO R$:107,00'),
                         ('32','QUEIJO R$:150,00'),('33','QUEIJO R$:0,500'),('34','QUEIJO R$:140,00'),
                         ('35','QUEIJO R$:160,00'),('36','QUEIJO R$:10,200'),('37','QUEIJO R$:17,00'),
                         ('38','QUEIJO R$:170,00'),('39','QUEIJO R$:10,001'),('40','QUEIJO R$:140,00'),
                         ('41','QUEIJO R$:180,00'),('42','QUEIJO R$:10,002'),('43','QUEIJO R$:1470,00'),
                         ('44','QUEIJO R$:190,00'),('45','QUEIJO R$:10,010'),('46','QUEIJO R$:1470,00'),
                         ('47','QUEIJO R$:20,00'),('48','QUEIJO R$:10,001'),('49','QUEIJO R$:140,00'),
                         ('50','QUEIJO R$:30,00'),('51','QUEIJO R$:10,0011'),('52','QUEIJO R$:170,00'),
                         ('53','QUEIJO R$:40,00'),('54','QUEIJO R$:10,010'),('55','QUEIJO R$:140,00'),]
        pasteis = dict(lista_pasteis)
        if p in pasteis:
            pasteis[p]
            return pasteis[p]
    
    def pedido_numero(self,e,a,n):
        
        pedido = self.ids['pedido'].text
        pedido = pedido[:]
        
        if len(pedido) <= 3:
            self.ids['pedido'].text += n
        
        if e == '1':
            self.ids['escolha'].text = pedido
            trans = int(pedido)
            if trans < 56 and trans != 0 :
                trastr = str(trans)
                pastel = Tela_Principal().lista_pastel(trastr)
                self.ids['pastel'].text = pastel
            else:
                trastr = str(trans)
                self.ids['escolha'].text =  'Pedido:\n'+trastr+'\nnao encontrado\n1/55'
        if a == '1':
            self.ids['pedido'].text = pedido[:-1]
        
        
        
class Construtor(App):
    def build(self):
        return Gerenciador_De_Telas()
    
if __name__ == "__main__":
    Construtor().run()
