import socket
import json
from crud import CRUD

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = ''
porta = 50000
origem = (ip, porta)


database = CRUD()

tcp.bind(origem)

tcp.listen(1)

tcp_dados, cliente = tcp.accept()

op = 1

while op != 5:

    op = int.from_bytes(tcp_dados.recv(1), 'big')

    if op >= 1 and op <= 4:

        json_string = tcp_dados.recv(500).decode('utf-8')        
        json_string = json_string.rstrip('\x00')
                
        print("Recebido: {}".format(json_string))
        data = json.loads(json_string)

        database_return = {'data' : 'none'}

        # Inserir
        if op == 1:

            database_return = database.store(data)        

        # Atualizar
        elif op == 2:
            if('uuid' in data):
                user_uuid = data['uuid']
                database_return = database.update(user_uuid, data)
                
        # Achar
        elif op == 3:
            if('uuid' in data):
                user_uuid = data['uuid']                
                database_return = database.get(user_uuid)    
        # Deletar
        else:
            if('uuid' in data):
                user_uuid = data['uuid']                
                database_return = database.destroy(user_uuid)
                
        request_response = json.dumps(database_return)
        request_response = str.encode(request_response)
        request_response = request_response + bytes(500 - len(request_response))
        tcp_dados.send(request_response)

tcp_dados.close()

tcp.close()

input('aperte enter para encerrar')
