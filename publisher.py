import argparse, sys
import asyncio
import os
import signal
import json
import holder_pb2
from proto_write import WriteCardHolder
from nats.aio.client import Client as NATS

def show_usage():
    usage = """
nats-pub SUBJECT [-d DATA] [-s SERVER]
Example:
python3 pub.py telegraf -d world -s nats://127.0.0.1:4222
"""
    print(usage)

def show_usage_and_die():
    show_usage()
    sys.exit(1)

async def run(loop):
    parser = argparse.ArgumentParser()

    # e.g. nats-pub hello -d "world" -s nats://127.0.0.1:4222 -s nats://127.0.0.1:4223
    parser.add_argument('subject', default='hello', nargs='?')
    parser.add_argument('-d', '--data', default="hello world")
    parser.add_argument('-f', '--file', default="records.txt")
    parser.add_argument('-s', '--servers', default=[], action='append')
    parser.add_argument('--creds', default="")
    args = parser.parse_args()

    nc = NATS()

    async def error_cb(e):
        print("Error:", e)

    async def closed_cb():
        print("Connection to NATS is closed.")

    async def reconnected_cb():
        print(f"Connected to NATS at {nc.connected_url.netloc}...")

    options = {
        "loop": loop,
        "error_cb": error_cb,
        "closed_cb": closed_cb,
        "reconnected_cb": reconnected_cb
    }

    if len(args.creds) > 0:
        options["user_credentials"] = args.creds

    try:
        if len(args.servers) > 0:
            options['servers'] = args.servers

        await nc.connect(**options)
    except Exception as e:
        print(e)
        show_usage_and_die()

    print(f"Connected to NATS at {nc.connected_url.netloc}...")
    
    # filepath = args.file
    # with open(filepath) as fp:
    #     for id, line in enumerate(fp):  
    #         await nc.publish(args.subject, line.encode())

    write_card_holder = WriteCardHolder()
    card_holder_book = holder_pb2.CardHolderBook()
    for x in range(1):
        a = write_card_holder.PromptForAddress(card_holder_book.card_holders.add())
        await nc.publish(args.subject, a.SerializeToString())
    await nc.flush()
    await nc.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run(loop))
    finally:
        loop.close()