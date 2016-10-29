import getpass
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
        self._gpg = gnupg.GPG(homedir=pwd.getpwuid(os.getuid()).pw_dir + '/' + self._config.gpg_keyring(),
                              keyring=self._config.gpg_pub_ring(),
                              secring=self._config.gpg_private_ring())

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
            print("No such file or directory: %s" % hostname_path)
            sys.exit(1)

        print ("Your domain is : %s" % host)

        # Get user data
        try:
            user = pwd.getpwnam(self._config.run_as())
        except KeyError:
            print ("User does not exists: %s" % self._config.run_as())
            sys.exit(1)

        # Read key password
        pw = getpass.getpass("Enter GPG password : ")

        # Write signature
        try:
            signature = self._gpg.sign(host, default_key=self._config.gpg_keyid(), clearsign=True, passphrase=pw)
            if (len(signature.__str__()) < 1):
                print ("The signing process has failed.")
                sys.exit(1)
        except:
            print ("The signing process has failed: exception raised")
            sys.exit(1)

        try:
            fd = open(signature_path, "w")
            fd.write(signature.__str__())
            fd.close()
            os.chown(signature_path, user[2], user[3])
        except:
            print ("Fail when create: %s" % signature_path)

        print ("The domain has been signed, now you can start the daemon")
        print ("Signed file path : %s" % signature_path)
        print ('Content of the signed file :')
        print signature.__str__()
