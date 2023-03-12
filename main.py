import asyncio
import can

async def read_can_messages(bus):
    while True:
        message = await bus.recv()
        print(message)

async def main():
    # CAN bus interface setup
    bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000)

    # Start async message reading
    asyncio.create_task(read_can_messages(bus))

    # Keep event loop running indefinitely
    while True:
        a = 2+3

if __name__ == '__main__':
    asyncio.run(main())