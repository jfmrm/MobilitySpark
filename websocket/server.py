import asyncio
import websockets
import pika
import utm

params = pika.ConnectionParameters('127.0.0.1',5672)
connection = pika.BlockingConnection(params)
channel = connection.channel()

def consume():
    payload = []

    for method_frame, properties, body in channel.consume('mobilityData'):
        channel.basic_ack(method_frame.delivery_tag)
        data = Dados(body.decode('utf-8'))
        if len(data) > 0:
            payload.append(data)
            break

    return payload

def Dados(String):
    Info = []
    try:
        Stringlist = String.split(",")
        Info.append(Stringlist[0])
        Info.append(Stringlist[1])
        GPS = utm.to_latlon(int(Stringlist[6]),int(Stringlist[7]), 25, "L")
        Info.append(str(GPS[0]))
        Info.append(str(GPS[1]))
    except:
        print('passing', String)
    return Info

async def serve(websocket, path):
    while True:
        payload = consume()
        for data in payload:
            print(data)
            await websocket.send(', '.join(data))
            await asyncio.sleep(1)

        if len(payload) == 0: break

start_server = websockets.serve(serve, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

connection.close()
