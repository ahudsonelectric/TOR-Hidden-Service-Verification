import ConfigParser
import json
from sys import exit


class Config:
    _config_file = '/etc/hsverifyd.conf'

    _challenge_port = None
    _hidden_services = None
    _run_as = None
    _server_password = None

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(self._config_file))
        try:
            self._challenge_port = config.getint('network', 'challenge_port')
            self._hidden_services = json.loads(config.get('network', 'hidden_services'))
            self._server_password = config.get('network', 'tor_password')
            self._run_as = config.get('system', 'run_as')
        except ConfigParser.NoOptionError:
            print "Error reading config file."
            exit(2)

    def challenge_port(self):
        return self._challenge_port

    def hidden_services(self):
        return self._hidden_services

    def run_as(self):
        return self._run_as

    def server_password(self):
        return self._server_password
