from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from os import path

Builder.load_file(path.dirname(path.abspath(__file__)) + '/../data/quadis.kv')

class FileSelectionScreen(Screen):
    def enter_text(self, file_path):
        if path.isfile(file_path) and file_path.endswith('.csv'):
            pass

        else:
            Clock.schedule_once(lambda dt:
                                setattr(self.file_path_input, 'focus', True), 0)
            self.file_path_input.text = ''

            if not path.isfile(file_path):
                self.failure_message.text = 'file doesn\'t exist'
            else:
                self.failure_message.text = 'invalid file format'

class CardCheckingScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(FileSelectionScreen(name='Select File'))

class QuadisApp(App):

    def build(self):
        return sm


def gui():
    QuadisApp().run()
