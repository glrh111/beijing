from threading import Thread, Event
import time

def countdown(n, started_event):
    print 'count down starting'
    started_event.set()
    while n > 0:
        print 'T-minus ', n
        n -= 1
        time.sleep(2)

# create the event object that will be used to signal startup
started_event = Event()

# launch the thread and pass the startup thread
print 'Launching coundown ...'
t = Thread(target=countdown, args=(5, started_event))
t.start()

# wait for the thread to start
started_event.wait()
print 'countdown is running'