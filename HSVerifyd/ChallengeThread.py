import json
from BaseHTTPServer import BaseHTTPRequestHandler


class ChallengeThread(BaseHTTPRequestHandler):
    gpg_keyid = None
    signed_file_path = None
    hostname = None

    def do_POST(self):
        # Response object
        response = {}

        # Get data from client
        request_sz = int(self.headers["Content-length"])
        request_str = self.rfile.read(request_sz) + " "
        data = json.loads(request_str)

        # If request is challenge
        if data.has_key("challenge") and data["challenge"] == "HSVerifyd":
            response['host'] = self.hostname
            response['gpg_id'] = self.gpg_keyid
            f = open(self.signed_file_path)
            response['signature'] = f.read()
            f.close()
        else:
            # If request is Unknown
            response['status'] = False

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(response))

        return
