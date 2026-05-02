import http.server
import http.client
import socketserver
import termcolor
import json
from pathlib import Path
from pygments.lexers import resource
from P01.Seq1_new_version import Seq
from json_functions import list_species_json, karyotype_json, chromosome_length_json, gene_lookup_json, gene_seq_json, gene_info_json, gene_calc_json, gene_list_json


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        from urllib.parse import parse_qs, urlparse
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        json_request = arguments.get('json')


        termcolor.cprint(self.requestline, 'green')
        try:
            if path == '/' or path == '':
               contents = Path('html/index.html').read_text()
               content_type = 'text/html'
               self.send_response(200)


            elif path == '/listSpecies':
                try:
                    limit = arguments.get('limit')[0]
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

                if json_request != None and json_request[0] == "1":
                    contents = list_species_json(limit, n_species, species, options)
                    content_type = 'application/json'
                    error_code = 200
                    self.send_response(error_code)
                else:
                    contents = Path('html/listSpecies.html').read_text()
                    contents = contents.format(limit=limit, species=species, n_species=n_species, names=names)
                    content_type = 'text/html'
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
                    content_type = 'text/html'
                    self.send_response(200)
                else:
                    chrom = ""
                    for i in karyotype:
                        chrom += f"<br> {i}"

                    if json_request != None and json_request[0] == "1":
                        contents = karyotype_json(karyotype)
                        content_type = 'application/json'
                        error_code = 200
                        self.send_response(error_code)
                    else:
                        contents = Path('html/karyotype.html').read_text()
                        contents = contents.format(chrom=chrom)
                        content_type = 'text/html'
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


                if species ==None or chromo == None:
                    contents = Path('html/error.html').read_text()
                    content_type = 'text/html'
                    self.send_response(200)
                else:

                    chrom_list = response['top_level_region']
                    for i in chrom_list:
                        name = i['name']
                        if name == chromo:
                            length = i['length']

                    if json_request != None and json_request[0] == "1":
                        contents = chromosome_length_json(length)
                        content_type = 'application/json'
                        error_code = 200
                        self.send_response(error_code)
                    else:
                        contents = Path('html/chromosomeLength.html').read_text()
                        contents = contents.format(length=length)
                        content_type = 'text/html'
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
                    content_type = 'text/html'
                    self.send_response(200)
                else:

                    if json_request != None and json_request[0] == "1":
                        contents = gene_lookup_json(gene, id)
                        content_type = 'application/json'
                        error_code = 200
                        self.send_response(error_code)
                    else:
                        contents = Path('html/geneLookup.html').read_text()
                        contents = contents.format(gene=gene, id=id)
                        content_type = 'text/html'
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
                    content_type = 'text/html'
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

                    if json_request != None and json_request[0] == "1":
                        contents = gene_seq_json(gene, sequence)
                        content_type = 'application/json'
                        error_code = 200
                        self.send_response(error_code)

                    else:
                        contents = Path('html/geneSeq.html').read_text()
                        contents = contents.format(gene=gene, sequence=sequence)
                        content_type = 'text/html'
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
                    content_type = 'text/html'
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

                    if json_request != None and json_request[0] == "1":
                        contents = gene_info_json(gene, start, end, length, id, chrom_name)
                        content_type = 'application/json'
                        error_code = 200
                        self.send_response(error_code)
                    else:
                        contents = Path('html/geneInfo.html').read_text()
                        contents = contents.format(gene=gene, start=start, end=end, length=length, id=id, chrom_name=chrom_name)
                        content_type = 'text/html'
                        self.send_response(200)

            elif path == '/geneCalc':
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
                    content_type = 'text/html'
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
                    bases = response["seq"]
                    s = Seq(bases)
                    length = s.len()
                    b_count = s.count()

                    c = ""
                    d = ""
                    for base, numb in b_count.items():
                        percentage = (numb / length) * 100
                        percentage = round(percentage, 1)
                        c += f"{base}: {numb} ({percentage}%)<br>"
                        d += f"\t{base}: {numb} ({percentage}%)\n"
                    base_calc = c
                    bases = d

                    if json_request != None and json_request[0] == "1":
                        contents = gene_calc_json(gene, bases, length)
                        content_type = 'application/json'
                        error_code = 200
                        self.send_response(error_code)

                    else:
                        contents = Path('html/geneCalc.html').read_text()
                        contents = contents.format(base_calc=base_calc, length=length, gene=gene)
                        content_type = 'text/html'
                        self.send_response(200)

            elif path == '/geneList':
                try:
                    chromo = arguments.get('chromo')[0]
                    chromo = str(chromo)
                    start = arguments.get('start')[0]
                    start = int(start)
                    end = arguments.get('end')[0]
                    end = int(end)

                except:
                    start = None
                    chromo = None
                    end = None

                SERVER = 'rest.ensembl.org'
                ENDPOINT = f'/overlap/region/human/{chromo}:{start}-{end}'
                PARAMS = '?content-type=application/json'
                EXTRA = ';feature=gene'
                REQUEST = ENDPOINT + PARAMS + EXTRA
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
                names = ""
                name_list = ""
                for i in response:
                    name = i['external_name']
                    names += f"<li>{name}</li>"
                    name_list += f"\t{name}\n"

                if chromo == None or start == None or end == None:
                    contents = Path('html/error.html').read_text()
                    content_type = 'text/html'
                    self.send_response(200)
                else:
                    if json_request != None and json_request[0] == "1":
                        contents = gene_list_json(chromo, start, end, name_list)
                        content_type = 'application/json'
                        error_code = 200
                        self.send_response(error_code)
                    else:
                        contents = Path('html/geneList.html').read_text()
                        contents = contents.format(chromo=chromo, start=start, end=end, names=names)
                        content_type = 'text/html'
                        self.send_response(200)
            else:
                contents = Path('html/error.html').read_text()
                self.send_response(200)
        except TypeError:
            contents = Path('html/error.html').read_text()
            content_type = 'text/html'
            self.send_response(200)
        except http.client.InvalidURL:
            contents = Path('html/error.html').read_text()
            content_type = 'text/html'
            self.send_response(200)


        # Define the content-type header:
        self.send_header('Content-Type', content_type)
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
