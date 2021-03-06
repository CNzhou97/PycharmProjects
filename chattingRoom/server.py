'''
	tornado 的核心IO循环模块， 封装了linux的epoll debian的kqueue, 是tornado高效的基础
'''
import tornado.ioloop
import tornado.httpserver
import config
from application import Application

if __name__ == "__main__":
    app = Application()
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.bind(config.options.get("port"))
    # 默认是创建和cpu的核心数个数一致的子进程
    httpserver.start()

    #IOLoop IO循环的类：内部继承了epoll实现高并发
    tornado.ioloop.IOLoop.current().start()