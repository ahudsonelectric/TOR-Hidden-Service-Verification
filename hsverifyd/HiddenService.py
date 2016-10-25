import os

import stem
from stem.control import Controller


class HiddenService:
    _controller = None
    _log = None

    def __init__(self, log):
        self._log = log

    def connect(self, tor_password):
        try:
            self._controller = Controller.from_port()
        except stem.SocketError as exc:
            self._log.error("Unable to connect to tor on port 9051: %s" % exc)
            return False

        try:
            self._controller.authenticate(password=tor_password)
        except stem.connection.MissingPassword:
            self._log.error("Unable to authenticate, missing password")
            return False
        except stem.connection.AuthenticationFailure as exc:
            self._log.error("Unable to authenticate: %s" % exc)
            return False

        return True

    def bind(self, hidden_services, challenge_port):
        hidden_service_dir = os.path.join(self._controller.get_conf('DataDirectory', '/tmp'), 'hsverifyd')
        self._controller.create_hidden_service(hidden_service_dir, 111, target_port=challenge_port)
        for service in hidden_services:
            self._controller.create_hidden_service(hidden_service_dir, service[1], target_port=service[0])
        self._controller.close()
        return hidden_service_dir
