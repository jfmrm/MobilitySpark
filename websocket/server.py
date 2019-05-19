import asyncio
import websockets
import pika

params = pika.ConnectionParameters('amqp://localhost',5672)
connection = pika.BlockingConnection(params)
channel = connection.channel()

def consume():
    payload = []
    for method_frame, properties, body in channel.consume('mobilityData'):
        print(method_frame, properties, body)
        channel.basic_ack(method_frame.delivery_tag)
        payload.append(body)

        if method_frame.delivery_tag == 10:
            break
    return payload

def tratar():
    pass

async def serve():
    data = consume()
    resp = tratar(data)
    con = await websocket.recv()

    await websocket.send(data)

start_server = websockets.serve(serve, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

connection.close()
