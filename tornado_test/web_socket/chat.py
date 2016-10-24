#! /usr/bin/env python

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid

from tornado.options import define, options
define('port', default=8080, help='application run on this port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', MainHandler),
            (r'/chatsocket', ChatSocketHandler)
        ]
        settings = dict(
            cookie_secret='TODO:GENERAYE SELF COOKIE',
            template_path=os.path.join(
                os.path.dirname(__file__),
                'templates'
            ),
            static_path=os.path.join(
                os.path.dirname(__file__),
                'static'
            ),
            xsrf_cookies=True
        )
        super(Application, self).__init__(handlers=handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', messages=ChatSocketHandler.cache)


class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 200

    def get_compression_options(self):
        # Non-None enables compression with default options
        return {}

    def open(self):
        ChatSocketHandler.waiters.add(self)

    def on_close(self):
        ChatSocketHandler.waiters.remove(self)

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        logging.info('sending message to %d waiters', len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
            except Exception:
                logging.error('Error sending message', exc_info=True)

    def on_message(self, message):
        logging.info('got message %r', message)
        parsed = tornado.escape.json_decode(message)
        message_body = parsed.get('body', '')
        if message_body:
            chat = {
                'id': str(uuid.uuid4()),
                'body': message_body
            }
            chat['html'] = tornado.escape.to_basestring(
                self.render_string('message.html', message=chat)
            )
            ChatSocketHandler.update_cache(chat)
            ChatSocketHandler.send_updates(chat)
        else:
            logging.warning('Error message empty')

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()