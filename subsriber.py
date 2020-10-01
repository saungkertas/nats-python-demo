import asyncio
import os
import signal
from proto_read import ReadCardHolder
from nats.aio.client import Client as NATS


async def run(loop):
    nc = NATS()

    async def closed_cb():
        print("Connection to NATS is closed.")
        await asyncio.sleep(0.1, loop=loop)
        loop.stop()

    # It is very likely that the demo server will see traffic from clients other than yours.
    # To avoid this, start your own locally and modify the example to use it.
    options = {
        # "servers": ["nats://127.0.0.1:4222"],
        "servers": "localhost:4222",
        "loop": loop,
        "closed_cb": closed_cb
    }

    await nc.connect(**options)
    print(f"Connected to NATS at {nc.connected_url.netloc}...")

    async def subscribe_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data
        
        read_card_holder = ReadCardHolder()
        #print(data)
        # a = bListPeople'\n\x9b\x01\n\x0fNicholas Rivera\x12\x17Clinical cytogeneticist\x1a\n7523889213"409558 Brooks Fields Suite 354\nJasonchester, TX 39801*\x1035243937086347792\x1bDiners Club / Carte Blanche'
        read_card_holder.card_holder_book.ParseFromString(data)
        print(read_card_holder.ListPeople())
        #print(data)
        # print("Received a message on '{subject} {reply}': {data}".format(
            # subject=subject, reply=reply, data=data))

    # Basic subscription to receive all published messages
    # which are being sent to a single topic 'discover'
    await nc.subscribe("telegraf", cb=subscribe_handler)

    # Subscription on queue named 'workers' so that
    # one subscriber handles message a request at a time.
    await nc.subscribe("telegraf.*", "workers", subscribe_handler)

    def signal_handler():
        if nc.is_closed:
            return
        print("Disconnecting...")
        loop.create_task(nc.close())

    for sig in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(getattr(signal, sig), signal_handler)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    try:
        loop.run_forever()
    finally:
        loop.close()
