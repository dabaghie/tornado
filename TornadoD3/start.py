import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
# from pycket.session import SessionManager
from tornado.options import define, options

define("port", default=890, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # session = SessionManager(self)
        # if session.get("LoggedIn","No") != "No" :
        #     session.set('info', {"Ln":"Alavi","Fn":"ali"})
        #     session.set('_id','1233444')
            self.render('index.html',UN= "hello")
        # else :
        #     session.set('LoggedIn', {"_id":"12222222","name":"ali"})
        #     self.render('index.html',UN="U Are Not Logged In..")





class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
                # if session.get()
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,difference=noun3)


# Your app launch code here..
class MedxApplication(tornado.web.Application):

    def __init__(self):
        # self.db = ["Medex"]
        handlers = [(r'/', IndexHandler), (r'/poem', PoemPageHandler)]
        settings = dict(
            debug=True,
            cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path= os.path.join(os.path.dirname(__file__), "static")


        )
        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()


    http_server = tornado.httpserver.HTTPServer(MedxApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()