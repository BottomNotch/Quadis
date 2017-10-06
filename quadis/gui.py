from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from os import path

Builder.load_file(path.dirname(path.abspath(__file__)) + '/../data/quadis.kv')

class FileSelectionScreen(Screen):
    def enter_text(self, file_path):
        if path.isfile(file_path):
            if file_path.endswith('.csv'):
                pass
            else:
                self.failure_message.text = 'invalid file format, please provide a csv file'

        else:
            self.failure_message.text = 'file doesn\'t exist'

class CardCheckingScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(FileSelectionScreen(name='Select File'))

class QuadisApp(App):

    def build(self):
        return sm


def gui():
    QuadisApp().run()
