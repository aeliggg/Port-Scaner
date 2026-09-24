import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

class Port :
    type = ""
    id:int
    def __init__ (self, name,id):
        self.name=name
        self.id=id

def scan (ip,port:Port):
    if (port.id>0):
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
    else :
        print("Id de port non valide")

def scanRange(ip, portStart:Port,portEnd:Port) :
    if (portStart.id>0 and portEnd.id>0 and portStart.id<portEnd.id) :
        portList=[]
        for j in range (0,portEnd.id-portStart.id+1):
            currentPort=Port("int:{j}",portStart.id+j)
            portList.append(currentPort)
        with ThreadPoolExecutor(max_workers=100) as executor:
            for port in portList:
                executor.submit(scan, ip, port)
        return portList
    else : 
        print ("Id de port(s) non valide(s)")


testPort=Port("test",8000)
testPortEnd=Port("test",8500)
scan("127.0.0.1", testPort)
print(testPort.type)
portList=scanRange("127.0.0.1", testPort,testPortEnd)
for i in range (0,len(portList)) : 
    print(portList[i].type)



    




