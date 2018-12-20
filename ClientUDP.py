import socket

UDP_IP = "10.160.108.101"
UDP_PORT = 5005
MESSAGE = b'?'

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print ("received message: ", data)

sock.sendto(b"cinema", (UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(1024)
print ("received message: ", data)

octet1 = hex(15) and (data>>2)
#octet2 = b'\xff' and (data >> 4)
#octet3 = b'\xff' and (data >> 8)
#octet4 = b'\xff' and (data >> 12)
print (octet1)

#sock.sendto(code, (UDP_IP, UDP_PORT))
#data, addr = sock.recvfrom(1024)
#print ("received message: ", data)
