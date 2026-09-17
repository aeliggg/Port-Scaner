import socket

class Port :
    type = ""
    id:int
    def __init__ (self, name,id):
        self.name=name
        self.id=id

def scan (ip,port:Port):
    idPort=port.id
    Filtered=False
    timeout = 1
    socketScan=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socketScan.settimeout(timeout)
    try :
        response = socketScan.connect_ex((ip,idPort))
    except socket.timeout:
        port.type="filtered"
        Filtered=True
        ##socketScan.close()
        ##return()
    if Filtered==False :
        if (response==0) :
            port.type="Open"
        else :
            port.type="Closed"
    socketScan.close()

testPort=Port("test",8000)
scan("127.0.0.1", testPort)
print(testPort.type)


    




