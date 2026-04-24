import http.client
import json
import termcolor
from P01.Seq1_new_version import Seq
from e2 import get_genes
genes, text1 = get_genes()

for gene, ID in genes.items():
    SERVER = 'rest.ensembl.org'
    ENDPOINT = f'/sequence/id/{ID}'
    PARAMS = '?content-type=application/json'
    URL = SERVER + ENDPOINT + PARAMS
    REQUEST = ENDPOINT + PARAMS

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

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

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    # -- Create a variable with the data,
    # -- form the JSON received
    response = json.loads(data1)


    termcolor.cprint(f"Gene:", 'green', end=" ")
    print(gene)
    termcolor.cprint(f"Description:", 'green', end=" ")
    print(response["desc"])

    bases = response["seq"]
    s = Seq(bases)
    length = s.len()
    b_count = s.count()
    freq_base = s.gene_processing()
    termcolor.cprint(f"Total length:", 'green', end=" ")
    print(length)

    for base, numb in b_count.items():
        percentage = (numb / length) * 100
        percentage = round(percentage, 1)
        c = f"{base}: {numb} ({percentage}%)"
        print(c)
    termcolor.cprint(f"Most frequent Base:", 'green', end=" ")
    print(freq_base)

