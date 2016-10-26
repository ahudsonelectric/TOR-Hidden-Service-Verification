import json
from threading import Thread


class ChallengeThread(Thread):
    _conn = None
    _config = None

    def __init__(self, conn, config):
        Thread.__init__(self)
        self._conn = conn
        self._config = config

    def run(self):
        # Get data from client
        data = json.loads(self._conn.recv(2048))

        # Check valid json
        if data.has_key("hello") and data["hello"] == "hsverifyd":
            self._conn.send('{"gpg":"' + self._config.gpg_keyid() + '"}')
        elif data.has_key("challenge"):
            with open(self._config.signed_file(), 'r') as signedfile:
                signature = signedfile.read().replace('\n', '')
            self._conn.send(signature)
        else:
            self._conn.send('{"status":"false"}')

        self._conn.close()
