# para executar o programa

## Passo 1: Execute o servidor

```bash
python3 server.py
```

## Passo 2: Execute o cliente

```bash
python3 client.py
```

## Passo 3: Escolha o modo de operação

No terminal do cliente, você será solicitado a escolher um modo de operação: "1" para modo normal ou "2" para ataque de negação de serviço (DOS attack).

Modo normal (1): Nesse modo, você pode enviar mensagens para o servidor e receber as respostas dele.
Modo de ataque de negação de serviço (DOS attack) (2): Nesse modo, o cliente enviará mensagens gigantes repetidamente para o servidor.

Digite "1" ou "2" e pressione Enter para escolher o modo de operação.


## Passo 4: Interaja com o cliente

No modo normal (1):

Digite mensagens no terminal do cliente e pressione Enter para enviá-las ao servidor.

O servidor irá inverter a mensagem recebida e enviá-la de volta ao cliente.

O cliente exibirá a resposta do servidor no terminal.

No modo de ataque de negação de serviço (DOS attack) (2):

O cliente enviará repetidamente mensagens gigantes ao servidor.