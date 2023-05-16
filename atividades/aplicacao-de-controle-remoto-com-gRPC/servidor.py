import grpc
from concurrent import futures
import commands_pb2
import commands_pb2_grpc
import subprocess

class CommandService(commands_pb2_grpc.CommandServiceServicer):
    def ExecuteCommand(self, request, context):
        command = request.command
        result = subprocess.check_output(command, shell=True).decode()
        return commands_pb2.CommandResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    commands_pb2_grpc.add_CommandServiceServicer_to_server(CommandService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
