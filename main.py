import server
from ssp import fetch_data

if __name__ == '__main__':
    fetch_data()

    HOST, PORT = "localhost", 8080

    server.run(HOST, PORT)