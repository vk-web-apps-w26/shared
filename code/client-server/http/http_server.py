#!/usr/bin/env python3
"""
HTTP server that handles addition requests.
Endpoint: GET /add?num1=X&num2=Y
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class AdditionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests."""
        # Parse the URL
        parsed_path = urlparse(self.path)
        
        # Check if the path is /add
        if parsed_path.path == '/add':
            # Parse query parameters
            params = parse_qs(parsed_path.query)
            
            try:
                # Get num1 and num2 from query parameters
                num1 = float(params.get('num1', [None])[0])
                num2 = float(params.get('num2', [None])[0])
                
                # Calculate sum
                result = num1 + num2
                
                # Prepare response
                response = {
                    'status': 'success',
                    'num1': num1,
                    'num2': num2,
                    'result': result
                }
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
                print(f"Calculated: {num1} + {num2} = {result}")
                
            except (TypeError, ValueError):
                # Send error response
                response = {
                    'status': 'error',
                    'message': 'Invalid parameters. Use /add?num1=X&num2=Y'
                }
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
        else:
            # Unknown endpoint
            response = {
                'status': 'error',
                'message': 'Unknown endpoint. Use /add?num1=X&num2=Y'
            }
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def log_message(self, format, *args):
        """Override to customize log messages."""
        print(f"Request: {args[0]}")

def main():
    HOST = '127.0.0.1'
    PORT = 8000
    
    server = HTTPServer((HOST, PORT), AdditionHandler)
    print(f"HTTP Server running on http://{HOST}:{PORT}")
    print(f"Example: http://{HOST}:{PORT}/add?num1=5&num2=3")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        server.shutdown()

if __name__ == "__main__":
    main()
