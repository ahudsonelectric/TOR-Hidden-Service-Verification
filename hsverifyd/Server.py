from flask import Flask


class Server:
    _app = None

    def __init__(self):
        self._app = Flask(self)

    @_app.route('/')
    def index(self):
        return "<h1>Hi Grandma!</h1>"

    def run(self):
        self._app.run()
