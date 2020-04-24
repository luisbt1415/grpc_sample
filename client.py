import logging
import grpc
import greeting_pb2
import greeting_pb2_grpc
from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def hello_name(name):
    msg = run(name)
    return msg


def run(name_):
    with grpc.insecure_channel('grpc-server:50051') as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel)
        response = stub.Greeting(greeting_pb2.HelloRequest(name=name_))
    return "Greeter client received: " + response.message


if __name__ == '__main__':
    logging.basicConfig()
    app.run(debug=True, host='0.0.0.0', port=5000)