import asyncio
import websockets
import pika


connection = pika.BlockingConnection()
channel = connection.channel()

def consume():
    payload = []
    for method_frame, properties, body in channel.consume('mobilityData'):
        print(method_frame, properties, body)
        channel.basic_ack(method_frame.delivery_tag)
        payload.append()

        if method_frame.delivery_tag == 10:
            break
    return payload

'''
async def serve():
    name = await websocket.recv()

    print('con')
    await websocket.send('teste')

start_server = websockets.serve(serve, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
'''
connection.close()
