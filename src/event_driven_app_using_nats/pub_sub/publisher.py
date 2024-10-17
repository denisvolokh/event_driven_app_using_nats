import asyncio
from nats.aio.client import Client as NATS

async def run() -> None:
    nats: NATS = NATS()

    # Connect to the NATS server
    await nats.connect("nats://localhost:4222")

    # Publishing a message
    subject: str = "events.updates"
    message: str = "Hello, NATS!"
    await nats.publish(subject, message.encode())

    print(f"Published message: {message} to {subject}")

    # Close the connection to the server
    await nats.close()

if __name__ == "__main__":
    asyncio.run(run())
