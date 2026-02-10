from pb import ping_pb2
from pathlib import Path

BASE_PATH=Path(__file__).resolve().parent
PING_FILEPATH=BASE_PATH/'PING_FILE'

def write()->None:
    ping = ping_pb2.Ping()
    ping.ok=True
    print("ping:", ping.SerializeToString())
    with PING_FILEPATH.open("wb") as f:
        f.write(ping.SerializeToString())

def read()->None:
    ping=ping_pb2.Ping()
    with PING_FILEPATH.open("rb") as f:
        ping.ParseFromString(f.read())
    print("ping ok: ", ping.ok)
    print("", ping)

def main()->None:  
    write()
    read()
    
if __name__=='__main__':
    main()