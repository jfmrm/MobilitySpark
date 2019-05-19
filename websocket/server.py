import asyncio
import websockets
import pika
import utm

params = pika.ConnectionParameters('127.0.0.1',5672)
connection = pika.BlockingConnection(params)
channel = connection.channel()

def consume():
    payload = []
    i=0
    for method_frame, properties, body in channel.consume('mobilityData'):
        #print(method_frame, properties, body)
        channel.basic_ack(method_frame.delivery_tag)
        data = Dados(body.decode('utf-8'))
        print(data)
        payload.append(data)
        i+=1

        if i == 10:
            break
    return payload

def Dados(String):
    Info = []
    Stringlist = String.split(",")
    Info.append(Stringlist[0])
    Info.append(Stringlist[1])
    GPS = utm.to_latlon(int(Stringlist[6]),int(Stringlist[7]), 25, "L")
    Info.append(GPS[0])
    Info.append(GPS[1])
    return Info

async def serve(websocket, path):
    data = consume()

    await websocket.send(str(data))

start_server = websockets.serve(serve, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

connection.close()
