# UDP Client 
# 1. Socket()
# 2. Sendto()
# 3. RecFrom()
# 4. Close 
import socket

Server_Name = socket.gethostname()
Server_IP = socket.gethostbyname(Server_Name)


port = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = "Message From Client To Server Using UDP"
s.sendto(msg.encode(), (Server_IP,port ))		# Sending message to the server
print("Client send this message \"{}\" to the Server".format(msg))
s.close()
