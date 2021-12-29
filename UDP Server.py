# UDP SERVER 
# 1. Socket() 
# 2. Bind()
# 3. recFrom()
# 4. sendTo() 
import socket 

Server_Name = socket.gethostname()
Server_IP = socket.gethostbyname(Server_Name)

port = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((Server_IP , port))
print("Waiting for client...")
(Message , Addrees)  = s.recvfrom(1024) 	#The return value is a pair (bytes, address)
print("UDP Server Received a Message : ",Message.decode()," from",Addrees[0])