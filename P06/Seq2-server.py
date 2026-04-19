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

        elif path == '/get':
            sequence = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA", "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT", "GGGTGTGTGTTAGTGTGCGTGCTTGCTTGTGTGTGGAAGAAACCAACAGGGTTCACGCTG", "CGGCTCCCGCGGCTGCAGGCGCGCGGCTAGAGTGCCTGGCGGGCTCCGGCTTCCGCGTCC", "ATCCCGCAGCCGCTGTCGGGTCCGTGCCGGCGAGGATGGCTCCGGGGCGCCGCCGCCTCC"]
            number = arguments.get('n')
            number = int(number[0])
            seq = sequence[number]
            contents =  Path('html/get.html').read_text()
            contents = contents.format(number=number, seq=seq)
            self.send_response(200)

        elif path == '/gene':
            gene = arguments.get('name')
            gene = str(gene[0])
            text = Path(f'../S04/sequences/{gene}.txt').read_text()
            a = text.split("\n")
            body = a[1::]
            gene_text = "<br>".join(body)
            contents =  Path('html/gene.html').read_text()
            contents = contents.format(gene=gene, gene_text=gene_text)
            self.send_response(200)
        elif path == '/operation':
            sequence = arguments.get('sequence')
            sequence = str(sequence[0])
            sequence = sequence.upper()
            operation = arguments.get('base')
            operation = str(operation[0])

            list_bases = {'A' : 0, 'T' : 0, 'G' : 0, 'C' : 0}
            length = len(sequence)
            for letter in sequence:
                if letter in list_bases:
                    list_bases[letter] += 1
            bases = ""
            for base, numb in list_bases.items():
                if length > 0:
                    percentage = (numb / length) * 100
                    percentage = round(percentage, 1)
                else:
                    percentage = 0
                bases += f"{base}: {numb} ({percentage}%)<br>"
            if operation == 'Info':
                result = f"Sequence: {sequence}<br> Total length: {length}<br> {bases}"
            elif operation == 'Comp':
                comp_bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
                result = ""
                for i in sequence:
                    if i in comp_bases:
                        result += comp_bases[i]
                    else:
                        result += i
            elif operation == 'Rev':
                result = sequence[::-1]

            contents =  Path('html/operation.html').read_text()
            contents = contents.format(sequence=sequence, operation=operation, result=result)
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
