import socket
from sys import exit

from hsverifyd.ChallengeThread import ChallengeThread


class Server():
    _log = None
    _port = None
    _tcpServer = None

    threads = []

    def __init__(self, log, port):
        self._log = log
        self._port = port

    def run(self):
        try:
            self._tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._tcpServer.bind(("127.0.0.1", self._port))
        except socket.error:
            self._log.error("There was an error when trying to bind the server")
            exit(2)
        finally:
            self._log.info("Waiting for connections ...")

        while True:
            self._tcpServer.listen(4)
            (conn, (ip, port)) = self._tcpServer.accept()
            newthread = ChallengeThread(conn)
            newthread.start()
            self.threads.append(newthread)
