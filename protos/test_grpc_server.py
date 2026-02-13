import asyncio
import logging

import grpc
import pb.ping_pb2 as pb
import pb.ping_pb2_grpc as pb_grpc

class Greeter(pb_grpc.GreeterServicer):
    async def SayHello(
            self,
            request: pb.HelloRequest,
            context: grpc.aio.ServicerContext,
    )-> pb.HelloReply:
        return pb.HelloReply(message=f"Hello, %s!" % request.name)
    
async def serve()->None:
    server=grpc.aio.server()
    pb_grpc.add_GreeterServicer_to_server(Greeter(),server)
    l_addr="[::]:50051"
    server.add_insecure_port(l_addr)
    logging.info("Starting server in %s", l_addr)
    await server.start()
    await server.wait_for_termination()

def main():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())

if __name__=="__main__":
    main()