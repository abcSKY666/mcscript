from __future__ import annotations
import warnings
from abc import ABC
from typing import Any, Optional, TYPE_CHECKING

#import dns.resolver
from .decode import *
#import asyncio_dgram
from time import perf_counter
import socket
from .address import Address
from dns import resolver


class Game:
    request_status_data = b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x124Vx"
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.addr = Address(ip, port)

        self.timeout = 3
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.settimeout(self.timeout)

    def get_status(self):
        try:
            start = perf_counter()

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(self.timeout)

            s.sendto(self.request_status_data, self.addr)
            data, _ = s.recvfrom(2048)

            return decode(data, (perf_counter() - start))
        except Exception as err:
            print("[ERROR] Reason:"+err)
        
    
    def send(self, data):
        self.client.sendto(data, self.addr)
