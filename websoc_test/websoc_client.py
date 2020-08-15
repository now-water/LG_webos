import asyncio	

import websockets	
async def connect():	
    async with websockets.connect("ws://localhost:3001") as websocket:

     await websocket.send(input("input the object name to find : "))

    data = await websocket.recv()
    print(data)

asyncio.get_event_loop().run_until_complete(connect())
