import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('8.8.8.8', 80))

def getIp():
    global sock
    return sock.getsockname()[0]