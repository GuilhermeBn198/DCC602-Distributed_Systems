import grpc
import commands_pb2
import commands_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = commands_pb2_grpc.CommandServiceStub(channel)
    
    command = input("Digite o comando a ser executado: ")
    request = commands_pb2.CommandRequest(command=command)
    response = stub.ExecuteCommand(request)
    
    print("Resultado:")
    print(response.result)

if __name__ == '__main__':
    run()
