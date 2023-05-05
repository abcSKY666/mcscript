from __future__ import annotations
from typing import Any, Optional, TYPE_CHECKING
import socket
from dns import resolver

# Locals
from packets.decode import *
from foundation.address import Address
from packets.id import packets

class Client:
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.addr = Address(ip, port)

        self.timeout = 3
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.settimeout(self.timeout)
    
    def writePackets(self, data):
        self.client.sendto(data, self.addr)
