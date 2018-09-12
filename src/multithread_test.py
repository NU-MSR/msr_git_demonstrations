import threading
import time

class FirstThread (threading.Thread):
    def run (self):
        while True:
            print 'first'

class SecondThread (threading.Thread):
    def run (self):
        while True:
            print 'second'

f1 = FirstThread()
f1.daemon = True
f2 = SecondThread()
f2.daemon = True
f1.start()
f2.start()

while True:
    time.sleep(1)
