from http.server import BaseHTTPRequestHandler, HTTPServer
import led

class LEDRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/led-strip/on':
            led.start_rainbow()
            self.send_response(200)
            self.end_headers()
            print("LED strip switched on")
        elif self.path == '/led-strip/off':
            led.stop_rainbow()
            self.send_response(200)
            self.end_headers()
            print("LED strip switched off")
        else:
            self.send_response(404)
            self.end_headers()
            print("Unknown path")

def run(server_class=HTTPServer, handler_class=LEDRequestHandler, port=8888):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    print(f"Server started on port {port}...")

if __name__ == '__main__':
    run()