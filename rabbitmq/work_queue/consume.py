#!/usr/bin/env python
import pika
import time
import click

def callback(ch, method, properties, body):
    click.secho(" [x] Received %r" % body, bg='green', fg='magenta')
    time.sleep(body.count('.'))
    click.secho(' [x] Done\n', fg='red')
    ch.basic_ack(delivery_tag = method.delivery_tag)

@click.command()
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()

    result = channel.queue_declare()

    print result

    channel.queue_bind(exchange='hello_exchange_fanout',
                       queue=result.method.queue,
                       routing_key='hello')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue=result.method.queue)
                          #no_ack=True

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()