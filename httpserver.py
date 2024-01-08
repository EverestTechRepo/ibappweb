from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        return super().end_headers()

    def do_OPTIONS(self):           
        self.send_response(200, "ok")       
        self.end_headers()

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8000), CORSHTTPRequestHandler)
    httpd.serve_forever()