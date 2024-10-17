import asyncio
from nats.aio.client import Client as NATS
from nats.js.api import StreamConfig

async def run() -> None:
    nats: NATS = NATS()
    await nats.connect("nats://localhost:4222")

    js = nats.jetstream()

    # Define a stream configuration
    stream: str = "events_stream"
    await js.add_stream(StreamConfig(name=stream, subjects=["events.updates"]))

    # Publish messages to the stream
    await js.publish("events.updates", b"JetStream message 1")
    await js.publish("events.updates", b"JetStream message 2")

    print(f"Published messages to JetStream")

    await nats.close()

if __name__ == "__main__":
    asyncio.run(run())
