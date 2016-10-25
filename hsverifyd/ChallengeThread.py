import json
from threading import Thread

import gnupg


class ChallengeThread(Thread):
    _conn = None
    _config = None
    _gpg = None

    def __init__(self, conn, config):
        Thread.__init__(self)
        self._conn = conn
        self._config = config
        self._gpg = gnupg.GPG(gnupghome=self._config.gpgring())

    def run(self):
        # Get data from client
        data = json.loads(self._conn.recv(2048))
        # Check valid json
        if not data.has_key("challenge"):
            self._conn.send('{"status":"false"}')
            self._conn.close()
            return False
        # TODO: Resolve challenge
        # Respond to user
        self._conn.send('{"status":"true"}')
        self._conn.close()
