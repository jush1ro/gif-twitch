#!/usr/bin/env/python
import BaseHTTPServer, SimpleHTTPServer
import ssl

cert_file = "./localhost.pem"
key_file = "./localhost-key.pem"

class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

httpd = BaseHTTPServer.HTTPServer(
    ('', 8080),
    RequestHandler
)

httpd.socket = ssl.wrap_socket(
    httpd.socket,
    server_side=True,
    keyfile=key_file,
    certfile=cert_file
)

httpd.serve_forever()