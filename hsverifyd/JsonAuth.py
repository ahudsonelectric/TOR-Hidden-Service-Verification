import os.path
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

        file = self._hs.get_data_dir() + "/hostname"

        # Create the url service if not exists yet
        if not os.path.isfile(file):
            self._hs.set_own(self._config.challenge_port())
            self._hs.remove_own()

        self._hs.close()

        try:
            with open(file, 'r') as hostname:
                host = hostname.read().replace('\n', '')
        except IOError:
            self._log.error("No such file or directory: " + file)
            self._log.close()
            sys.exit(1)

        self._log.close()
        return '{"url":"' + host + '"}'
