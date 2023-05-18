## para executar ambiente virtual python: (caso ñ esteja funcionando no terminal normal)
```bash
Python -m venv venv
./venv/Scripts/activate ou ./venv/bin/activate
Isso daí vai iniciar o ambiente
Aí tu vai dar o pip install das bibliotecas que se quer testar
e executar teu programa
```

# para executar o programa
## Passo 1: Instalação das dependências
```bash
pip install grpcio grpcio-tools
```

## Passo 2: Execute o comando abaixo para gerar o código Python a partir do arquivo commands.proto:
	
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. commands.proto
```

Isso criará os arquivos commands_pb2.py e commands_pb2_grpc.py.

## Passo 3: Execução do servidor e do cliente

```bash
python3 servidor.py
```

```bash
python3 client.py

```

## Passo 4: executar um comando no client. Ex: ls -a