from collections import defaultdict

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

# dictionary of all created exchanges
_exchanges = defaultdict(Exchange)

# return the exchange instance assiciated with a given name
def get_exchange(name):
    return _exchanges[name]

# example os using a task

class Task:
    def send(self, msg):
        return msg

task_a = Task()
task_b = Task()

# Example of getting an exchange
exc = get_exchange('name')

# example of subscribing tasks to it
exc.attach(task_a)
exc.attach(task_b)

# example of sending messages
exc.send('msg1')
exc.send('msg2')

# example of un subscribing
exc.detach(task_a)
exc.detach(task_b)