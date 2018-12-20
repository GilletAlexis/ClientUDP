import socket

UDP_IP = "10.160.108.101"
UDP_PORT = 5005
MESSAGE = b'?'

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print ("received message: ", data)
sock.sendto(b"cinema", (UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print ("received message: ", data)

    i=0
    code = 0
    taboctet = []
    for i in range(4):
        taboctet.append(data[i])
        #data >> 8
    code = data[3]<<24 | data[2]<<16 | data[1]<<8 | data[0]
    
    print(taboctet)
    print(code)

    code = str(code)
    sock.sendto(code.encode(), (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    print ("received message: ", data)
