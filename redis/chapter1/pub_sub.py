import redis
from threading import Thread
import time

conn = redis.StrictRedis(host='redis')

def publisher():
    time.sleep(1)
    for i in range(10):
        conn.publish('channel1', 'wocaoni-{}'.format(i))
        time.sleep(1)

def subscribe():
    t1 = Thread(target=publisher)
    t1.start()

    subscriber = conn.pubsub()
    subscriber.subscribe(['channel1'])
    for message in subscriber.listen():
        print message

if __name__ == '__main__':
    subscribe()