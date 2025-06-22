from http.server import BaseHTTPRequestHandler, HTTPServer
import led

class LEDRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/led-strip/on':
            led.start_rainbow()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'LED strip switched ON')
        elif self.path == '/led-strip/off':
            led.stop_rainbow()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'LED strip switched OFF')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def do_POST(self):
        self.send_response(405)
        self.end_headers()
