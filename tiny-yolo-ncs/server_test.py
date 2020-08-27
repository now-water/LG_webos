import base64
import asyncio
import websockets
import time
import os.path


host = "172.20.10.4"  # 172.31.53.3
port_detection = 3001


async def accept_webOS(websocket, path):
    previous=1
    while True:
        if os.path.isfile("result.jpg") and previous!=os.path.getmtime("result.jpg"):
            with open("result.jpg","rb") as f:
                img_string = base64.b64encode(f.read())  # .encode('utf8')
                previous=os.path.getmtime("result.jpg")
                await websocket.send(img_string)
                await asyncio.sleep(0.2)


print("server is run...")
server_webOS = websockets.serve(accept_webOS, host, port_detection)
asyncio.get_event_loop().run_until_complete(server_webOS)
asyncio.get_event_loop().run_forever()
