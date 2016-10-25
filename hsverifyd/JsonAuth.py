import sys

from hsverifyd.ConfigLoader import Config
from hsverifyd.HiddenService import HiddenService
from hsverifyd.LogWriter import Logger


class JsonAuth:
    def __init__(self):
        self._log = Logger()
        self._config = Config()
        self._hs = HiddenService(self._log)

    def get(self):
        # Start hidden services
        if not self._hs.connect(self._config.server_password()):
            self._log.close()
            sys.exit(1)

        with open(self._hs.get_data_dir() + "/hsverifyd.signed", 'r') as hostname:
            host = hostname.read().replace('\n', '')
        self._log.close()
        self._hs.close()
        return '{"url":"' + host + '"}'
