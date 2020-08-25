import base64
import asyncio
import websockets
import socket
import time
host = "localhost"#172.31.53.3
port_detection = 3000
port_webOS = 3001
websocket = ""

async def accept_webOS(websoc, path):
    print("Client connected !")
    global websocket 
    websocket = websoc
    
def getImageFromDetection():
    global websocket
    s = socket.socket()
    s.bind((host, port_detection))
    s.listen(5)
    while True:
        client, addr = s.accept()
        f = open("result.png", "wb")
        l = client.recv(8096)
        while(l):
            f.write(l)
            l = client.recv(8096)
        f.close()
        
        with open("result.png", "rb") as f:
            img_string = base64.b64encode(f.read())  # .encode('utf8')
            websocket.send(img_string)
        
        print("File Transmitting Ended")
        client.close()

server_webOS = websockets.serve(accept_webOS, host, port_webOS);
getImageFromDetection()
asyncio.get_event_loop().run_until_complete(server_webOS)
asyncio.get_event_loop().run_forever()
