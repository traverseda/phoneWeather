import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix import settings
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.utils import platform
import service
from kivy.clock import Clock
from kivy.lib import osc
from kivy.lang import Builder
activityport = 3001

def some_api_callback(message, *args):
   print("got a message! %s" % message)

kv = '''
Button:
    text: 'push me!'
'''

class TestApp(App):
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })
    def build_settings(self, settings):
        jsondata = """[
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

    def build(self):
        if platform == 'android':
            from android import AndroidService
            service = AndroidService('my pong service', 'running')
            service.start('service started')
            self.service = service

        osc.init()
        oscid = osc.listen(ipAddr='127.0.0.1', port=activityport)
        osc.bind(oscid, some_api_callback, '/some_api')
        Clock.schedule_interval(lambda *x: osc.readQueue(oscid), 0)
#    def on_config_change(config, section, key, value):
#        print(configchange)

    def close_settings(self,*args, **kwargs):
        super(TestApp, self).close_settings(*args, **kwargs)
        self.stop()


    def on_start(self):
        self.open_settings()
if __name__ == '__main__':
    TestApp().run()

