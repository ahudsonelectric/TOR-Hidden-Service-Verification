import os
import sys

import stem
from stem.control import Controller


class HiddenService:
    _controller = None
    _config = None

    def __init__(self, config):
        self._config = config

        try:
            self._controller = Controller.from_port()
        except stem.SocketError as exc:
            print("Unable to connect to tor on port 9051: %s" % exc)
            sys.exit(1)

        try:
            self._controller.authenticate()
        except stem.connection.MissingPassword:
            print("Unable to authenticate, password is incorrect")
            sys.exit(1)
        except stem.connection.AuthenticationFailure as exc:
            print("Unable to authenticate: %s" % exc)
            sys.exit(1)

    def bind(self):
        # All hidden services have a directory on disk. Lets put ours in tor's data
        #  directory.
        hidden_service_dir = os.path.join(self._controller.get_conf('DataDirectory', '/tmp'), 'hello_world')
        # Create a hidden service where visitors of port 80 get redirected to local
        #  port 5000 (this is where Flask runs by default).
        print(" * Creating our hidden service in %s" % hidden_service_dir)
        result = self._controller.create_hidden_service(hidden_service_dir, 80, target_port=5000)
        # The hostname is only available when we can read the hidden service
        #  directory. This requires us to be running with the same user as tor.

        if result.hostname:
            print(" * Our service is available at %s, press ctrl+c to quit" % result.hostname)
        else:
            print(
                " * Unable to determine our service's hostname, probably due to being unable to read the hidden service directory")
        self._controller.close()
