import asyncio
from typing import List

import can
from can.notifier import MessageRecipient


def print_message(msg: can.Message) -> None:
    """Regular callback function. Can also be a coroutine."""
    print(msg)
async def main() -> None:
    """The main function that runs in the loop."""

    with can.Bus(  # type: ignore
        interface="socketcan", channel="can0", bitrate=250000
    ) as bus:
        reader = can.AsyncBufferedReader()
        logger = can.Logger("logfile.asc")

        listeners: List[MessageRecipient] = [
            print_message,  # Callback function
            reader,  # AsyncBufferedReader() listener
            logger,  # Regular Listener object
        ]
        # Create Notifier with an explicit loop to use for scheduling of callbacks
        loop = asyncio.get_running_loop()
        notifier = can.Notifier(bus, listeners, loop=loop)

        while True:
            a = 2+3

if __name__ == "__main__":
    asyncio.run(main())
