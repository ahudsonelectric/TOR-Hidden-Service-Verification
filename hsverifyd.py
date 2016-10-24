#!/usr/bin/python

import argparse

__application__ = "hsverifyd"
__version__ = "0.1.0"
__release__ = __application__ + '/' + __version__
__author__ = "Juan Ezquerro LLanes"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', '-s', help='Start Server', action="store_true")
    parser.add_argument('--stop', '-k', help='Stop Server', action="store_true")
    parser.add_argument('--restart', '-r', help='Restart Server', action="store_true")
    args = parser.parse_args()

    if args.start:
        pass
    elif args.stop:
        pass
    elif args.restart:
        pass
    else:
        parser.print_help()
