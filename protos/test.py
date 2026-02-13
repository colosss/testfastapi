import test_grpc_client as cli
import test_grpc_server as ser

import asyncio


def main():
    asyncio.run(ser.main())
    asyncio.run(cli.main())

if __name__=="__main__":
    main()