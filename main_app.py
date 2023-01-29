from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

import instructions

name = ""
age = 7
p1,p2,p3 = 0,0,0

class Window1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = Label(text = instructions.txt_instruction, color =(0.5, 0.5, 0.5, 1))
        self.mainLayout = BoxLayout(orientation = 'vertical')
        self.nameLayout = BoxLayout()
        self.ageLayout = BoxLayout()
        self.textName = Label(text = "Введите ім'я:")
        self.textAge = Label(text = 'Введіть ваш вік:')
        self.inputName = TextInput()
        self.inputAge = TextInput()
        self.nameLayout.add_widget(self.textName)
        self.nameLayout.add_widget(self.inputName)
        self.ageLayout.add_widget(self.textAge)
        self.ageLayout.add_widget(self.inputAge)
 
        self.button = Button(text = 'Почати')
        self.button.on_press = self.triger 

        self.mainLayout.add_widget(self.text)
        self.mainLayout.add_widget(self.nameLayout)
        self.mainLayout.add_widget(self.ageLayout)
        self.mainLayout.add_widget(self.button)
 
        self.add_widget(self.mainLayout)
    
    def triger(self):
        global name
        global age 
        name = self.inputName.text
        age = self.inputAge.text
        age = self.checkpoint(age)
        if age:
            if age > 6:
                self.manager.current = '. . .'
            else:    
                self.textAge.text = "Введіть число більше ніж 6"

    def checkpoint(self, value):
        try:
            value = int(value)
            return value
        except:    
            self.textAge.text = "Введіть число"        




class Ruffie(App):
    def build(self):
        build=ScreenManager()
        build.add_widget(Window1(name = 'Valera'))
        return build

app=Ruffie()
app.run()