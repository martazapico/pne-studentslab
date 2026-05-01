import http.server
import socketserver
import termcolor
from pathlib import Path
from pygments.lexers import resource
import json
from P01.Seq1_new_version import Seq

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        from urllib.parse import parse_qs, urlparse
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)


        termcolor.cprint(self.requestline, 'green')
        try:
            # Open the form1.html file
            # Read the index from the file
            if path == '/' or path == '':
               contents = Path('html/index.html').read_text()
               self.send_response(200)


            elif path == '/listSpecies':
                limit = arguments.get('limit')[0]
                try:
                    limit = int(limit)
                except:
                    limit = None
                SERVER = 'rest.ensembl.org'
                ENDPOINT = '/info/species'
                PARAMS = '?content-type=application/json'
                REQUEST = ENDPOINT + PARAMS
                conn = http.client.HTTPConnection(SERVER)
                try:
                    conn.request("GET", REQUEST)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")

                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)
                species = response['species']
                n_species = len(species)
                if limit ==None or limit >= n_species:
                    options = range(n_species)
                else:
                    options = range(limit)
                names = ""
                for i in options:
                    number = species[i]
                    name = number['display_name']
                    names += f"<li> {name}"

                contents = Path('html/listSpecies.html').read_text()
                contents = contents.format(limit=limit, species=species, n_species=n_species, names=names)
                self.send_response(200)

            elif path == '/karyotype':
                species = arguments.get('species')[0]
                try:
                    species = str(species)
                except:
                    species = None
                SERVER = 'rest.ensembl.org'
                ENDPOINT = f'/info/assembly/{species}'
                PARAMS = '?content-type=application/json'
                REQUEST = ENDPOINT + PARAMS
                conn = http.client.HTTPConnection(SERVER)
                try:
                    conn.request("GET", REQUEST)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")

                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)
                karyotype = response['karyotype']
                if species ==None:
                    contents = Path('html/error.html').read_text()
                    self.send_response(200)
                else:
                    chrom = ""
                    for i in karyotype:
                        chrom += f"<br> {i}"

                    contents = Path('html/karyotype.html').read_text()
                    contents = contents.format(chrom=chrom)
                    self.send_response(200)

            elif path == '/chromosomeLength':
                species = arguments.get('species')[0]
                chromo = arguments.get('chromo')[0]
                try:
                    species = str(species)
                except:
                    species = None
                try:
                    chromo = str(chromo)
                except:
                    chromo = None
                SERVER = 'rest.ensembl.org'
                ENDPOINT = f'/info/assembly/{species}'
                PARAMS = '?content-type=application/json'
                REQUEST = ENDPOINT + PARAMS
                conn = http.client.HTTPConnection(SERVER)
                try:
                    conn.request("GET", REQUEST)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")

                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)
                karyotype = response['karyotype']

                if species ==None or chromo == None:
                    contents = Path('html/error.html').read_text()
                    self.send_response(200)
                else:

                    chrom_list = response['top_level_region']
                    for i in chrom_list:
                        name = i['name']
                        if name == chromo:
                            length = i['length']

                    contents = Path('html/chromosomeLength.html').read_text()
                    contents = contents.format(length=length)
                    self.send_response(200)

            elif path == '/geneLookup':
                try:
                    gene = arguments.get('gene')[0]
                    gene = str(gene)
                except:
                    gene = None

                SERVER = 'rest.ensembl.org'
                ENDPOINT = f'/xrefs/symbol/human/{gene}'
                PARAMS = '?content-type=application/json'
                REQUEST = ENDPOINT + PARAMS
                conn = http.client.HTTPConnection(SERVER)
                try:
                    conn.request("GET", REQUEST)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")

                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)
                id = response[0]['id']
                if gene == None:
                    contents = Path('html/error.html').read_text()
                    self.send_response(200)
                else:
                    contents = Path('html/geneLookup.html').read_text()
                    contents = contents.format(gene=gene, id=id)
                    self.send_response(200)

            elif path == '/geneSeq':
                try:
                    gene = arguments.get('gene')[0]
                    gene = str(gene)
                except:
                    gene = None

                SERVER = 'rest.ensembl.org'
                ENDPOINT = f'/xrefs/symbol/human/{gene}'
                PARAMS = '?content-type=application/json'
                REQUEST = ENDPOINT + PARAMS
                conn = http.client.HTTPConnection(SERVER)
                try:
                    conn.request("GET", REQUEST)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")

                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)
                id = response[0]['id']
                if gene == None:
                    contents = Path('html/error.html').read_text()
                    self.send_response(200)
                else:
                    SERVER = 'rest.ensembl.org'
                    ENDPOINT = f'/sequence/id/{id}'
                    PARAMS = '?content-type=application/json'
                    REQUEST = ENDPOINT + PARAMS
                    conn = http.client.HTTPConnection(SERVER)
                    try:
                        conn.request("GET", REQUEST)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    r1 = conn.getresponse()
                    print(f"Response received!: {r1.status} {r1.reason}\n")

                    data1 = r1.read().decode("utf-8")
                    response = json.loads(data1)
                    sequence = response["seq"]
                    contents = Path('html/geneSeq.html').read_text()
                    contents = contents.format(gene=gene, sequence=sequence)
                    self.send_response(200)
            elif path == '/geneInfo':
                try:
                    gene = arguments.get('gene')[0]
                    gene = str(gene)
                except:
                    gene = None

                SERVER = 'rest.ensembl.org'
                ENDPOINT = f'/xrefs/symbol/human/{gene}'
                PARAMS = '?content-type=application/json'
                REQUEST = ENDPOINT + PARAMS
                conn = http.client.HTTPConnection(SERVER)
                try:
                    conn.request("GET", REQUEST)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")

                data1 = r1.read().decode("utf-8")
                response = json.loads(data1)
                id = response[0]['id']
                if gene == None:
                    contents = Path('html/error.html').read_text()
                    self.send_response(200)
                else:
                    SERVER = 'rest.ensembl.org'
                    ENDPOINT = f'/lookup/id/{id}'
                    PARAMS = '?content-type=application/json'
                    REQUEST = ENDPOINT + PARAMS
                    conn = http.client.HTTPConnection(SERVER)
                    try:
                        conn.request("GET", REQUEST)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    r1 = conn.getresponse()
                    print(f"Response received!: {r1.status} {r1.reason}\n")

                    data1 = r1.read().decode("utf-8")
                    response = json.loads(data1)
                    start = response["start"]
                    end = response["end"]
                    chrom_name = response["seq_region_name"]

                    SERVER = 'rest.ensembl.org'
                    ENDPOINT = f'/sequence/id/{id}'
                    PARAMS = '?content-type=application/json'
                    REQUEST = ENDPOINT + PARAMS
                    conn = http.client.HTTPConnection(SERVER)
                    try:
                        conn.request("GET", REQUEST)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    r1 = conn.getresponse()
                    print(f"Response received!: {r1.status} {r1.reason}\n")

                    data1 = r1.read().decode("utf-8")
                    response = json.loads(data1)
                    bases = response["seq"]
                    s = Seq(bases)
                    length = s.len()

                    contents = Path('html/geneInfo.html').read_text()
                    contents = contents.format(gene=gene, start=start, end=end, length=length, id=id, chrom_name=chrom_name)
                    self.send_response(200)

            else:
                contents = Path('html/error.html').read_text()
                self.send_response(200)
        except TypeError:
            contents = Path('html/error.html').read_text()
            self.send_response(200)
        except http.client.InvalidURL:
            contents = Path('html/error.html').read_text()
            self.send_response(200)


        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

Handler = TestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)


    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
