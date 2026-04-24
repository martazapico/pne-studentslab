import http.client
import json
import termcolor
def get_genes():
    genes = {}
    species = "homo_sapiens"
    gene_list = ["FRAT1", "ADA", "FXN", "RNU6-269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3", "KDR", "ANK2"]

    num_genes = len(gene_list)

    text1 = f"Dictionary of Genes!\nThere are {num_genes} genes in the dictionary:\n"
    for name in gene_list:

        SERVER = 'rest.ensembl.org'
        ENDPOINT = f'/xrefs/symbol/{species}/{name}'
        PARAMS = '?content-type=application/json'
        URL = SERVER + ENDPOINT + PARAMS
        REQUEST = ENDPOINT + PARAMS


        # Connect with the server
        conn = http.client.HTTPConnection(SERVER)

        # -- Send the request message, using the GET method. We are
        # -- requesting the main page (/)
        try:
            conn.request("GET", REQUEST)
        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()

        # -- Read the response message from the server
        r1 = conn.getresponse()

        # -- Read the response's body
        data1 = r1.read().decode("utf-8")

        # -- Create a variable with the data,
        # -- form the JSON received
        response = json.loads(data1)

        for key, value in response[0].items():
            if key == "id":
                ID = value
        genes[name] = ID
    return genes, text1
if __name__ == "__main__":
    genes, text1 = get_genes()
    print(text1)

    for key, value in genes.items():
        termcolor.cprint(f"{key}:", 'green', end='')
        print(f" --> {value}")

    gene_list = []
    for key, value in genes.items():
        gene_list.append(f"{key}:{value}")

