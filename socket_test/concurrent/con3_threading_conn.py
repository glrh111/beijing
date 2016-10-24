from Queue import Queue
from threading import Thread
import time

# a thread that produces data
def producer(out_q):
    data = 1
    while True:
        data += 1
        out_q.put(data)
        # process
        print 'Put ', data
        time.sleep(2.5)

def consumer(in_q):
    while True:
        data = in_q.get()
        # process
        print 'Get ', data

q = Queue()

t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()