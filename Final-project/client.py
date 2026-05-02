import http.client
import json

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


print("LIST SPECIES:")
response = send_request("/listSpecies?limit=10&json=1")
print("CONTENT:")
print(response)


print("\nKARYOTYPE:")
response = send_request("/karyotype?species=mouse&json=1")
print("CONTENT:")
print(response)


print("\nCHROMOSOME LENGTH:")
response = send_request("/chromosomeLength?species=mouse&chromo=18&json=1")
print("CONTENT:")
print(response)


print("\nGENE LOOKUP:")
response = send_request("/geneLookup?gene=FRAT1&json=1")
print("CONTENT:")
print(response)


print("\nGENE SEQUENCE:")
response = send_request("/geneSeq?gene=FRAT1&json=1")
print("CONTENT:")
print(response)