from time import sleep
from kivy.lib import osc

service = 3000

def some_api_callback(message, *args):
   print("got a message! %s" % message)

if __name__ == '__main__':
    osc.init()
    oscid = osc.listen(ipAddr='127.0.0.1', port=service)
    osc.bind(oscid, some_api_callback, '/some_api')

    while True:
        osc.readQueue(oscid)
        sleep(.1)
