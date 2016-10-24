#! /usr/bin/env python

import os.path
import textwrap

import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options

from tornado.options import define, options
define('port', default=8080, help='run on this port', type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')


class ReverseHandler(tornado.web.RequestHandler):
    def get(self, text):
        self.write(text[::-1])


class FillHandler(tornado.web.RequestHandler):
    def get(self):
        # parse
        text = self.get_argument('text', 'cao')
        length = self.get_argument('length', 10)
        # fill
        self.write(textwrap.fill(text, int(length)))


class MusicHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        name = self.get_argument('name', 'Unknown')
        length = self.get_argument('length', '10s')
        country = self.get_argument('country', 'China')
        self.render('music.html', name=name, length=length, country=country)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/reverse/(\w+)', ReverseHandler),
            (r'/fill', FillHandler),
            (r'/music', MusicHandler)
        ],
        template_path=os.path.join(
            os.path.dirname(__file__),
            'templates'
        ),
        static_path=os.path.join(
            os.path.dirname(__file__),
            'static'
        ),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()