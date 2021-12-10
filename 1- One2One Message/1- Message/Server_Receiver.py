import socket

host = '192.168.1.9'
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host, port))

# receive message string from server, at a time 1024 B
msg = s.recv(1024)

# repeat as long as message string are not empty
while msg:
	print('Received:' + msg.decode())
	msg = s.recv(1024)

# disconnect the client
s.close()
