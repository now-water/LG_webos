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


async def accept_webOS(websocket,path):
    previous="1";

    with open("result.jpg", "rb") as f:
        img_string = base64.b64encode(f.read())  # .encode('utf8')
        previous = time.ctime(os.path.getmtime("result.jpg"))
        print("send")
        await websocket.send(img_string)
    # while True:
    #     if os.path.isfile("result.jpg") and previous != time.ctime(os.path.getmtime("result.jpg")):
    #         with open("result.jpg","rb") as f:
    #             img_string = base64.b64encode(f.read())  # .encode('utf8')
    #             previous=time.ctime(os.path.getmtime("result.jpg"))
    #             await websocket.send(img_string)



# def getImageFromDetection():
#     s = socket.socket()
#     s.bind((host, port_detection))
#     s.listen(5)
#     while True:
#         client, addr = s.accept()
#         f = open("result.jpg", "wb")
#         l = client.recv(8096)
#         while (l):
#             f.write(l)
#             l = client.recv(8096)
#         f.close()
#         print("File Transmitting Ended")
#         client.close()
#
# getImageFromDetection()
server_webOS = websockets.serve(accept_webOS, host, port_webOS)
asyncio.get_event_loop().run_until_complete(server_webOS)
asyncio.get_event_loop().run_forever()
