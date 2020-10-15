import argparse, sys
import asyncio
import os
import signal
from proto_read import ReadCardHolder
from nats.aio.client import Client as NATS
from datetime import datetime
import json


async def run(loop):
    nc = NATS()

    async def closed_cb():
        print('Connection to NATS is closed.')
        await asyncio.sleep(0.1, loop=loop)
        loop.stop()

    # It is very likely that the demo server will see traffic from clients other than yours.
    # To avoid this, start your own locally and modify the example to use it.
    options = {
        # 'servers': ['nats://127.0.0.1:4222'],
        'servers': args.servers,
        'loop': loop,
        'closed_cb': closed_cb
    }

    await nc.connect(**options)
    print(f'Connected to NATS at {nc.connected_url.netloc}...')

    async def subscribe_handler(msg):
        data = msg.data

        read_card_holder = ReadCardHolder()
        read_card_holder.card_holder.ParseFromString(data)
        row_to_insert = read_card_holder.GetRowToInsert()

        filename = datetime.today().strftime('%Y%m%d_%H%M')
        f = open('tmp/'+filename, 'a')
        f.write(json.dumps(row_to_insert)+'\n')
        f.close()

    # Basic subscription to receive all published messages
    # which are being sent to a single topic 'discover'
    await nc.subscribe(args.subject, cb=subscribe_handler)

    # Subscription on queue named 'workers' so that
    # one subscriber handles message a request at a time.
    await nc.subscribe(args.subject, args.queue, subscribe_handler)

    def signal_handler():
        if nc.is_closed:
            return
        print('Disconnecting...')
        loop.create_task(nc.close())

    for sig in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(getattr(signal, sig), signal_handler)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # e.g python3 subscriber_gcs_batch.py subject_name -q queue_name -s nats://159.89.28.145:4222
    parser.add_argument('subject', default='hello', nargs='?')
    parser.add_argument('-s', '--servers', default=[], action='append')
    parser.add_argument('-q', '--queue', default="")
    parser.add_argument('--creds', default="")
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    try:
        loop.run_forever()
    finally:
        loop.close()
