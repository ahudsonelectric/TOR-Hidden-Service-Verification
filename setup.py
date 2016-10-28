from distutils.core import setup

setup(
    # Application name:
    name="hsverifyd",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Juan Ezquerro LLanes",
    author_email="arrase@gmail.com",

    # Packages
    packages=["HSVerifyd"],

    # Details
    url="https://github.com/arrase/TOR-Hidden-Service-Verification",

    description="A way to fight against service impersonations in the TOR network",

    data_files=[
        ('/etc/init.d', ['etc/init.d/hsverifyd']),
        ('/etc/', ['etc/hsverifyd.conf']),
        ('/usr/sbin', ['hsverifyd'])
    ]
)
