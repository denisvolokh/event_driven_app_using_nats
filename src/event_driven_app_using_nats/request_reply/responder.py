import asyncio
from nats.aio.client import Client as NATS
from nats.aio.msg import Msg

async def request_handler(msg: Msg) -> None:
    request: str = msg.data.decode()
    print(f"Received request: {request}")
    # Respond to the request
    await msg.respond(b"The system is operational")

async def run() -> None:
    nats: NATS = NATS()
    await nats.connect("nats://localhost:4222")

    # Subscribe to the request topic and provide a response
    await nats.subscribe("service.status", cb=request_handler)

    print("Responder is ready to handle requests...")

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run())
