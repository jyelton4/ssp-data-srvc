from os import curdir,sep,path
from http.server import BaseHTTPRequestHandler, HTTPServer

from routes.main import routes

class API(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if self.path == '/':
            content_type = 'text/html'
        elif self.path == '/data':
            content_type = 'json'
        else:
            content_type = "text/plain"
        try:
            self.respond(content_type)
        except IOError:
            self.send_error(400, 'Bad Request')

    def handle_http(self, content_type):
        if self.path in routes:
            status = 200
            route_content = routes[self.path]
            file_path = curdir + sep + route_content
    
            content_type = content_type
            response_content = open(file_path)
            response_content = response_content.read()
        else:
            status = 404
            content_type = "text/plain"
            response_content = "404 Not Found"

        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.end_headers()
        return bytes(response_content, 'UTF-8')

    def respond(self, content_type):
        content = self.handle_http(content_type)
        self.wfile.write(content)

def run(HOST, PORT):
    print('http server is starting...')
    server_address = (HOST, PORT)
    with HTTPServer(server_address, API) as httpd:
        try:
            print('serving at port', PORT)
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.socket.close()