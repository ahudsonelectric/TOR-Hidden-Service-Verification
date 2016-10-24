import ConfigParser
import os.path
from sys import exit


class Config:
    _config_file = '/etc/hsverifyd.conf'
    _log = None

    port = None
    run_as = None

    def __init__(self, log):
        self._log = log
        self._check_conf_file()
        self._load()

    def _check_conf_file(self):
        if not os.path.isfile(self._config_file):
            self._log.error("File " + self._config_file + " does not exist")
            exit(2)

    def _load(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(self._config_file))
        try:
            self.port = config.getint('network', 'port')
            self.run_as = config.get('system', 'run_as')
        except ConfigParser.NoOptionError:
            self._log.error("Error reading config file.")
            exit(2)

