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

        dir = self._hs.get_data_dir() + "/hostname"

        try:
            with open(dir, 'r') as hostname:
                host = hostname.read().replace('\n', '')
        except IOError:
            self._log.error("No such file or directory: " + dir)
            self._log.close()
            self._hs.remove_own()
            self._hs.close()
            sys.exit(1)

        self._log.close()
        self._hs.remove_own()
        self._hs.close()
        return '{"url":"' + host + '"}'
