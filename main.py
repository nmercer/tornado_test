import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html", title="Main...", lister=[1,2,3,4])

    def post(self):
        self.set_header("Content-Type", "text/plain")
        #self.write(self.get_argument("message"))
	self.write(self.request.files)
	print self.request

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Test!")

class PrintHandler(tornado.web.RequestHandler):
    def get(self, printer):
         self.write(printer)

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        raise tornado.web.HTTPError(403)

class InitHandler(tornado.web.RequestHandler):
    def initialize(self, foo, bar):
	print foo + bar
	print test

    def get(self):
	self.write(test)

class RedirectHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/test', permanent=True)

class CookiesHandler(tornado.web.RequestHandler):
    def get(self):
       if not self.get_cookie("cook"):
            self.set_cookie("cook", "All the cookies for you!")
            self.write("No cookies for you!")
       else:
            self.write(self.get_cookie("cook"))

test = {"foo": 1, "bar": 2}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/test/", TestHandler),
    (r"/printit/([0-9A-Za-z]+)", PrintHandler),
    (r"/error/", ErrorHandler),
    (r"/init/", InitHandler, test),
    (r"/redirect", RedirectHandler),
    (r"/cookies", CookiesHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
