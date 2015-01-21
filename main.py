import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp

class TestApp(App):
    use_kivy_settings = False
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })
    def build_settings(self, settings):
        jsondata = """[
    { "type": "title",
      "title": "Test application" },

    { "type": "options",
      "title": "My first key",
      "desc": "Description of my first key",
      "section": "section1",
      "key": "key1",
      "options": ["value1", "value2", "another value"] },

    { "type": "numeric",
      "title": "My second key",
      "desc": "Description of my second key",
      "section": "section1",
      "key": "key2" }
     ]"""

        settings.interface.menu.width = dp(100)
        settings.add_json_panel('Test application',
            self.config, data=jsondata)

if __name__ == '__main__':
    TestApp().run()
