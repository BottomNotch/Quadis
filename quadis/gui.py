from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.clock import Clock
from os import path
from quadis import main

Builder.load_file(path.dirname(path.abspath(__file__)) + '/../data/quadis.kv')
Builder.load_file(path.dirname(path.abspath(__file__)) + '/../data/custom_file_chooser.kv')

csv_path = None

class QuadisTextInput(TextInput):
    pass

class ConfirmationPopup(RelativeLayout):
    pass

class OkPopup(RelativeLayout):
    pass

class FileSelectionScreen(Screen):
    def set_path(self):
        return path.expanduser('~')

    def select_file(self, file_path):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Scan Card'
        self.manager.get_screen('Scan Card').file_name.text = file_path

class CardCheckingScreen(Screen):
    def disable_buttons(self, checkin_card, mod_card, add_card, remove_card):
        self.checkin_card_button.disabled = checkin_card
        self.mod_card_button.disabled = mod_card
        self.add_card_button.disabled = add_card
        self.remove_card_button.disabled = remove_card

    def display_card_info(self, card_num):
        card_dict = main.card_info(self.file_name.text, card_num)

        self.card_num_label.text = '[b]number:[/b] ' + card_dict['card_num']
        self.name_label.text = '[b]name:[/b] ' + card_dict['name']
        self.under_13_label.text = '[b]children 12 and under:[/b] ' + card_dict['under_13']
        self.under_18_label.text = '[b]children over the age of 12:[/b] ' + card_dict['under_18']
        self.under_60_label.text = '[b]adults under the age of 60:[/b] ' + card_dict['under_60']
        self.over_59_label.text = '[b]adults age 60 and older:[/b] ' + card_dict['over_59']
        self.zip_code_label.text = '[b]zip code:[/b] ' + card_dict['zip']
        self.last_used_label.text = '[b]card last used on:[/b] ' + card_dict['last_used_date']

    def clear_card_info(self):
        self.card_num_label.text = ''
        self.name_label.text = ''
        self.under_13_label.text = ''
        self.under_18_label.text = ''
        self.under_60_label.text = ''
        self.over_59_label.text = ''
        self.zip_code_label.text = ''
        self.last_used_label.text = ''

    def check_card(self, card_num, update_card):
        result = main.check_card(self.file_name.text, card_num, update_card=update_card)

        if result is 0:
            self.card_check_results.text = 'card not found'
            self.card_check_results.color = [1, 0, 0, 1]
            self.disable_buttons(True, True, False, True)

        elif result is 1:
            if update_card is False:
                self.card_check_results.text = 'card found and has not been used today'
                self.card_check_results.color = [0, 1, 0, 1]
                self.disable_buttons(False, False, True, False)
            else:
                self.card_check_results.text = 'card checked in'
                self.card_check_results.color = [0, 1, 0, 1]
                self.disable_buttons(True, False, True, False)

        elif result is 2:
            self.card_check_results.text = 'card found and has been used today'
            self.card_check_results.color = [1, 0, 0, 1]
            self.disable_buttons(True, False, True, False)

        else:
            self.card_check_results.text = 'unknown error'
            self.card_check_results.color = [1, 0, 0, 1]
            self.disable_buttons(True, True, True, True)

        if result is 1 or result is 2:
            self.display_card_info(card_num)

        else:
            self.clear_card_info()

    def add_card_screen(self):
        s = self.manager.get_screen('Add or Modify Card')
        s.card_num_input.text = self.card_num_input.text
        s.card_num_input.disabled = True
        s.file_name.text = self.file_name.text
        s.add_card_mode = True
        s.change_card_mode = False
        s.name_input.foucs = True

        self.manager.transition.direction = 'down'
        self.manager.current = 'Add or Modify Card'

    def change_card_screen(self):
        card_dict = main.card_info(self.file_name.text, self.card_num_input.text)
        s = self.manager.get_screen('Add or Modify Card')
        s.card_num_input.text = self.card_num_input.text
        s.card_num_input.disabled = False
        s.name_input.text = card_dict['name']
        s.under_13_input.text = card_dict['under_13']
        s.under_18_input.text = card_dict['under_18']
        s.under_60_input.text = card_dict['under_60']
        s.over_59_input.text = card_dict['over_59']
        s.zip_code_input.text = card_dict['zip']
        s.last_used_input.text = card_dict['last_used_date']

        s.file_name.text = self.file_name.text
        s.add_card_mode = False
        s.change_card_mode = True
        s.card_num_input.focus = True

        self.manager.transition.direction = 'up'
        self.manager.current = 'Add or Modify Card'

class CardAddAndModScreen(Screen):
    _popup = None
    add_card_mode = False
    change_card_mode = False

    def card_dict_builder(self):
        card_dict = dict()
        card_dict['card_num'] = self.card_num_input.text
        card_dict['name'] = self.name_input.text
        card_dict['under_13'] = self.under_13_input.text
        card_dict['under_18'] = self.under_18_input.text
        card_dict['under_60'] = self.under_60_input.text
        card_dict['over_59'] = self.over_59_input.text
        card_dict['zip'] = self.zip_code_input.text
        card_dict['last_used_date'] = self.last_used_input.text
        return card_dict

    def add_card(self):
        card_dict = self.card_dict_builder()
        result = main.add_card(self.file_name.text, card_dict)

        content = OkPopup()

        if result is 0:
            title = 'success'
            content.dialog.text = 'card {0} was added successfully'.format(
                card_dict['card_num'])

        elif result is 2:
            title = 'failure'
            content.dialog.text = '{0} is not a valid date/date format'.format(
                self.last_used_input.text)

        else:
            title = 'failure'
            content.dialog.text = 'an unknown error has occurred'

        self._popup.dismiss()
        self._popup = Popup(title=title, content=content,
                                size_hint=(0.35, 0.35))
        if result is 0:
            self._popup.content.ok.on_press = self.close_screen

        else:
            self._popup.content.ok.on_press = self._popup.dismiss

        self._popup.open()

    def change_card(self):
        card_dict = self.card_dict_builder()
        result = main.change_card(self.file_name.text,
                               self.manager.get_screen('Scan Card').card_num_input.text,
                               card_dict)
        content = OkPopup()

        if result is 0:
            title = 'success'
            content.dialog.text = 'all information was changed successfully'

        elif result is 2:
            title = 'failure'
            content.dialog.text = 'the new card number {0} already exists'.format(
                self.card_num_input.text)

        elif result is 3:
            title = 'failure'
            content.dialog.text = '{0} is not a valid date/date format'.format(
                self.last_used_input.text)

        else:
            title = 'failure'
            content.dialog.text = 'an unknown error has occurred'

        self._popup.dismiss()
        self._popup = Popup(title=title, content=content,
                                size_hint=(0.35, 0.35))
        if result is 0:
            self._popup.content.ok.on_press = self.close_screen

        else:
            self._popup.content.ok.on_press = self._popup.dismiss

        self._popup.open()

    def close_screen(self):
        self.card_num_input.text = ''
        self.name_input.text = ''
        self.under_13_input.text = ''
        self.under_18_input.text = ''
        self.under_60_input.text = ''
        self.over_59_input.text = ''
        self.zip_code_input.text = ''
        self.last_used_input.text = ''

        self._popup.dismiss()
        s = self.manager.get_screen('Scan Card')
        s.card_num_input.text = ''
        s.clear_card_info()
        s.disable_buttons(True, True, True, True)
        self.manager.transition.direction = 'up'
        self.manager.current = 'Scan Card'

    def confirm_popup(self, add_card=False, change_card=False, cancel=False):
        if add_card:
            dialog_text = 'are you sure want to add this card?'
            on_press = self.add_card

        elif change_card:
            dialog_text = 'are you sure you want to change this card?'
            on_press = self.change_card

        elif cancel:
            dialog_text = 'are you sure you want to cancel this operation?'
            on_press = self.close_screen

        else:
            dialog_text = 'something went wrong, these buttons won\'t do anything'

        content = ConfirmationPopup()
        self._popup = Popup(title='Are You Sure?', content=content,
                            size_hint=(0.35, 0.35))
        self._popup.content.dialog.text = dialog_text
        self._popup.content.yes.on_press = on_press
        self._popup.content.no.on_press = self._popup.dismiss
        self._popup.open()

sm = ScreenManager()
sm.add_widget(FileSelectionScreen(name='Select File'))
sm.add_widget(CardCheckingScreen(name='Scan Card'))
sm.add_widget(CardAddAndModScreen(name='Add or Modify Card'))

class QuadisApp(App):

    def build(self):
        return sm


def gui():
    QuadisApp().run()
