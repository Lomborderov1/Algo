from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from numpy import multiply, spacing 


class ScrButton(Button):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen 
        self.direction = direction
        self.goal = goal 
    def  on_press(self):
        self.scrern.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScr(screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout(orientation="vertical", padding=8, spacing=8)
        h1 = BoxLayout()
        txt = Label(text="Выбери экран")
        v1.add_widget(ScrButton(self, direction='down', goal='first', ext='1'))
        v1.add_widget(ScrButton(self, direction='left', goal='second', text='2'))
        v1.add_widget(ScrButton(self, direction='up', goal='third', text='3'))
        h1.add_widget(txt)
        h1.add_widget(v1)
        self.add_widget(h1)

class FirstScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout(orientation='vertical',size_hint=(.5, .5), pos_hint={'center_x' : 0.5, 'center': 0.5})
        btn = Button(text= 'Выбор: 1', size_hint=(.5,1), pos_hint={'left': 0})
        btn_back = ScrButton(self,direction= 'up',goal= 'main',text= "Назад",size_hint=(.5,1), pos_hint={'right': 1})
        v1.add_widget(btn)
        v1.add_widget(btn_back)
        self.add_widget(v1)
'''
class SecondScr(screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        v1 = BoxLayout(orientation='vertical')
        self.txt = Label(text= 'Выбор: 2')
        v1.add_widget(self.txt)
        
        h1_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl1 = Label(text='Введите пароль:', height= 'right')
        self.input = TextInput(multiline = False)'''

My.app()