import os

from stem.control import Controller


class HiddenService:
    def start(self):
        with Controller.from_port() as controller:
            controller.authenticate()
            # All hidden services have a directory on disk. Lets put ours in tor's data
            #  directory.
            hidden_service_dir = os.path.join(controller.get_conf('DataDirectory', '/tmp'), 'hello_world')
            # Create a hidden service where visitors of port 80 get redirected to local
            #  port 5000 (this is where Flask runs by default).
            print(" * Creating our hidden service in %s" % hidden_service_dir)
            result = controller.create_hidden_service(hidden_service_dir, 80, target_port=5000)
            # The hostname is only available when we can read the hidden service
            #  directory. This requires us to be running with the same user as tor.

            if result.hostname:
                print(" * Our service is available at %s, press ctrl+c to quit" % result.hostname)
            else:
                print(
                    " * Unable to determine our service's hostname, probably due to being unable to read the hidden service directory")
