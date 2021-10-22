# PR 01 - Sistemas Distribuidos

O sistema consiste de um simples CRUD de usuários, que mantém as seguintes informações:

- Nome
- Email
- Senha

## Instruções de execução
Rodar o arquivo "crud_servidor.py"

```
python crud_servidor.py
```

Rodar o arquivo "crud_cliente.py". A variavel ``DO_FIRST_TEST`` define se um teste inicial será executado. Por padrão está como ``False``

```
python crud_cliente.py
```

Após rodar o "crud_cliente.py", basta seguir as instruções exibidas.

### Operações Disponíveis
- Inserir

Um nome, email e senha serão requisitados. O retorno será a informação inserida no banco, junto com uuid de 4 digitos.

- Atualizar

Um uuid, nome, email e senha serão requisitados. O retorno será a informação atualizada no banco, ou `none` caso o usuário não exista.

- Achar

Um uuid será requisitado, o retorno será o usuário (com seus respectivos campos), ou `none` caso o usuário não exista.

- Deletar 

Um uuid será requisitado, o retorno será o próprio uuid, ou `none` caso o usuário não exista.

## Estrutura do pacote de requisição
O primeiro byte é a operação escolhida (1 a 5), e os 500 bytes seguintes correspondem a um json contendo as informações do usuário (nome, email e senha).

Exemplo de inserção:
```
b'1{"nome": "Arthur", "email": "arthur@email.com", "senha": "senha123"}'
```

## Estrutura do pacote de resposta

O pacote consiste de 500 bytes, que correspondem a um json (manipulado no Python como um objeto do tipo Dictionary) contendo as informações respondidas pelo CRUD, no caso de inserção, uma chave ``data`` contendo outro objeto com os atributos do usuário inserido, juntamente com seu ``uuid``, gerado aleatoriamente.

Exemplo de resposta:
```
b'{"data": {"name": "Arthur", "email": "arthur@email.com", "password": "senha123", "uuid": 9005}}'
```