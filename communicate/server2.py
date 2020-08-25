import base64
import asyncio
import websockets
import socket
import time
import os.path

host = "192.168.43.240"  # 172.31.53.3
port_detection = 3004
port_webOS = 3001
websocket = ""


def getImageFromDetection():
    s = socket.socket()
    s.bind((host, port_detection))
    s.listen(5)
    while True:
        client, addr = s.accept()
        f = open("result.jpg", "wb")
        l = client.recv(8096)
        while (l):
            f.write(l)
            l = client.recv(8096)
        f.close()
        print("File Transmitting Ended")
        client.close()

getImageFromDetection()