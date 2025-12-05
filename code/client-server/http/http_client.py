#!/usr/bin/env python3
"""
HTTP client that sends addition requests to the server.
"""
import urllib.request
import urllib.parse
import json

def main():
    # Server configuration
    HOST = '127.0.0.1'
    PORT = 8000
    
    # Get numbers from user
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    # Build URL with query parameters
    params = urllib.parse.urlencode({'num1': num1, 'num2': num2})
    url = f"http://{HOST}:{PORT}/add?{params}"
    
    try:
        # Send HTTP GET request
        print(f"\nSending request to: {url}")
        
        with urllib.request.urlopen(url) as response:
            # Read and parse JSON response
            data = response.read().decode('utf-8')
            result = json.loads(data)
            
            if result['status'] == 'success':
                print(f"\nServer response:")
                print(f"  {result['num1']} + {result['num2']} = {result['result']}")
            else:
                print(f"\nError: {result['message']}")
                
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        try:
            error_data = json.loads(e.read().decode('utf-8'))
            print(f"Message: {error_data.get('message', 'Unknown error')}")
        except:
            pass
    except urllib.error.URLError as e:
        print(f"Error: Could not connect to server. Make sure the server is running.")
        print(f"Details: {e.reason}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
