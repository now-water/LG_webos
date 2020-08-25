import base64
import asyncio
import websockets
import socket
host = "128.0.0.1"#172.31.53.3
port_detection = 3000
port_webOS = 3001

def getImageFromDetection():
    s = socket.socket()
    s.bind((host, port_detection))
    f = open("result.png", "wb")
    s.listen(5)
    while True:
        client, addr = s.accept()
        l = client.recv(8096)
        while(l):
            f.write(l)
            l = client.recv(8096)
        f.close()
        #client.send('Completed Transmitting Image File !')
        print("File Transmitting Ended")
        client.close()

getImageFromDetection()

async def accept_webOS(websocket, path):

    with open("result.png", "rb") as f:
        img_string = base64.b64encode(f.read())  # .encode('utf8')
        print(img_string)
        await websocket.send(img_string)

# # 클라이언트 접속이 되면 호출된다.
# try:
#     server = socketserver.TCPServer((host, port_detection), MyTcpHandler)
#     server.serve_forever()
# except KeyboardInterrupt:
#     print('++++++File server terminate.++++++')

# 웹 소켓 서버 생성.호스트는 localhost에 port + 1로 생성한다. (port는 서버 포트여서 다르게 줬다)

server_webOS = websockets.serve(accept_webOS, host, port_webOS);
asyncio.get_event_loop().run_until_complete(server_webOS)
asyncio.get_event_loop().run_forever()
