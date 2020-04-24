# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import greeting_pb2 as greeting__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Greeting = channel.unary_unary(
                '/Greeter/Greeting',
                request_serializer=greeting__pb2.HelloRequest.SerializeToString,
                response_deserializer=greeting__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Greeting(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Greeting': grpc.unary_unary_rpc_method_handler(
                    servicer.Greeting,
                    request_deserializer=greeting__pb2.HelloRequest.FromString,
                    response_serializer=greeting__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Greeting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/Greeting',
            greeting__pb2.HelloRequest.SerializeToString,
            greeting__pb2.HelloReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
