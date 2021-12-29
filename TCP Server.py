# Server TCP 
# 1. socket() => SOCK_STREAM 'TCP' || SOCK_DGRAM 'UDP'
# 2. bind( IP address , host number)
# 3. listen() 
# 4. accept()  => connection , ip addrees 
# 5. read() : do decode() for msgs 
# 6. write() : do encode() for msgs
# 7. close() the sokect
import socket
# Get The Host name and its IPv4 Addrees 
Server_Name = socket.gethostname()
Server_IP = socket.gethostbyname(Server_Name)
# Make Dict to Store The Host name and its IP
Connected_Hosts = {}
Connected_Hosts[Server_Name] = Server_IP
# Port Number To Connect 
port = 5000
# Make TCP Connection 
# AF_INET => IPv4 Addrees -- AF_INET6 => IPv6 Addrees
# SOCK_STREAM => TCP -- SOCK_DGRAM => UDP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Connect To Server
# bind() =>  server -- connect() => client
s.bind((Server_IP, port))
# makes the socket ready for accepting connections.
s.listen(1)
print("Server Listening ....")
# accept incoming connection request from a TCP client
(clientConnection, clientAddress) = s.accept()
# Add this Client To The Hosts Dict
Connected_Hosts["Client1"] = clientAddress[0]
# Print The Dict
print("Connected Hosts :")
print( Connected_Hosts)
# receive data as bytes object -- bufferSize  = 1024 byte
msg = clientConnection.recv(1024)
print("TCP Server Received a Message : \"{}\"".format(msg.decode()))
msg2 = input("Enter Ur Sessage To Send To Client : ")
clientConnection.send(msg2.encode())
s.close()
print("Connection Closed")
