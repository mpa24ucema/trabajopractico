import json
from models.client import Client


def load_clients():
    clients = []

    with open('src/db/clients_mock.json', 'r') as file:
        clients_json = json.load(file)
        for client in clients_json:
            clients.append(
                Client(
                    client['nombre'],
                    client['apellido'],
                    client['numero_telefonico'],
                    client['email'],
                    client['numero_de_compra'],
                )
            )
    return clients

