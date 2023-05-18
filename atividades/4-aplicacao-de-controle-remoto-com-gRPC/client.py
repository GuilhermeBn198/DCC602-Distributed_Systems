import grpc
import commands_pb2
import commands_pb2_grpc

def run():
    # Cria um canal de comunicação gRPC com o servidor
    channel = grpc.insecure_channel('localhost:50051')
    stub = commands_pb2_grpc.CommandServiceStub(channel)
    
    # Solicita ao usuário para digitar o comando a ser executado
    command = input("Digite o comando a ser executado: ")
    
    # Cria uma requisição com o comando digitado
    request = commands_pb2.CommandRequest(command=command)
    
    # Chama o método ExecuteCommand do servidor e recebe a resposta
    response = stub.ExecuteCommand(request)
    
    # Exibe o resultado da execução do comando
    print("Resultado:")
    print(response.result)

if __name__ == '__main__':
    run()
