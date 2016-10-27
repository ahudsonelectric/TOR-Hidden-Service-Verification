import json
from BaseHTTPServer import BaseHTTPRequestHandler


class ChallengeThread(BaseHTTPRequestHandler):
    gpg_keyid = None
    signed_file_path = None

    def do_POST(self):
        # Default response
        response = '{"status":"false"}'

        # Get data from client
        with self.rfile as query:
            json_data = query.read().replace('\n', '')

        data = json.loads(json_data)

        self.send_response(200)
        self.end_headers()

        # Check valid json
        if data.has_key("hello") and data["hello"] == "hsverifyd":
            response = '{"gpg":"' + self.gpg_keyid + '"}'
        elif data.has_key("challenge"):
            with open(self.signed_file_path, 'r') as signedfile:
                response = signedfile.read().replace('\n', '')

        self.wfile.send(response)

        return
