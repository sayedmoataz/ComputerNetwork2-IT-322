import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enable broadcasting mode
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.settimeout(0.2)
message = "Broadcast Message"
s.sendto(message.encode(), ('<broadcast>', 5000))
print("message sent!")