import base64
import asyncio
import websockets
host = "localhost"
port = "3001"

# 클라이언트 접속이 되면 호출된다.
async def accept(websocket, path):
    with open("result.png", "rb") as f:
        img_string = base64.b64encode(f.read())  # .encode('utf8')
        print(img_string)
        await websocket.send(img_string)

# 웹 소켓 서버 생성.호스트는 localhost에 port + 1로 생성한다. (port는 서버 포트여서 다르게 줬다)
start_server = websockets.serve(accept, host, port);
# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# def sending():
#     with open("../result.jpeg", "rb") as f:
#         img_string = base64.b64encode(f.read()).encode('utf8')
#
#
# sending()