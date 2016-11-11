import pika, sys
from pika import spec

# build conn
credentials = pika.PlainCredentials('guest', 'guest')
conn_params = pika.ConnectionParameters('localhost',
                                        credentials=credentials)

conn_broker = pika.BlockingConnection(conn_params)

# get channel
channel = conn_broker.channel()
channel.confirm_delivery()


# get exchange
channel.exchange_declare(exchange='hello_exchange',
                         type='direct',
                         passive=False,
                         durable=True,
                         auto_delete=False)

# create messages
msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = 'text/plain'

# publish
if channel.basic_publish(body=msg,
                      exchange='hello_exchange',
                      properties=msg_props,
                      routing_key='hola'):
    print 'confimed'
else:
    print 'lost'

channel.close()