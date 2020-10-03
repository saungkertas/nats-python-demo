import asyncio
import os
import signal
from proto_read import ReadCardHolder
from nats.aio.client import Client as NATS
from datetime import datetime
import constant


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
        'servers': 'localhost:4222',
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
        f.write(json.dumps(row_to_insert))
        f.close()

    # Basic subscription to receive all published messages
    # which are being sent to a single topic 'discover'
    await nc.subscribe('telegraf', cb=subscribe_handler)

    # Subscription on queue named 'workers' so that
    # one subscriber handles message a request at a time.
    await nc.subscribe('telegraf.*', 'workers', subscribe_handler)

    def signal_handler():
        if nc.is_closed:
            return
        print('Disconnecting...')
        loop.create_task(nc.close())

    for sig in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(getattr(signal, sig), signal_handler)


def create_file(self, filename, rows_to_insert):
    write_retry_params = gcs.RetryParams(backoff_factor=1.1)
    gcs_file = gcs.open(filename,
                        'w',
                        content_type='text/plain',
                        retry_params=write_retry_params)
    gcs_file.write('abcde\n')
    gcs_file.write('f'*1024*4 + '\n')
    gcs_file.close()
    self.tmp_filenames_to_clean_up.append(filename)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    try:
        loop.run_forever()
    finally:
        loop.close()
