import socket

host = '192.168.1.9'
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind the socket with server
# and port number
s.bind(('', port))

# allow maximum 1 connection to
s.listen(5)

# wait till a client accept
c, addr = s.accept()

# display client address
print("CONNECTION FROM:", str(addr))

# encode -> Binary then send
msg1 = "msg From Sayed !!!"
c.send(msg1.encode())

msg2 = "Bye"
c.send(msg2.encode())

# disconnect the server
c.close()