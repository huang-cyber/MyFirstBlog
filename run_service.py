#!C:\Program Files\Python39
# coding:utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from handlers import login_handler
from applications import application

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'hello')
        self.write(greeting + ', friendly user!')


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
