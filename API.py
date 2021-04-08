from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import json

host = "localhost"
port = 8080

names = ["Tom Cruise", "David Balne", "Abigail Anderson", "Joel Miller", "Oscar Isaac", "Sarah Taylor", "Janet Mason", "Catherine Jones", "Alice Evans", "Ella Wright", "Logan Brown"]
adresses = ["12 Waterloo Road","69 Waterfront Plaza","104 Apex Street","76 Grethound Gardens","32 Trynadmere Court","88 Province Islands","72 District Lane","66 Pointer Close","48 Aztec Drive"," 9000 Penny Lane"]
post_codes = ["IP11 7QE","RH19 2QP","NE16 5SN","CT21 4HJ","EH14 1HH","DL13 1QX","BS10 6UA","WV13 1DO","TS14 6BG","SG4 9DA"]

class OrderToSend:

    def __init__(self):
        random_index = random.randint(0, 10 - 1)
        name = names[random_index]
    
        self.name = f'{names[random_index]}'
        self.address = f'{adresses[random_index]}'
        self.post_code = f'{post_codes[random_index]}'
        self.email = f'{name.replace(" ", "")}@gmail.com'
        self.item_id = random.randint(1, 10)



class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        orders = [vars(OrderToSend()), vars(OrderToSend()), vars(OrderToSend()), vars(OrderToSend())]
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(orders), encoding='utf8'))


if __name__ == "__main__":
    local_server = HTTPServer((host, port), Server)
    print("Server started...")
    try:
        local_server.serve_forever()
    except KeyboardInterrupt:
        pass
    local_server.server_close()
    print("Server closed...")
