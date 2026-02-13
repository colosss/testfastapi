import asyncio
import logging

import grpc
import pb.ping_pb2 as pb2
import pb.ping_pb2_grpc as pb2_grpc

async def run()->None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub=pb2_grpc.GreeterStub(channel)
        response=await stub.SayHello(pb2.HelloRequest(name="you"))
    print("Greeter client received: "+response.message)


def main():
    logging.basicConfig()
    asyncio.run(run())

if __name__=="__main__":
    main()
