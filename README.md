# PR 01 - Sistemas Distribuidos

## Instruções
Rodar o arquivo "crud_servidor.py"

```
python crud_servidor.py
```

Rodar o arquivo "crud_cliente.py". A variavel ``DO_FIRST_TEST`` define se um teste inicial será executado. Por padrão está como ``False``

```
python crud_cliente.py
```

### Operações Disponíveis
- Inserir
Um nome, email e senha serão requisitados. O retorno será a informação inserida no banco, junto com uuid de 4 digitos.

- Atualizar
Um uuid, nome, email e senha serão requisitados. O retorno será a informação atualizada no banco, ou `none` caso o usuário não exista.

- Achar
Um uuid será requisitado, o retorno será o usuário (com seus respectivos campos), ou `none` caso o usuário não exista.

- Deletar 
Um uuid será requisitado, o retorno será o próprio uuid, ou `none` caso o usuário não exista.