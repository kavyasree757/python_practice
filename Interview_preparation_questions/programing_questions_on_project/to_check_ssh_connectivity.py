import socket

ip = "192.168.1.10"
port = 22

s = socket.socket()

try:
    s.connect((ip, port))
    print("SSH is available")
except:
    print("SSH is not available")

s.close()
