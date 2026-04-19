import http.server
import socketserver
import termcolor
from pathlib import Path

from pygments.lexers import resource



# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        from urllib.parse import parse_qs, urlparse
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Open the form1.html file
        # Read the index from the file
        if path == '/' or path == '':
           contents = Path('html/index.html').read_text()
           self.send_response(200)


        elif path == '/ping':
            contents = f"""<!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <title>PING OK</title>
          </head>
          <body>
           <h1> PING OK! </h1>
              <p> The SEQ2 server is running... </p>
              <a href="http://localhost:8080/">Main page</a>
          </body>
        </html>
        """
            self.send_response(200)
        else:
            contents = Path('html/error.html').read_text()
            self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
