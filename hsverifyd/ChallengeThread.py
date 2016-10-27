import json
from BaseHTTPServer import BaseHTTPRequestHandler


class ChallengeThread(BaseHTTPRequestHandler):
    gpg_keyid = None
    signed_file_path = None

    def do_POST(self):


        # Get data from client
        with self.rfile as query:
            json_data = query.read().replace('\n', '')

        data = json.loads(json_data)

        self.send_response(200)
        self.send_header('Content-type', "application/json")
        self.end_headers()

        # If request is challenge
        if data.has_key("challenge"):
            f = open(self.signed_file_path)
            self.wfile.write(f.read())
            f.close()
            return

        # If request is Unknown
        response = '{"status":"false"}'

        # If request is HELLO
        if data.has_key("hello") and data["hello"] == "hsverifyd":
            response = '{"gpg":"' + self.gpg_keyid + '"}'

        self.wfile.send(response)

        return
