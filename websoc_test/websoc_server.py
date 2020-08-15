import asyncio
# 웹 소켓 모듈을 선언한다.	
import websockets
import sys

host = sys.argv[1]
port = sys.argv[2]
# 클라이언트 접속이 되면 호출된다.	
async def accept(websocket, path):
  while True:	
    # 클라이언트로부터 메시지를 대기한다.
    data = await websocket.recv()
    await websocket.send(data + " 가 바라보는 방향에 위치합니다.")
    print(data)
 	
# 웹 소켓 서버 생성.호스트는 localhost에 port + 1로 생성한다. (port는 서버 포트여서 다르게 줬다)
start_server = websockets.serve(accept, host, port + 1);
# 비동기로 서버를 대기한다.	
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
