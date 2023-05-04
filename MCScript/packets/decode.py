from typing import Optional
import struct

class PacketDecode:

    def decode(data: bytes, latency: float) -> "PacketDecode.GameData":
        data = data[1:]
        name_length = struct.unpack(">H", data[32:34])[0]
        decoded_data = data[34 : 34 + name_length].decode().split(";")

        try:
            map_ = decoded_data[7]
        except IndexError:
            map_ = None
        try:
            gamemode = decoded_data[8]
        except IndexError:
            gamemode = None

        return PacketDecode.Local(
            protocol=int(decoded_data[2]),
            brand=decoded_data[0],
            version=decoded_data[3],
            latency=latency,
            players_online=int(decoded_data[4]),
            players_max=int(decoded_data[5]),
            motd=decoded_data[1],
            map_=map_,
            gamemode=gamemode,
        )

    class Local:
        class Version:
            def __init__(self, protocol: int, brand: str, version: str):
                self.protocol = protocol
                self.brand = brand
                self.version = version

        def __init__(
            self,
            protocol: int,
            brand: str,
            version: str,
            latency: float,
            players_online: int,
            players_max: int,
            motd: str,
            map_: Optional[str],
            gamemode: Optional[str],
        ):
            self.version = self.Version(protocol, brand, version)
            self.latency = latency
            self.players_online = players_online
            self.players_max = players_max
            self.motd = motd
            self.map = map_
            self.gamemode = gamemode

