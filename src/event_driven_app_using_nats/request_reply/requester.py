import asyncio
from nats.aio.client import Client as NATS
from nats.aio.msg import Msg

async def run() -> None:
    nats: NATS = NATS()
    await nats.connect("nats://localhost:4222")

    # Send a request and wait for a reply
    response: Msg = await nats.request("service.status", b'What is the system status?', timeout=2)
    reply: str = response.data.decode()
    print(f"Received reply: {reply}")

    await nats.close()

if __name__ == "__main__":
    asyncio.run(run())
