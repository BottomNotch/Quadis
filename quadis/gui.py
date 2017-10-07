from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from os import path
from quadis import main

Builder.load_file(path.dirname(path.abspath(__file__)) + '/../data/quadis.kv')

csv_path = None

class QuadisTextInput(TextInput):
    pass

class FileSelectionScreen(Screen):
    def enter_text(self, file_path):
        if path.isfile(file_path) and file_path.endswith('.csv'):
            self.manager.current = 'Scan Card'
            self.manager.get_screen('Scan Card').file_name.text = file_path 

        else:
            Clock.schedule_once(lambda dt:
                                setattr(self.file_path_input, 'focus', True), 0)
            self.file_path_input.text = ''

            if not path.isfile(file_path):
                self.failure_message.text = 'file doesn\'t exist'
            else:
                self.failure_message.text = 'invalid file format'

class CardCheckingScreen(Screen):
    def disable_buttons(self, checkin_card, mod_card, add_card, remove_card):
        self.checkin_card_button.disabled = checkin_card
        self.mod_card_button.disabled = mod_card
        self.add_card_button.disabled = add_card
        self.remove_card_button.disabled = remove_card
        
    def check_card(self, card_num, update_card):
        result = main.check_card(self.file_name.text, card_num, update_card=update_card)

        if result is 0:
            self.card_check_results.text = 'card not found'
            self.disable_buttons(True, True, False, True)

        elif result is 1:
            if update_card is False:
                self.card_check_results.text = 'card found and has not been used today'
                self.disable_buttons(False, False, True, False)
            else:
                self.card_check_results.text = 'card checked in'
                self.disable_buttons(True, False, True, False)

        elif result is 2:
            self.card_check_results.text = 'card found and has been used today'
            self.disable_buttons(True, False, True, False)

        else:
            self.card_check_results.text = 'unknown error'
            self.disable_buttons(True, True, True, True)

sm = ScreenManager()
sm.add_widget(FileSelectionScreen(name='Select File'))
sm.add_widget(CardCheckingScreen(name='Scan Card'))

class QuadisApp(App):

    def build(self):
        return sm


def gui():
    QuadisApp().run()
