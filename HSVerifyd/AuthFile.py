import os.path
import pwd
import sys

import gnupg

from HSVerifyd.ConfigLoader import Config
from HSVerifyd.HiddenService import HiddenService
from HSVerifyd.LogWriter import Logger


class AuthFile:
    def __init__(self):
        self._log = Logger()
        self._config = Config()
        self._hs = HiddenService(self._log)
        self._gpg = gnupg.GPG()

    def sign(self):
        # Start hidden services
        if not self._hs.connect(self._config.server_password()):
            print ("Unable to connect to Tor server")
            self._log.close()
            sys.exit(1)

        # Setup paths
        data_dir = self._hs.get_data_dir()
        hostname_path = data_dir + "/hostname"
        signature_path = data_dir + "/HSVerifyd.asc"

        # Create the service url if not exists
        if not os.path.isfile(data_dir):
            self._hs.set_own(self._config.challenge_port())
            self._hs.remove_own()

        # We no longer need this
        self._hs.close()
        self._log.close()

        # Read hostname
        try:
            with open(hostname_path, 'r') as hostname:
                host = hostname.read().replace('\n', '')
        except IOError:
            print("No such file or directory: " + hostname_path)
            sys.exit(1)

        # Get user data
        try:
            user = pwd.getpwnam(self._config.run_as())
        except KeyError:
            print ("User does not exists: %s" % self._config.run_as())
            sys.exit(1)

        # Write signature
        try:
            self._gpg.sign(host, output=signature_path)
            os.chown(signature_path, user[2], user[3])
        except:
            print ("Fail when create: %s" % signature_path)
            sys.exit(1)

        print ("The domain has been signed, now you can start the daemon")
