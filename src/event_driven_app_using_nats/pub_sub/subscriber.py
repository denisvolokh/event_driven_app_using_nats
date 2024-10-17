import asyncio
from nats.aio.client import Client as NATS
from nats.aio.msg import Msg

async def message_handler(msg: Msg) -> None:
    subject: str = msg.subject
    data: str = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")

async def run() -> None:
    nats: NATS = NATS()

    # Connect to the NATS server
    await nats.connect("nats://localhost:4222")

    # Subscribe to the subject
    subject: str = "events.updates"
    await nats.subscribe(subject, cb=message_handler)

    print(f"Subscribed to '{subject}'")

    # Keep the connection open to listen for messages
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run())
