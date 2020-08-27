import base64
import asyncio
import websockets
import socket
import time

def accept_webOS(websocket,path):
     with open("result.jpg", "rb") as f:
            img_string = base64.b64encode(f.read())  # .encode('utf8')
            await websocket.send(img_string)