from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import json

host = "localhost"
port = 8080
n_orders = 5
n_people = 10


class OrderToSend:
    # class variable: records last id, gets incremented in init method
    last_id = 0

    def __init__(self):
        self.order_id = self.last_id
        self.name = "Owen"
        self.address = "Owen Drive"
        self.item = "Owen item"
        self.item_price = 69

        OrderToSend.last_id += 1


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
