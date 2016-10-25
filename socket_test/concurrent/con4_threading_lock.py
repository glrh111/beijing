from threading import Lock, Thread
import time

class SharedCounter(object):

    def __init__(self, init=0):
        self._value = init
        self._lock = Lock()

    def incr(self, delta=1):
        with self._lock:
            self._value += delta

    def decr(self, delta=1):
        with self._lock:
            self._value -= delta

counter = SharedCounter(4)

def test1():
    while 1:    
        counter.incr(2)
        print 'test1 ', counter._value
        time.sleep(1)

def test2():
    while 1:    
        counter.decr(2)
        print 'test2 ', counter._value
        time.sleep(1)

t1 = Thread(target=test1)
t2 = Thread(target=test2)
t1.start()
t2.start()

