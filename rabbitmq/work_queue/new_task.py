#!/usr/bin/env python
import pika
import click

@click.command()
@click.argument('message', type=str)
def main(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='hello_exchange_fanout',
                             type='fanout')
    # channel.queue_declare(queue='hello_queue')
    channel.basic_publish(exchange='hello_exchange_fanout',
                          routing_key='hello',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2   # make message persistent
                          ))
    print(" [x] Sent '{}'".format(message))
    connection.close()

if __name__ == '__main__':
    main()