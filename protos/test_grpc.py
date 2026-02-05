from pb import ping_pb2

def test()->None:
    ping = ping_pb2.Ping()
    ping.ok=True
    print("ping:", ping.SerializeToString())

def main()->None:
    test()

if __name__=='__main__':
    main()