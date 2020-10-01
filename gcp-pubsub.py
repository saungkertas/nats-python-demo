#!/usr/bin/python3
from google.cloud import pubsub_v1
import asyncio
import requests
import json
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

async def run(loop):
    publisher = pubsub_v1.PublisherClient()
    topic_name = 'projects/charged-ridge-279113/topics/nats'
    nc = NATS()
	
    # It is very likely that the demo server will see traffic from clients other than yours.
    # To avoid this, start your own locally and modify the example to use it.
    # await nc.connect("nats://127.0.0.1:4222", loop=loop)
    await nc.connect("10.148.0.5:4222", loop=loop)

    async def message_handler(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        publisher.publish(topic_name, msg.data)
        print(data)

    # Simple publisher and async subscriber via coroutine.
    sid = await nc.subscribe("telegraf_stdout", cb=message_handler)
    a = {
    "record_date": "2020-05-01",
    "daily_confirmed_cases": 347,
    "daily_deaths": 8,
    "confirmed_cases": 10118,
    "deaths": 792,
    "countries_and_territories": "Indonesia",
    "geo_id": "ID",
    "pop_data_2019": 270625567
    }
    # Stop receiving after 2 messages.
    #await nc.auto_unsubscribe(sid, 3)
    while True:
        await nc.publish("telegraf_stdout", str.encode(json.dumps(a)))
		#await nc.publish("telegraf_stdout", str.encode(b))
        #await nc.publish("telegraf", b'telegraf_test,host=server05,region=asia-east value=0.8')
        #await nc.publish("telegraf", b'telegraf_test,host=server05,region=asia-east value=0.7')

    async def help_request(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print(data)
        #await nc.publish(reply, b'I can help')

    # Use queue named 'workers' for distributing requests
    # among subscribers.
    sid = await nc.subscribe("help", "workers", help_request)

    # Send a request and expect a single response
    # and trigger timeout if not faster than 500 ms.
    try:
        response = await nc.request("help", b'help me', 0.5)
        print("Received response: {message}".format(
            message=response.data.decode()))
    except ErrTimeout:
        print("Request timed out")

    # Remove interest in subscription.
    await nc.unsubscribe(sid)

    # Terminate connection to NATS.
    await nc.close()
	
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()
