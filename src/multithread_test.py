import threading

class FirstThread (threading.Thread):
    def run (self):
        while True:
            print 'first'

class SecondThread (threading.Thread):
    def run (self):
        while True:
            print 'second'

FirstThread().start()
SecondThread().start()

