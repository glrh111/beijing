import pika
credentials = pika.PlainCredentials('guest', 'guest')
conn_params = pika.ConnectionParameters('localhost',
                                        credentials=credentials)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
channel.exchange_declare(exchange='hello_exchange',
                         type='direct',
                         passive=False,
                         durable=True,
                         auto_delete=False)
channel.queue_declare(queue='hello_queue')
channel.queue_bind(queue='hello_queue',
                   exchange='hello_exchange',
                   routing_key='hola')

def msg_consumer(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if 'quit' == body:
        channel.basic_cancel(consumer_tag='hello_consumer')
        channel.stop_consuming()
    else:
        print body
    return

channel.basic_consume(msg_consumer,
                      queue='hello_queue',
                      consumer_tag='hello_consumer')
channel.start_consuming()