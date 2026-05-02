import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'


def send_request(endpoint):
    print(f"\nREQUEST: {endpoint}")

    conn = http.client.HTTPConnection(SERVER, PORT)

    try:
        conn.request("GET", endpoint)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    response = conn.getresponse()

    print(f"Response received!: {response.status} {response.reason}\n")

    data = response.read().decode("utf-8")
    conn.close()

    return json.loads(data)


print(f"\nConnecting to server: {SERVER}:{PORT}\n")


termcolor.cprint("1) LIST SPECIES:", 'green')
response = send_request("/listSpecies?limit=10&json=1")
print("CONTENT:")
for key, value in response.items():
    if key != "species":
        termcolor.cprint(f"{key}:", 'blue', f"{value}")
    else:
        termcolor.cprint(f"{key}:", 'blue')
        for i in value:
            print(f"\t{i}")


termcolor.cprint("\n2) KARYOTYPE:", 'green')
response = send_request("/karyotype?species=mouse&json=1")
print("CONTENT:")
for key, value in response.items():
    termcolor.cprint(f"{key}:", 'blue')
    for i in value:
        print(f"\t{i}")


termcolor.cprint("\n3) CHROMOSOME LENGTH:", 'green')
response = send_request("/chromosomeLength?species=mouse&chromo=18&json=1")
print("CONTENT:")
for key, value in response.items():
    termcolor.cprint(f"{key}:", 'blue', f"{value}")


termcolor.cprint("\n4) GENE LOOKUP:", 'green')
response = send_request("/geneLookup?gene=ADA&json=1")
print("CONTENT:")
for key, value in response.items():
    termcolor.cprint(f"{key}:", 'blue', f"{value}")


termcolor.cprint("\n5) GENE SEQUENCE:", 'green')
response = send_request("/geneSeq?gene=FRAT1&json=1")
print("CONTENT:")
for key, value in response.items():
    termcolor.cprint(f"{key}:", 'blue', f"{value}")


termcolor.cprint("\n6) GENE INFORMATION:", 'green')
response = send_request("/geneInfo?gene=FXN&json=1")
print("CONTENT:")
for key, value in response.items():
    termcolor.cprint(f"{key}:", 'blue', f"{value}")


termcolor.cprint("\n7) GENE CALCULATIONS:", 'green')
response = send_request("/geneCalc?gene=U5&json=1")
print("CONTENT:")
for key, value in response.items():
    if key != "base calculations":
        termcolor.cprint(f"{key}:", 'blue', f"{value}")
    else:
        termcolor.cprint(f"{key}:", 'blue', )
        print(f"{value}")


termcolor.cprint("\n8) GENE LIST:", 'green')
response = send_request("/geneList?chromo=20&start=44584896&end=44652252&json=1")
print("CONTENT:")
for key, value in response.items():
    if key != "names":
        termcolor.cprint(f"{key}:", 'blue', f"{value}")
    else:
        termcolor.cprint(f"{key}:", 'blue', )
        print(f"{value}")
