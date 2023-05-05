"""
MCScript | PingServer
v.1.0.0

"""


import socket
from time import perf_counter
from ModuleImporter import Importer

# 假导入
try:
    from ..packets.id import packets
    from ..packets.decode import PacketDecode
    from ..Client import Client
except:
    pass

mt = Importer(globals()) # Module Tools
mt.Import("../packets/id", "packets") 
mt.Import("../packets/decode", "PacketDecode")
mt.Import("../Client", "Client")

def ping(client: Client):
    try:
        start = perf_counter()

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(client.timeout)

        s.sendto(packets.server.request_status, client.addr)
        data, _ = s.recvfrom(2048)

        return PacketDecode.decode(data, (perf_counter() - start))
    except Exception as err:
        return 