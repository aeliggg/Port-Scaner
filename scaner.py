import socket

class Port :
    type = ["Open", "Closed", "filtered"]
    def __init__ (self, name):
        self.name=name

def scan (ip,port):
    timeout = 1
    socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.connect_ex()




