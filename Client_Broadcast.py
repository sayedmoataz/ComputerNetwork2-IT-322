import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Enable broadcasting mode
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 5000))
data, addr = client.recvfrom(1024)
print("received BroadCast message: \"{}\" ".format(data.decode()))