import asyncio
from nats.aio.client import Client as NATS
from nats.js.api import ConsumerConfig

async def message_handler(msg) -> None:
    subject: str = msg.subject
    data: str = msg.data.decode()
    print(f"Replayed message on '{subject}': {data}")

async def run() -> None:
    nats: NATS = NATS()
    await nats.connect("nats://localhost:4222")

    js = nats.jetstream()

    # Create a consumer configuration to replay messages
    consumer_config: ConsumerConfig = ConsumerConfig(durable_name="replay_consumer")
    await js.subscribe("events.updates", cb=message_handler, consumer_config=consumer_config)

    print(f"Subscribed to JetStream with replay")

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run())
