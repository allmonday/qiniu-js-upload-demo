# coding: utf-8
"""
js客户端上传图片, 需要后端提供uptoken, 由/uptoken接口提供, access_key, secret_key自备
"""
import tornado.ioloop
import tornado.web
from qiniu import Auth, put_file, etag
import qiniu.config

access_key = '<your access_key>'
secret_key = '<your secret_key>'


class BaseHandler(tornado.web.RequestHandler):
    pass


class MainHandler(BaseHandler):
    def get(self):
        self.render("upload.html")


class TokenHandler(BaseHandler):
    def get(self):
        q = qiniu.Auth(access_key, secret_key)
        bucket_name = '<your bucket_name>'
        token = q.upload_token(bucket_name)
        self.write({'uptoken': token})


def make_app():
    return tornado.web.Application([
        (r"/uptoken", TokenHandler),
        (r"/", MainHandler), 
    ], debug=True, 
       template_path='template',
       static_path='static')


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
