import json
from BaseHTTPServer import BaseHTTPRequestHandler


class ChallengeThread(BaseHTTPRequestHandler):
    gpg_keyid = None
    signed_file_path = None

    def do_POST(self):
        # Get data from client
        request_sz = int(self.headers["Content-length"])
        request_str = self.rfile.read(request_sz) + " "
        data = json.loads(request_str)

        self.send_response(200)

        # If request is challenge
        if data.has_key("challenge") and data["challenge"] == "HSVerifyd":
            f = open(self.signed_file_path)
            response = f.read()
            f.close()
        elif data.has_key("hello") and data["hello"] == "HSVerifyd":
            response = '{"gpg":"' + self.gpg_keyid + '"}'
        else:
            # If request is Unknown
            response = '{"status":"false"}'

        self.end_headers()
        self.wfile.write(response)

        return
