# TCP Client Steps 
# 1. Create Socket()
# 2. Make Connect() 
# 3. Do Opertations Read() & Write()
# 4. Close() Socket

import socket
# Get The Host name
Client_Name = socket.gethostname()
# Port Number To Connect 
port = 5000
# Make TCP Connection 
# AF_INET => IPv4 Addrees -- AF_INET6 => IPv6 Addrees
# SOCK_STREAM => TCP -- SOCK_DGRAM => UDP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Connect To Server
s.connect((Client_Name, port))
msg1 = input("Enter ur Message To send To Server : " )
s.send(msg1.encode())
print("Message Sent")
data = s.recv(1024)
print("Received Message From Server \"{}\"".format(data.decode()))
s.close()
print("Connection Closed")