from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000

# Function to block requests
def block_request(self):
    self.send_response(403)
    self.send_header("content-type", "application/json")
    self.end_headers()
    self.wfile.write(b'{"status": "blocked", "reason": "blocked by firewall rule"}')
    print(f"[!] Blocked request to {self.path} from {self.client_address}")

# Function to allow requests
def handle_request(self):
    self.send_response(200)
    self.send_header("content-type", "application/json")
    self.end_headers()
    self.wfile.write(b'{"status": "allowed"}')
    print(f"[+] Allowed request to {self.path} from {self.client_address}")

# Inspect requests for the malicious path
def inspect_request(self):
    # Block if the request path contains /tomcatwar.jsp
    if "/tomcatwar.jsp" in self.path.lower():
        block_request(self)
    else:
        handle_request(self)

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        inspect_request(self)

    def do_POST(self):
        inspect_request(self)

if __name__ == "__main__":        
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)
