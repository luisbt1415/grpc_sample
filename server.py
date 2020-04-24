from concurrent import futures
import logging
import grpc
import greeting_pb2
import greeting_pb2_grpc
from greeting import greeting


class Greeter(greeting_pb2_grpc.GreeterServicer):
    def Greeting(self, request, context):
        print("Server side print: " + greeting(request.name))
        return greeting_pb2.HelloReply(message=greeting(request.name))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeting_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print('Starting server. Listening on port 50051.')
    logging.basicConfig()
    serve()