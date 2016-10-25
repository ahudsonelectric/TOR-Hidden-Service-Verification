#!/usr/bin/python

import argparse

import sys

from hsverifyd.Daemonize import Daemonize
from hsverifyd.JsonAuth import JsonAuth

__application__ = "hsverifyd"
__version__ = "0.1.0"
__release__ = __application__ + '/' + __version__
__author__ = "Juan Ezquerro LLanes"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', help='Start Server', action="store_true")
    parser.add_argument('--stop', help='Stop Server', action="store_true")
    parser.add_argument('--restart', help='Restart Server', action="store_true")
    parser.add_argument('--json', help='Echo auth string to be signed', action="store_true")
    args = parser.parse_args()

    if args.json:
        auth = JsonAuth()
        print auth.get()
        sys.exit(0)

    daemon = Daemonize()

    if args.start:
        daemon.start()
    elif args.stop:
        daemon.stop()
    elif args.restart:
        daemon.restart()
    else:
        parser.print_help()
