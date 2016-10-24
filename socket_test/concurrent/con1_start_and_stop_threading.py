import time
from threading import Thread

def countdown(n):
    while n > 0:
        print 'T-minus', n
        n -= 1
        time.sleep(5)

t = Thread(target=countdown, args=(10,))
# t.daemon = True
t.start()

while t.is_alive():
    print 'Still alive'
    time.sleep(1)