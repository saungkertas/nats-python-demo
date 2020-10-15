import asyncio
import os
import signal
import argparse, sys
from proto_read import ReadCardHolder
from nats.aio.client import Client as NATS
from google.cloud import bigquery


async def run(loop):
    nc = NATS()

    async def closed_cb():
        print("Connection to NATS is closed.")
        await asyncio.sleep(0.1, loop=loop)
        loop.stop()

    # It is very likely that the demo server will see traffic from clients other than yours.
    # To avoid this, start your own locally and modify the example to use it.
    options = {
        "servers": args.servers,
        "loop": loop,
        "closed_cb": closed_cb
    }

    await nc.connect(**options)
    print(f"Connected to NATS at {nc.connected_url.netloc}...")

    async def subscribe_handler(msg):
        data = msg.data
        read_card_holder = ReadCardHolder()
        read_card_holder.card_holder.ParseFromString(data)
        row_to_insert = read_card_holder.GetRowToInsert()
        sink_to_bq(args.table,row_to_insert)

    await nc.subscribe(args.subject, cb=subscribe_handler)

    # Subscription on queue named 'workers' so that
    # one subscriber handles message a request at a time.
    await nc.subscribe(args.subject, args.queue, subscribe_handler)

    def signal_handler():
        if nc.is_closed:
            return
        print("Disconnecting...")
        loop.create_task(nc.close())

    for sig in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(getattr(signal, sig), signal_handler)

def sink_to_bq(table_id, row_to_insert):
    rows_to_insert = []
    rows_to_insert.append(row_to_insert)
    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # e.g python3 subscriber_bq_streaming.py subject_name -q queue_name -s nats://159.89.28.145:4222
    parser.add_argument('subject', default='hello', nargs='?')
    parser.add_argument('-s', '--servers', default=[], action='append')
    parser.add_argument('-q', '--queue', default="")
    parser.add_argument('-t', '--table', default="")
    parser.add_argument('--creds', default="")
    args = parser.parse_args()
    client = bigquery.Client()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    try:
        loop.run_forever()
    finally:
        loop.close()
