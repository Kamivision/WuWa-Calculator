import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label




# Create app build and run
class WuWaApp(App):
    def build(self):
        return Grid()

if __name__ == "__main__":
    WuWaApp().run()