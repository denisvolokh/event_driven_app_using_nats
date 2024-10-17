import asyncio
from nats.aio.client import Client as NATS
from nats.aio.msg import Msg

async def message_handler(msg: Msg) -> None:
    subject: str = msg.subject
    data: str = msg.data.decode()
    print(f"Worker 2 received a message on '{subject}': {data}")

async def run() -> None:
    nats: NATS = NATS()
    await nats.connect("nats://localhost:4222")

    # Subscribe to the subject as part of a queue group
    subject: str = "events.updates"
    queue_group: str = "workers"
    await nats.subscribe(subject, queue=queue_group, cb=message_handler)

    print(f"Worker 2 subscribed to '{subject}' in queue group '{queue_group}'")

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run())
