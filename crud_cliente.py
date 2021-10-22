import json
import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

DO_FIRST_TEST = False

ip_serv = '127.0.0.1'     
porta_serv = 50000
dest = (ip_serv, porta_serv)

# Conectando ao servidor TCP (handshake)
tcp.connect(dest)

op = 1

def getUserUUID():
    user_uuid_length = 0
    while(user_uuid_length > 4 or user_uuid_length == 0):
        user_uuid = input("Insira o id do usuario (no máximo 4 characteres): ")
        user_uuid_length = len(user_uuid)
    return {'uuid' : user_uuid}

def getUserData():
    name_length = 0
    email_length = 0
    password_length = 0
    while(name_length > 50 or name_length == 0):
        name = input("Insira um nome (no máximo 50 characteres): ")
        name_length = len(name)
    while(email_length > 50 or email_length == 0):
        email = input("Insira um email (no máximo 50 characteres): ")
        email_length = len(email)
    while(password_length > 50 or password_length == 0):
        password = input("Insira uma senha (no máximo 50 characteres): ")
        password_length = len(password)
    
    return {'name' : name, 'email': email, 'password':password}

if(DO_FIRST_TEST):
    request_body = {"name": "Arthur", "email" : "arthur@email.com", "password" : "senha123"}
    op = 1
    op_b = op.to_bytes(1,'big')
    request_body_str = json.dumps(request_body)
    request_body = str.encode(request_body_str)
    request_body = request_body + bytes(500 - len(request_body))

    tcp.send(op_b + request_body)
    ops_resp = tcp.recv(500).decode('utf-8')
    print(ops_resp)

while op != 5:
    print('Digite:')
    print('1 - Inserir')
    print('2 - Atualizar')
    print('3 - Achar')
    print('4 - Deletar')
    print('5 Sair')

    op = int(input())

    if op >= 1 and op <= 4:

        if(op == 1):
            user_data = getUserData()

            request_body = user_data
        elif(op==2):
            user_uuid_obj = getUserUUID()

            print("Agora insira os novos dados do usuario...")

            user_new_data = getUserData()
            user_new_data['uuid'] = user_uuid_obj['uuid']

            request_body = user_new_data

        elif(op==3 or op == 4):
            user_uuid_obj = getUserUUID()

            request_body = user_uuid_obj

        op_b = op.to_bytes(1,'big')
        request_body_str = json.dumps(request_body)
        request_body = str.encode(request_body_str)
        request_body = request_body + bytes(500 - len(request_body))

        tcp.send(op_b + request_body)        
        ops_resp = tcp.recv(500).decode('utf-8')

        print(ops_resp)
    elif op == 5:
        op_b = op.to_bytes(1,'big')
        tcp.send(op_b)

    
tcp.close()
input('aperte enter para encerrar')
