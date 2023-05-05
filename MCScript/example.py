from Client import *
from server.ping import ping


test = Client("play.hyperlandsmc.net", 19132)
print(ping(test))
