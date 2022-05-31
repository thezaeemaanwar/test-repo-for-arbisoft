from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = "localhost"
serverPort = 8080
MyJSON = json.dumps(
    {'id': 'hyueHiu83u8-3irfj', 'name': 'Zaeema Anwar', 'age': '21'})


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(MyJSON.encode())


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server Started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    print("Server Stopping ...")
    webServer.server_close()
    print("Server Stopped")
