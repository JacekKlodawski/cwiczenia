from http.server import HTTPServer,BaseHTTPRequestHandler

class HodowlaZajecy(BaseHTTPRequestHandler):
    html = """ 
    <html><body>
    <a href="google.pl">Google</a>
    </body></html>
    """
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(self.html.encode('utf-8'))

Serwer = HTTPServer(('localhost',8000),HodowlaZajecy)
Serwer.serve_forever()

