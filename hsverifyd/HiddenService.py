import os
import sys

import stem
from stem.control import Controller


class HiddenService:
    _controller = None

    def connect(self, tor_password):
        try:
            self._controller = Controller.from_port()
        except stem.SocketError as exc:
            print("Unable to connect to tor on port 9051: %s" % exc)
            sys.exit(1)

        try:
            self._controller.authenticate(password=tor_password)
        except stem.connection.MissingPassword:
            print("Unable to authenticate, missing password")
            sys.exit(1)
        except stem.connection.AuthenticationFailure as exc:
            print("Unable to authenticate: %s" % exc)
            sys.exit(1)

    def bind(self, hidden_services, challenge_port):
        hidden_service_dir = os.path.join(self._controller.get_conf('DataDirectory', '/tmp'), 'hsverifyd')
        self._controller.create_hidden_service(hidden_service_dir, challenge_port, target_port=5000)
        for service in hidden_services:
            self._controller.create_hidden_service(hidden_service_dir, service[0], target_port=service[1])
        self._controller.close()
