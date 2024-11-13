import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty



# Create app build and run
class WuWaApp(App):
    def build(self):
        return Grid()

if __name__ == "__main__":
    WuWaApp().run()