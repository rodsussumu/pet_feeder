import time
from connection import Connection

class Sender:
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        self.conn = Connection(port=port, baud=baud).connect()

    def alimentar(self):
        if(self.conn != 0):
            self.conn.write('open'.encode())
        else:
            time.sleep(30)
            self.conn = Connection(port=self.port, baud=self.baud).connect()
            self.alimentar
